import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from matplotlib.backends.backend_qtagg import NavigationToolbar2QT


class CustomToolbar(NavigationToolbar2QT):
    '''
    Custom toolbar for experiment reports

    Parameters
    ----------
    canvas_ : FigureCanvasQTAgg
        Canvas of the figure
    parent_ : QWidget
        Parent widget

    Attributes
    ----------
    toolitems : tuple
        Tuple of tuples with the toolbar items
    '''

    def __init__(self, canvas_, parent_):
        self.toolitems = (
            ('Home', 'Volver a la vista original', 'home', 'home'),
            ('Back', 'Volver a la vista previa', 'back', 'back'),
            ('Forward', 'Volver a la siguiente vista', 'forward', 'forward'),
            (None, None, None, None),
            ('Pan', 'El botón izquierdo panea, el botón derecho hace zoom\n'
                    'x/y fija el eje, CTRL fija el aspecto', 'move', 'pan'),
            ('Zoom', 'Zoom a rectángulo\nx/y fija el eje', 'zoom_to_rect', 'zoom'),
            ('Subplots', 'Configurar subgráficas', 'subplots', 'configure_subplots'),
            ("Customize", "Editar ejes, curvas y parámetros de la gráfica", "qt4_editor_options", "edit_parameters"),
            (None, None, None, None),
            ('Save', 'Guardar la figura', 'filesave', 'save_figure'),
        )
        NavigationToolbar2QT.__init__(self, canvas_, parent_)


class Graphic(FigureCanvasQTAgg):
    def __init__(self, wavelengths=None, intensities=None):
        # Initialize wavelengths and intensities
        self.wavelengths = wavelengths
        self.intensities = intensities

        # Create a figure and configure the layout once
        self.figure, self.ax = plt.subplots()
        self.figure.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.90, wspace=0.4)

        # Initialize the canvas
        super().__init__(self.figure)
        self.restart_figure()

    def update_data(self, wavelengths=None, intensities=None):
        """Update wavelengths and/or intensities."""
        if wavelengths is not None:
            self.wavelengths = wavelengths
        if intensities is not None:
            self.intensities = intensities

    def get_intensities_by_indices(self, indices=None):
        if self.intensities.ndim > 1:
            return self.intensities if indices is None else self.intensities[indices, :]
        else:
            return self.intensities

    def update_figure(self, indices=None):
        """Clear and update the figure with the latest data."""
        if self.wavelengths is None or self.intensities is None:
            return  # Avoid plotting if no data

        intensities = self.get_intensities_by_indices(indices=indices)
        intensities = intensities[30:-30] if intensities.ndim == 1 else intensities[:, 30:-30].T


        # Clear the axes and plot updated data
        self.ax.clear()
        self.ax.plot(self.wavelengths[30:-30], intensities)

        # Set axis labels and update layout
        self.ax.set_xlim([self.wavelengths[30], self.wavelengths[-30]])
        self.ax.set_xlabel('Wavelength [nm]')
        self.ax.set_ylabel('Intensity')
        self.ax.grid('on')

        self.figure.tight_layout()
        self.draw()

    def restart_figure(self):
        """Clear and restart the figure for new plots."""
        # Clear the current axes and figure
        self.ax.clear()

        # Optionally reset data to None if you want to clear everything
        self.wavelengths = None
        self.intensities = None

        # Reset axis labels
        self.ax.set_xlabel('Wavelength [nm]')
        self.ax.set_ylabel('Intensity')

        # Reapply layout and redraw
        self.figure.tight_layout()
        self.draw()
