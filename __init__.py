
# import importlib
# from projectmanager import project
# importlib.reload(project)


# def onCreateInterface():
#     return project.ProjectManager()




#####FOR TESTING #####
# import unittest
# import importlib
# from pathlib import Path
# from projectmanager import testproject
# importlib.reload(testproject)

# def onCreateInterface():
#     s = unittest.TestLoader().loadTestsFromTestCase(AllTests)
#     unittest.TextTestRunner().run(s)
#     return testproject.ProjectManager()
        
# def check_project(test_case):
#   return test_case.cwd
  
# def open_scene(test_case):
#     clicked = example() 
#     opened_file = test_case.openScene(clicked)
#     return opened_file
  
# class AllTests(unittest.TestCase):
#   def test_projectdir(self):
#     example  = testproject.ProjectManager()
#     self.assertEqual(check_project(example), hou.getenv('JOB') + '/')

#   def test_fileopen(self):
#     example  = testproject.ProjectManager()
#     self.assertEqual(open_scene(example), example.cwd + 'BlankHoudiniScene2.hipnc')
  
#   def test_copy(self):
#     example  = testproject.ProjectManager()
#     example.selected = (hou.node('/obj/geo1/box1'), ...)
#     example.parentNode = hou.node('/obj/geo1/')
#     example.copy_selection()
#     my_file = Path('/home/s5531409/HoudiniProjects/ProjectManager/Copied Objects/box1.fbx')
#     isFile = False
#     if my_file.is_file():
#         isFile = True
#     self.assertEqual(isFile, True)
    
#   def test_paste(self):
#     example  = testproject.ProjectManager()
#     example.selected = (hou.node('/obj/geo1/box1'), ...)
#     example.parentNode = hou.node('/obj/geo1/')
#     example.copy_selection()
#     example.paste_selection()
#     isNode = False
#     # print("NODE = ")
#     # print(hou.node("obj/geo2/file1"))
#     if hou.node("obj/geo2/file1")!= None:
#         isNode = True
#     self.assertEqual(isNode, True)
#   def test_clear(self):
#     example  = testproject.ProjectManager()
#     example.selected = (hou.node('/obj/geo1/box1'), ...)
#     example.parentNode = hou.node('/obj/geo1/')
#     example.copy_selection()
#     cleared = False
#     example.clear_everything()
#     if len(os.listdir('/home/s5531409/HoudiniProjects/ProjectManager/Copied Objects')) == 0:
#         cleared  = True
#     self.assertEqual(cleared, True)
# #Mocking the QT signals
# class example():
#     def data(self):
#         return 'BlankHoudiniScene2.hipnc'