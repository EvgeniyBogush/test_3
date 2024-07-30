import clr
clr.AddReference("RevitAPI")
import os

from Autodesk.Revit.DB import FilteredElementCollector as FEC

path_file_s = r"D:\Revit\test_3\2020"
name_s = os.listdir(path_file_s)

OUT = 0
for name in name_s:
    doc_file = __revit__.OpenAndActivateDocument(path_file_s + "\\" + name).Document
    OUT += FEC(doc_file,doc_file.ActiveView.Id).ToElements().Count
print OUT