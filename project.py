import hou
from PySide2 import QtWidgets, QtCore
import os
obj = hou.node("/obj/")
class ProjectManager(QtWidgets.QWidget):
    def __init__(self):
        super(ProjectManager, self).__init__()
        self.cwd = hou.getenv('JOB') + '/'
        self.title = QtWidgets.QLabel("Scene Breakdown")
        self.title.setMinimumHeight(30) 
        self.title.setStyleSheet("QLabel{font-size: 16pt;}")
        self.listwidget = QtWidgets.QListWidget()
        self.onCreateInterface()
        self.copySelection = QtWidgets.QPushButton("Copy Selected Node", self)
        self.pasteSelection = QtWidgets.QPushButton("Paste An Object", self)
        self.clearEverything = QtWidgets.QPushButton("Clear Copied Objects", self)
        listLayout = QtWidgets.QVBoxLayout()
        self.copySelection.clicked.connect(self.copy_selection)
        self.pasteSelection.clicked.connect(self.paste_selection)
        self.clearEverything.clicked.connect(self.clear_everything)
        listLayout.addWidget(self.title)
        listLayout.addWidget(self.listwidget)
        listLayout.addWidget(self.copySelection)
        listLayout.addWidget(self.pasteSelection)
        listLayout.addWidget(self.clearEverything)
        self.setLayout(listLayout)
        self.project =  hou.text.expandString("$JOB")
        if not os.path.exists(f"{self.project}/Copied Objects"):
            os.mkdir(f"{self.project}/Copied Objects")
    def openScene(self, item):
        scene  = self.cwd + item.data()
        hou.hipFile.load(scene)
        return scene

    def onCreateInterface(self):

        for file in os.listdir(self.cwd):
            if file.endswith(".hipnc"):
                self.listwidget.addItem(file)
        self.listwidget.doubleClicked.connect(self.openScene)        

    def copy_selection(self): 
        if 'self.output' in locals() :
            self.temp_dir.cleanup()
        if len(hou.selectedNodes()) < 1:
            no_select = PopUpDialog()
            no_select.setParent(hou.qt.floatingPanelWindow(None), QtCore.Qt.Window)
            no_select.show()
            title = QtWidgets.QLabel("No Nodes Are Selected")
            listLayout = QtWidgets.QVBoxLayout()
            listLayout.addWidget(title)
            no_select.setLayout(listLayout)
        else:
            self.currentBottomNode()
            nodename = self.selected[0].name()
            self.output = self.parentNode.createNode('rop_fbx')
            self.output.setFirstInput(self.selected[0])
            self.outname = f"{self.project}/Copied Objects" + "/" +  nodename + ".fbx"
            self.output.parm("sopoutput").set(self.outname)
            self.output.parm("execute").pressButton()
            self.output.destroy()

    def paste_selection(self):
        if not any(fname.endswith('.fbx') for fname in os.listdir(f"{self.project}/Copied Objects")):
            no_select = PopUpDialog()
            no_select.setParent(hou.qt.floatingPanelWindow(None), QtCore.Qt.Window)
            no_select.show()
            title = QtWidgets.QLabel("Nothing Selected")
            listLayout = QtWidgets.QVBoxLayout()
            listLayout.addWidget(title)
            no_select.setLayout(listLayout)
        else:
            object = hou.ui.selectFile(f"{self.project}/Copied Objects")
            obj = hou.node("/obj")
            geo = obj.createNode('geo')  
            self.input = geo.createNode("file")
            self.input.parm("file").set(object)
    def clear_everything(self):
        if os.listdir(f"{self.project}/Copied Objects"):
            filelist = [ f for f in os.listdir(f"{self.project}/Copied Objects")]
            for f in filelist:
                os.remove(os.path.join(f"{self.project}/Copied Objects", f))
    def currentBottomNode(self):
        self.selected = hou.selectedNodes()
        self.parentNode = self.selected[0].parent()
        last = self.parentNode
        for child in self.parentNode.children():
            last = child
        return last

class PopUpDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(PopUpDialog, self).__init__( parent)
        self.setWindowTitle("Error")
        self.resize(200,50)