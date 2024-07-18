import clr 
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB
from System.Collections.Generic import List

exception_id = [695,136343]
element_id = [DB.ElementId(id) for id in exception_id]

sumId = 0
for view_id in element_id:
    for element in FEC(doc,view_id).OwnedByView(view_id).ToElements():
        if not (element.Name == 'ExtentElem'):
            sumId += element.Id.IntegerValue

print sumId