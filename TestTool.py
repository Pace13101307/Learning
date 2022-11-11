import os
from maya import cmds, mel
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui


def maya_main_window():
    try:
        # ~~~ Get the main Maya window, and change it to a Qt object to parent the new window to ~~~ #
        main_window_ptr = omui.MQtUtil.mainWindow()
        # ~~~ wrapInstance changes a C++ object saved in memory at given position into the type requested (QWidget) ~~~ #
        return wrapInstance(int(main_window_ptr),
                            QtWidgets.QWidget)  # int is the new long (py3 uses int, below uses long)
    except Exception:
        return None


class CollapsibleHeader(QtWidgets.QWidget):
    COLLAPSED_PIXMAP = QtGui.QPixmap(":teRightArrow.png")
    EXPANDED_PIXMAP = QtGui.QPixmap(":teDownArrow.png")

    clicked = QtCore.Signal()

    def __init__(self, text, parent=None):
        super(CollapsibleHeader, self).__init__(parent)

        self.setAutoFillBackground(True)
        self.set_background_colour(None)

        self.icon_label = QtWidgets.QLabel()
        self.icon_label.setFixedWidth(self.COLLAPSED_PIXMAP.width())

        self.text_label = QtWidgets.QLabel()
        self.text_label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.setContentsMargins(4, 4, 4, 4)
        self.main_layout.addWidget(self.icon_label)
        self.main_layout.addWidget(self.text_label)

        self.set_text(text)
        self.set_expanded(False)

    def set_text(self, text):
        self.text_label.setText("<p style='font-size:12px'><b>{}</b></p>".format(text))

    def set_background_colour(self, colour):
        if not colour:
            colour = QtWidgets.QPushButton().palette().color(QtGui.QPalette.Button)
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, colour)
        self.setPalette(palette)

    def is_expanded(self):
        return self._expanded

    def set_expanded(self, expanded):
        self._expanded = expanded
        if self._expanded:
            self.icon_label.setPixmap(self.EXPANDED_PIXMAP)
        else:
            self.icon_label.setPixmap(self.COLLAPSED_PIXMAP)

    def mouseReleaseEvent(self, event):
        self.clicked.emit()


class CollapsibleWidget(QtWidgets.QWidget):
    def __init__(self, text, parent=None):
        super(CollapsibleWidget, self).__init__(parent)

        self.header_wdg = CollapsibleHeader(text)
        self.header_wdg.clicked.connect(self.on_header_clicked)
        self.header_wdg.setFixedHeight(CollapsibleHeader.COLLAPSED_PIXMAP.height() * 2)

        self.body_wdg = QtWidgets.QWidget()

        self.body_layout = QtWidgets.QVBoxLayout(self.body_wdg)
        self.body_layout.setContentsMargins(4, 2, 4, 2)
        self.body_layout.setSpacing(3)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.header_wdg)
        self.main_layout.addWidget(self.body_wdg)

        self.set_expanded(False)

    def set_header_background_colour(self, colour):
        self.header_wdg.set_background_colour(colour)

    def add_widget(self, widget):
        self.body_layout.addWidget(widget)

    def add_layout(self, layout):
        self.body_layout.addLayout(layout)

    def set_expanded(self, expanded):
        self.header_wdg.set_expanded(expanded)
        self.body_wdg.setVisible(expanded)

    def on_header_clicked(self):
        self.set_expanded(not self.header_wdg.is_expanded())


class TestTool(QtWidgets.QDialog):
    tool_name = "Test Tool"

    def __init__(self, parent=maya_main_window()):
        # ~~~ Super gives parameters to the given class, giving init the Maya main window Qt object parent argument~~~ #
        super(TestTool, self).__init__(parent)

        self.setWindowTitle(self.tool_name)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.create_widgets()
        self.create_layout()

        self.setMinimumSize(200, 400)

    def create_widgets(self):
        self.collapsible_wdgt_A = CollapsibleWidget("Section A")
        self.collapsible_wdgt_A.set_expanded(True)
        # self.collapsible_wdgt_A.set_header_background_colour(QtCore.Qt.darkRed)
        for name in ["Round", "Bevelled", "Triangular"]:
            widget = QtWidgets.QPushButton("{} Button".format(name))
            # widget.setMaximumSize(widget.sizeHint())
            self.collapsible_wdgt_A.add_widget(widget)

        self.collapsible_wdgt_B = CollapsibleWidget("Section B")
        layout = QtWidgets.QFormLayout()
        for i in range(6):
            layout.addRow("Row {0}".format(i), QtWidgets.QCheckBox())
        self.collapsible_wdgt_B.add_layout(layout)
        self.collapsible_wdgt_C = CollapsibleWidget("Section C")
        widget = QtWidgets.QPushButton("Test 1")
        # widget.setMaximumSize(widget.sizeHint())
        self.collapsible_wdgt_C.add_widget(widget)

        self.collapsible_wdgt_D = CollapsibleWidget("Section D")
        widget = QtWidgets.QPushButton("Test 2")
        # widget.setMaximumSize(widget.sizeHint())
        self.collapsible_wdgt_D.add_widget(widget)

    def create_layout(self):
        self.body_wdg = QtWidgets.QWidget()

        self.body_layout = QtWidgets.QVBoxLayout(self.body_wdg)
        self.body_layout.setContentsMargins(4, 2, 4, 2)
        self.body_layout.setSpacing(3)
        self.body_layout.setAlignment(QtCore.Qt.AlignTop)

        self.body_layout.addWidget(self.collapsible_wdgt_A, 0)
        self.body_layout.addWidget(self.collapsible_wdgt_B, 1)
        self.body_layout.addWidget(self.collapsible_wdgt_C, 2)
        self.body_layout.addWidget(self.collapsible_wdgt_D, 3)

        self.body_scroll = QtWidgets.QScrollArea()
        self.body_scroll.setWidgetResizable(True)
        self.body_scroll.setWidget(self.body_wdg)
        self.body_scroll.setFrameShape(QtWidgets.QFrame.NoFrame)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.body_scroll)


if __name__ == "__main__":
    # ~~~ Prevents the main method from being run when importing ~~~ #
    # ~~~ Try to close the window if it exists, if it does not pass and open ~~~ #
    try:
        TestTool.close()
        TestTool.deleteLater()
    except Exception as test_tool_Error:
        print(test_tool_Error)
    finally:
        test_tool = TestTool()
        test_tool.show()
