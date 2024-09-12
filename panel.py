import clr
clr.AddReference("RevitAPI")

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB

elements_type = FEC(doc).OfClass(DB.FamilyInstance).OfCategory(DB.BuiltInCategory.OST_CurtainWallPanels)

sum = int()

for itm in elements_type:
    parameter = itm.Parameter[DB.BuiltInParameter.HOST_AREA_COMPUTED]
    if itm.Name == "Glazed":
        if DB.UnitUtils.ConvertFromInternalUnits(parameter.AsDouble(), parameter.DisplayUnitType) > 1:
            if itm.Id.IntegerValue < 200000:
                sum += itm.Id.IntegerValue

print(sum)
