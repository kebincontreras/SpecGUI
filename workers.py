from collections import deque

import numpy as np
from PyQt6.QtCore import Qt, QThread, pyqtSignal


# Worker class that extends QThread
class Worker(QThread):
    # Define the signal that will carry the NumPy array
    data_signal = pyqtSignal(np.ndarray)

    def __init__(self, intensities=None):
        super().__init__()
        # If a NumPy array is provided, store it
        self.intensities = intensities

    def run(self):
        self.data_signal.emit(self.intensities)