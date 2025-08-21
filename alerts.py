from PyQt6.QtWidgets import QMessageBox

def showCritical(message, title="Error de ejecución", details=''):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)  # Update for PyQt6

    msg.setText(message)
    msg.setWindowTitle(title)

    if details != '':
        msg.setInformativeText(details)
        msg.setDetailedText("Información adicional:")

    msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Update for PyQt6

    retval = msg.exec()  # Updated method name
    print(f"value of pressed message box button: {retval}")


def showWarning(message, title="Advertencia"):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Icon.Warning)  # Update for PyQt6

    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)  # Update for PyQt6

    retval = msgBox.exec()  # Updated method name
    print(f"value of pressed message box button: {retval}")
