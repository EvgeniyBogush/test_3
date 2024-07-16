import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import BuiltInCategory , ElementCategoryFilter , FamilyInstance 
from Autodesk.Revit.DB import ElementId , Category 

filter_doors = ElementCategoryFilter(BuiltInCategory.OST_Doors, True)
filter_windows = ElementCategoryFilter(BuiltInCategory.OST_Windows, True)
filter_model = ElementCategoryFilter(BuiltInCategory.OST_GenericModel, True)

elements = FEC(doc).OfClass(FamilyInstance).WhereElementIsViewIndependent().WherePasses(filter_doors).WherePasses(filter_windows).WherePasses(filter_model)

category_elem = [element.Category for element in elements]
category_Id = [category.Id for category in category_elem]

minId = min(category_Id)
maxId = max(category_Id)
list = list(FEC(doc).OfCategoryId(minId)) + list(FEC(doc).OfCategoryId(maxId))
elemId = [element.Id.IntegerValue for element in list]
print sum(elemId)

