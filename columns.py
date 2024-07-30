import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB
doc = __revit__.ActiveUIDocument.Document

elements = FEC(doc).OfCategory(DB.BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType()

grid_params = ['B', 'C', 'G']
el_news = []
for e in elements:
    for g in grid_params:
        if g in e.get_Parameter(DB.BuiltInParameter.COLUMN_LOCATION_MARK).AsString():
            el_news.append(e)
            
with DB.Transaction(doc, 'Set Comments Value') as t:
    t.Start()
    for element in el_news:
        type_name = DB.UnitUtils.ConvertToInternalUnits(150, DB.DisplayUnitType.DUT_MILLIMETERS)
        parameter = element.Parameter[DB.BuiltInParameter.FAMILY_BASE_LEVEL_OFFSET_PARAM]
        parameter.Set(type_name)
    t.Commit()

volumes = int(0)
for e in elements:
    el = e.Parameter[DB.BuiltInParameter.HOST_VOLUME_COMPUTED]
    if DB.UnitUtils.ConvertFromInternalUnits(el.AsDouble(), el.DisplayUnitType) > 0.25:
        volumes += e.Id.IntegerValue
print(volumes)