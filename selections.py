import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import BuiltInCategory , ElementCategoryFilter , FamilyInstance

filter_doors = ElementCategoryFilter(BuiltInCategory.OST_Doors, True)
filter_windows = ElementCategoryFilter(BuiltInCategory.OST_Windows, True)
filter_model = ElementCategoryFilter(BuiltInCategory.OST_GenericModel, True)

elements = FEC(doc).OfClass(FamilyInstance).WhereElementIsViewIndependent().WherePasses(filter_doors).WherePasses(filter_windows).WherePasses(filter_model)

bprint(elements)
print(elements.GetElementCount())