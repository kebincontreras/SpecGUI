import os
import sys
import time

import numpy as np
import scipy.io as sio
from PyQt6.QtCore import QCoreApplication
from PyQt6 import QtWidgets

from alerts import showWarning
from graphics import Graphic, CustomToolbar
from guis.spec_gui import Ui_MainWindow
import guis.icons.icons  # Importa el archivo generado por pyside6-rcc

from seabreeze.spectrometers import Spectrometer

from workers import Worker


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(QCoreApplication.translate("MainWidget",
                                                       u"Adquicisión de Muestras Espectrales",
                                                       None))

        self.init_spectrometer_info()
        self.init_actions()
        self.init_variables()

    def init_spectrometer_info(self):
        try:
            spectrometer = Spectrometer.from_serial_number()
            print('Spectrometer found!')

            self.modelNameLineEdit.setText(spectrometer.model)
            self.serialNumberLineEdit.setText(spectrometer.serial_number)
            self.pixelsLineEdit.setText(str(spectrometer.pixels))
            self.maxIntensityLineEdit.setText(str(spectrometer.max_intensity))

            wavelengths = spectrometer.wavelengths()[30:-30]
            self.spectralRangeLineEdit.setText(str(f'{wavelengths[0]:.2f} - {wavelengths[-1]:.2f} [nm]'))

        except:
            showWarning('Spectrometer device has not been found or is not ready.')
            self.manualSamplePushButton.setEnabled(False)

    def closeEvent(self, event):
        """Override the closeEvent method to handle the close event."""
        message = QtWidgets.QMessageBox(self)
        message.setWindowTitle("Confirmación")
        message.setText("¿Estás seguro de que deseas salir?")
        message.setIcon(QtWidgets.QMessageBox.Icon.Question)

        # Add standard buttons
        yes_button = message.addButton(QtWidgets.QMessageBox.StandardButton.Yes)
        no_button = message.addButton(QtWidgets.QMessageBox.StandardButton.No)

        # Customize button text
        yes_button.setText("Sí")
        no_button.setText("No")
        message.exec()

        # Check which button was pressed
        if message.clickedButton() == yes_button:
            event.accept()  # Allow window to close
        else:
            event.ignore()  # Ignore the closing event

    def init_actions(self):
        self.loadSamplePushButton.clicked.connect(self.load_files)
        self.manualSamplePushButton.clicked.connect(self.acquire_manual_sample)
        self.savePushButton.clicked.connect(self.save_files)
        self.restartAllPushButton.clicked.connect(self.restart_acquired_samples)

        self.sampleComboBox.currentTextChanged.connect(self.sample_changed)
        self.sampleResultsComboBox.currentTextChanged.connect(self.sample_results_changed)
        self.plotSamplesSpinBox.valueChanged.connect(self.plot_samples_changed)

        self.restartAllPushButton.setEnabled(False)
        self.savePushButton.setEnabled(False)

    def init_variables(self):
        '''
        Initialize variables.
        '''
        sample_acquisition_template = dict(load_sample_lineedit='',
                                           time_spinbox=1000,
                                           current_samples_lineedit=0,
                                           current_samples_combobox='Borrar',
                                           current_samples_spinbox=0)
        self.sample_acquisition = dict(Blanco=sample_acquisition_template.copy(),
                                       Negro=sample_acquisition_template.copy(),
                                       Muestra=sample_acquisition_template.copy())

        visualization_template = dict(save_sample_lineedit='',
                                      plot_samples_spinbox=0)
        self.visualization = dict(Blanco=visualization_template.copy(),
                                  Negro=visualization_template.copy(),
                                  Muestra=visualization_template.copy())

        wavelengths = None
        storage_acquisition_template = dict(samples=None,
                                            wavelengths=wavelengths)
        try:
            spectrometer = Spectrometer.from_serial_number()
            wavelengths = spectrometer.wavelengths()[30:-30]

            storage_acquisition_template['spectrometer'] = dict(model=spectrometer.model,
                                                                serial_number=spectrometer.serial_number,
                                                                pixels=spectrometer.pixels,
                                                                max_intensity=spectrometer.max_intensity,
                                                                spectral_range=dict(init=wavelengths[0],
                                                                                    end=wavelengths[-1],
                                                                                    unit='nm')
                                                                )
        except:
            print('Spectrometer information wont be stored when you save your captured data')

        self.storage_acquisition = dict(Blanco=storage_acquisition_template.copy(),
                                        Negro=storage_acquisition_template.copy(),
                                        Muestra=storage_acquisition_template.copy())

        self.backup_samples = dict(Blanco=None, Negro=None, Muestra=None)

        self.graphics = dict(Blanco=Graphic(wavelengths=wavelengths),
                             Negro=Graphic(wavelengths=wavelengths),
                             Muestra=Graphic(wavelengths=wavelengths))
        self.whitePlotVLayout.addWidget(CustomToolbar(self.graphics['Blanco'], self))
        self.whitePlotVLayout.addWidget(self.graphics['Blanco'])
        self.blackPlotVLayout.addWidget(CustomToolbar(self.graphics['Negro'], self))
        self.blackPlotVLayout.addWidget(self.graphics['Negro'])
        self.samplePlotVLayout.addWidget(CustomToolbar(self.graphics['Muestra'], self))
        self.samplePlotVLayout.addWidget(self.graphics['Muestra'])

    def load_files(self):
        """
        Load files in the software with filenames.
        """
        kwargs = {}
        if 'SNAP' in os.environ:
            kwargs['options'] = QtWidgets.QFileDialog.Option.DontUseNativeDialog

        # Setting the dialog box for opening files
        dialog = QtWidgets.QFileDialog()
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)  # Switch to opening mode
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)  # Allow selecting existing files
        # dialog.setNameFilter("Math Files (*.mat *.npy)")  # File type filter
        dialog.setNameFilter("Matlab Files (*.mat);;Numpy Files (*.npz)")  # File type filter
        dialog.setOption(QtWidgets.QFileDialog.Option.DontUseCustomDirectoryIcons, True)  # Show extensions explicitly

        # Show the dialog box
        if dialog.exec():
            def to_dict(obj):
                if isinstance(obj, np.ndarray):
                    if obj.dtype.names:  # Array estructurado
                        return {name: to_dict(obj[name]) for name in obj.dtype.names}
                    if obj.size == 1:  # Si tiene un solo elemento, devolver ese elemento
                        return to_dict(obj.item())
                    return [to_dict(el) for el in obj]  # Si es un array estándar
                if isinstance(obj, (np.generic, np.number)):
                    return obj.item()  # Convertir NumPy a tipos nativos
                return obj  # Otros tipos (cadenas, listas, etc.)

            load_filename = dialog.selectedFiles()[0]  # Get the selected file
            self.sample_acquisition[self.sampleComboBox.currentText()]['load_sample_lineedit'] = load_filename
            self.loadSampleLineEdit.setText(load_filename.split('/')[-1])

            sample_name = self.sampleComboBox.currentText()
            extension_name = load_filename.split('.')[-1]
            try:
                if 'mat' == extension_name:
                    data = sio.loadmat(load_filename)
                else:  # npz
                    data = dict(np.load(load_filename, allow_pickle=True))

                data['spectrometer'] = to_dict(data['spectrometer'])

            except:
                showWarning('El archivo cargado no corresponde a uno guardado mediante este software. '
                            'Por favor asegurese de cargar solo archivos que fueron guardados mediante '
                            'este Software.')

            self.storage_acquisition[sample_name]['samples'] = data['samples']
            self.storage_acquisition[sample_name]['wavelengths'] = data['wavelengths'].squeeze()

            spectrometer = data['spectrometer']
            self.storage_acquisition[sample_name]['spectrometer'] = dict(model=spectrometer['model'],
                                                                         serial_number=spectrometer['serial_number'],
                                                                         pixels=spectrometer['pixels'],
                                                                         max_intensity=spectrometer['max_intensity'],
                                                                          spectral_range=dict(
                                                                             init=spectrometer['spectral_range']['init'],
                                                                             end=spectrometer['spectral_range']['end'],
                                                                             unit=spectrometer['spectral_range']['unit'])
                                                                         )

            # update GUI

            samples = self.storage_acquisition[sample_name]['samples']
            self.sample_acquisition[sample_name]['current_samples_lineedit'] = 1 if samples.ndim == 1 else len(
                samples)
            self.sample_acquisition[sample_name]['current_samples_spinbox'] = 1 if samples.ndim == 1 else len(
                samples)

            # plot acquired sample

            self.graphics[sample_name].update_data(
                wavelengths=self.storage_acquisition[sample_name]['wavelengths'],
                intensities=samples)
            self.graphics[sample_name].update_figure()

            self.update_sample_acquisition_components(sample_name)
            if sample_name == self.sampleResultsComboBox.currentText():
                self.update_sample_visualization_components(sample_name)

            print(f"Archivo cargado: {load_filename}")  # Process the selected files
        else:
            print("No se seleccionaron archivos.")

    def save_files(self):
        """
        Save files in the software with filenames.
        """
        kwargs = {}
        if 'SNAP' in os.environ:
            kwargs['options'] = QtWidgets.QFileDialog.Option.DontUseNativeDialog

        # Create a dialog to save files
        dialog = QtWidgets.QFileDialog()
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)  # Set to Save mode
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)  # Allow any file name
        dialog.setNameFilter("Matlab Files (*.mat);;Numpy Files (*.npz)")  # File type filter
        dialog.setOption(QtWidgets.QFileDialog.Option.DontUseCustomDirectoryIcons, True)  # Show extensions explicitly

        # Show the dialog
        if dialog.exec() == QtWidgets.QFileDialog.DialogCode.Accepted:
            saved_filename = dialog.selectedFiles()[0]  # Get the selected file
            # selected_filter = dialog.selectedNameFilter()
            # saved_filename = saved_filename + '.mat' if 'Matlab' in selected_filter else saved_filename + '.npy'

            self.visualization[self.sampleResultsComboBox.currentText()]['save_sample_lineedit'] = saved_filename
            self.saveSamplelineEdit.setText(saved_filename.split('/')[-1])

            # save file according with the extension

            extension_name = saved_filename.split('.')[-1]
            if 'mat' == extension_name:
                sio.savemat(saved_filename, self.storage_acquisition[self.sampleResultsComboBox.currentText()])

            else:  # npy
                np.savez(saved_filename, **self.storage_acquisition[self.sampleResultsComboBox.currentText()])

            print(f"File saved as: {saved_filename}")
        else:
            print("No file was saved.")

    def acquire_manual_sample(self):
        self.manualSamplePushButton.setEnabled(False)

        # try:
        spec = Spectrometer.from_serial_number()
        spec.integration_time_micros(int(self.integrationTimeSpinBox.value()))
        wavelengths = spec.wavelengths()
        intensities = spec.intensities()

        time.sleep(0.015)
        Spectrometer.close(spec)

        # save info in a variable

        sample_name = self.sampleComboBox.currentText()

        if self.storage_acquisition[sample_name]['wavelengths'] is None:
            self.storage_acquisition[sample_name]['wavelengths'] = wavelengths

        if self.storage_acquisition[sample_name]['samples'] is None:
            self.storage_acquisition[sample_name]['samples'] = intensities
        else:
            self.storage_acquisition[sample_name]['samples'] = np.vstack(
                [self.storage_acquisition[sample_name]['samples'],
                 intensities])

        # plot acquired sample

        samples = self.storage_acquisition[sample_name]['samples']
        self.graphics[sample_name].update_data(wavelengths=self.storage_acquisition[sample_name]['wavelengths'],
                                               intensities=samples)
        self.graphics[sample_name].update_figure()

        # update gui components

        self.sample_acquisition[sample_name]['current_samples_lineedit'] = 1 if samples.ndim == 1 else len(samples)
        self.sample_acquisition[sample_name]['current_samples_spinbox'] = 1 if samples.ndim == 1 else len(samples)

        self.update_sample_acquisition_components(sample_name)

        if sample_name == self.sampleResultsComboBox.currentText():
            self.update_sample_visualization_components(sample_name)

        print('Success!')

        self.manualSamplePushButton.setEnabled(True)

    def sample_changed(self, text):
        '''
        Sample changed event.

        Parameters
        ----------
        text : str
            Text of the combo box.
        '''
        self.update_sample_acquisition_components(text)

    def update_sample_acquisition_components(self, sample_name):
        sample_variables = self.sample_acquisition[sample_name]
        self.loadSampleLineEdit.setText(str(sample_variables['load_sample_lineedit'].split('/')[-1]))
        self.currentSamplesLineEdit.setText(str(sample_variables['current_samples_lineedit']))
        self.restartAllPushButton.setEnabled(True if int(self.currentSamplesLineEdit.text()) > 0 else False)
        self.restartAllPushButton.clicked.connect(self.restart_acquired_samples)

    def update_sample_visualization_components(self, sample_name):
        samples = self.storage_acquisition[sample_name]['samples']
        if samples is None:
            self.visualization[sample_name]['plot_samples_spinbox'] = 0
        else:
            self.visualization[sample_name]['plot_samples_spinbox'] = 1 if samples.ndim == 1 else len(samples)

        visualization_variables = self.visualization[sample_name]
        self.saveSamplelineEdit.setText(str(visualization_variables['save_sample_lineedit'].split('/')[-1]))
        self.plotSamplesSpinBox.setMaximum(int(visualization_variables['plot_samples_spinbox']))
        self.plotSamplesSpinBox.setValue(int(visualization_variables['plot_samples_spinbox']))

        self.savePushButton.setEnabled(True if self.storage_acquisition[sample_name]['samples'] is not None else False)

    def restart_acquired_samples(self):
        self.restartAllPushButton.setEnabled(False)
        sample_name = self.sampleComboBox.currentText()
        self.storage_acquisition[sample_name]['samples'] = None

        # update gui components

        self.sample_acquisition[sample_name]['load_sample_lineedit'] = ''
        self.sample_acquisition[sample_name]['current_samples_lineedit'] = 0
        self.sample_acquisition[sample_name]['current_samples_spinbox'] = 0
        self.update_sample_acquisition_components(sample_name)
        if sample_name == self.sampleResultsComboBox.currentText():
            self.update_sample_visualization_components(sample_name)
        self.graphics[sample_name].restart_figure()

    def sample_results_changed(self, text):
        '''
        Sample results changed event.

        Parameters
        ----------
        text : str
            Text of the combo box.
        '''
        self.update_sample_visualization_components(text)

    def plot_samples_changed(self, value):
        '''
        Plot samples changed event.

        Parameters
        ----------
        value : int
            Value of the spin box.
        '''
        visualization_name = self.sampleResultsComboBox.currentText()
        visualize_num_samples = self.plotSamplesSpinBox.value()

        indices = np.arange(0, visualize_num_samples, 1).astype(int)
        self.graphics[visualization_name].update_figure(indices=indices)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
