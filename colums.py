import clr
clr.AddReference("RevitAPI")

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import BuiltInCategory, Element

column_s = FEC(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType()
column_s_300x300 = [i for i in column_s if Element.Name.__get__(i) == "300mm"]

out = 0
for i in column_s_300x300:
    level_baza = i.LookupParameter('Базовый уровень').AsElementId().IntegerValue
    level_up = i.LookupParameter('Верхний уровень').AsElementId().IntegerValue
    out += (level_baza + level_up)
print out