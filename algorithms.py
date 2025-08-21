import time

import numpy as np
from skimage import io
from scipy.io import loadmat

try:
    from ALP4 import *
    from seabreeze.spectrometers import Spectrometer
except:
    print('It is not possible to run in real-time')

class Algorithm:
    '''
    Base class for all algorithms
    '''

    def reconstruct_sample(self, data):
        '''
        Reconstructs the data
        '''
        codes = data['codes']
        measurements = data['measurements']
        wavelengths = data['wavelengths']
        num_shots = data['num_shots']
        M = data['M']
        N = M

        x_hat = 0
        x_plot = 0
        for i in range(num_shots):
            time_start = time.time()

            CodeTomar = codes[i]
            CodeTomar = CodeTomar.astype(np.float32)

            measurement = measurements[i]
            intensity_sum = measurement.mean()
            H = CodeTomar * 2 - 1
            x_hat += H * intensity_sum * (1 / M * N)

            x_plot = np.copy(x_hat)
            x_plot -= (x_plot.min() + 1e-8)
            x_plot /= (x_plot.max() + 1e-8)

            x_plot = (x_plot * 255).astype(np.uint8)
            time_elapsed = (time.time() - time_start)

            yield i, dict(x_plot=x_plot, codes=codes, H=H, measurement=measurement,
                          wavelengths=wavelengths, time_elapsed=time_elapsed)

        yield dict(codes=codes, x_plot=x_plot, measurements=measurements, wavelengths=wavelengths)

    def reconstruct_sample_real_time(self, data):
        num_shots = data['num_shots']
        M = data['M']
        integration_time = data['integration_time']
        N = M

        # devices

        DMD = ALP4(version='4.3')
        DMD.Initialize()  # Initialize the device

        # variables

        pp = io.imread("data/dmd_template.bmp")
        pp = pp > 128
        pp_flat = pp.ravel()

        codes = loadmat('data/coded_apertures.mat')['coded_apertures']
        
        CodeTomar = codes[10, :, :]
        CodeTomar = CodeTomar.astype(np.float32)
        Size    = CodeTomar.shape
        Factor = np.array(512 / Size[1])
        Factor = Factor.astype(np.int8)
        Px = 400 - Factor * M / 2
        Px2 = 400 + Factor * M / 2 - 1
        Py = 640 - Factor * N / 2
        Py2 = 640 + Factor * N / 2 - 1

        assert codes.shape[
                0] >= num_shots, "Not enough coded apertures for the selected number of shots, reduce compression ratio"
        
        # start lecture

        measurements = np.zeros((M * M, 512))
        x_hat = 0
        for i in range(num_shots):
            time_start = time.time()

            CodeTomar = codes[i]
            CodeTomar = CodeTomar.astype(np.float32)

            CodeKron = np.kron(CodeTomar,np.ones((Factor, Factor)))
            Base = np.zeros((800,1280))

            # Falta llenar la base con el código de apertura
            Base[Px.astype(np.int16) - 1:Px2.astype(np.int16), 
                Py.astype(np.int16) - 1:Py2.astype(np.int16)] = CodeKron
            Base = 255 * Base.astype(np.uint8)
            imgSeq = Base.ravel()

            # Binary amplitude image (0 or 1)
            bitDepth = 1 
            measurement = 0
            vals = [1, -1]

            for val in vals:
                # Allocate the onboard memory for the image sequence
                # nbImg me dice cuantos codigos quiero poner en secuencia!
                DMD.SeqAlloc(nbImg=1, bitDepth=bitDepth)
                # Send the image sequence as a 1D list/array/numpy array
                if val == -1:
                    code = 255 - imgSeq
                else: 
                    code = imgSeq

                DMD.SeqPut(imgData=code * pp_flat)
                # Set image rate to 50 Hz
                DMD.SetTiming(pictureTime=4000)  # 3000  picture rate [fps] = 1 000 000 / ALP_PICTURE_TIME [µs]
                DMD.Run()
                time.sleep(0.009)  # 0.09

                # CODE PARA ADQUIRIR CON EL ESPECTROMETRO
                number = Spectrometer.from_serial_number()
                number.integration_time_micros(integration_time)  # 30000
                wavelengths = number.wavelengths()
                intensityX = number.intensities()  #-NEGRO
                intensityX = intensityX.astype(np.float64) / 64000
                # print(np.max(intensityX))
                time.sleep(0.015)  # 0.09

                ## CLOSE ESPECTROMETROS
                Spectrometer.close(number)

                # Save
                intensidad_nir = np.array(intensityX)
                intensidad_nir = intensidad_nir
                measurement += intensidad_nir * val * (1)

                intensity_sum = measurement[125:235].mean()

            measurements[i] = measurement
            H = CodeTomar * 2 - 1
            x_hat += H * intensity_sum * (1 / M * N)

            x_plot = np.copy(x_hat)
            x_plot -= (x_plot.min() + 1e-8)
            x_plot /= (x_plot.max() + 1e-8)

            x_plot = (x_plot * 255).astype(np.uint8)
            time_elapsed = (time.time() - time_start)

            yield i, dict(x_plot=x_plot, codes=codes, H=H, measurement=measurement,
                wavelengths=wavelengths, time_elapsed=time_elapsed, DMD=DMD)

        # Stop the sequence display
        DMD.Halt()
        # Free the sequence from the onboard memory
        DMD.FreeSeq()
        # De-allocate the device
        DMD.Free()
        
        yield dict(codes=codes, x_plot=x_plot, measurements=measurements, wavelengths=wavelengths, num_shots=num_shots, M=M)