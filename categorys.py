import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import BuiltInParameter, FilteredElementCollector as FEC
from System.Enum import GetValues

elements = FEC(doc).WhereElementIsElementType()

ids = [-1010103, -1010109, -1010108]

b_parameters = [b_parameter for b_parameter in GetValues(BuiltInParameter) if int(b_parameter) in ids]

n = 0
for element in elements:
    for i in b_parameters:
        if element.Parameter[i]:
            n += 1
print n