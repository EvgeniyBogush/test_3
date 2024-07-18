import clr 
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB
from System.Collections.Generic import List

type_wall = DB.ElementClassFilter(DB.WallType)
type_floor = DB.ElementClassFilter(DB.FloorType)
type_roof = DB.ElementClassFilter(DB.RoofType)
type_rooms = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Rooms)
type_stairs = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Stairs)
type_mullions = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_CurtainWallMullions)

all_filters = [type_rooms, type_floor, type_mullions, type_roof,type_stairs,type_wall]
all_filters_types = List[DB.ElementFilter](all_filters)
logical_or_filter = DB.LogicalOrFilter(all_filters_types)

elemUniqueId = [
'07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b3',
'07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b4',
'07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b6',
'07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b7',
'07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b9',
'07ae6064-8e02-489e-896d-f7554545ebb2-0002d8ba',
'07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bc',
'07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bd',
'07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bf',
]

listUniqueId = [doc.GetElement(itm).Id for itm in elemUniqueId]
list_exclusion = List[DB.ElementId](listUniqueId)
list_filter = DB.ExclusionFilter(list_exclusion)



elements = FEC(doc).WherePasses(logical_or_filter).WherePasses(list_filter)
print(sum([element.Id.IntegerValue for element in elements]))

