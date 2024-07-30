import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit import DB
from Autodesk.Revit.DB import FilteredElementCollector as FEC

all_rooms = FEC(doc).OfCategory(DB.BuiltInCategory.OST_Rooms)
rooms = []

for room in all_rooms:
    if room.Parameter[DB.BuiltInParameter.ROOM_NAME].AsString() == 'Instruction':
        rooms.append(room)

with DB.Transaction(doc, 'Set Offset Value') as t:
    t.Start()
    for room in rooms:
        parameter = room.Parameter[DB.BuiltInParameter.ROOM_UPPER_OFFSET]
        if room.Parameter[DB.BuiltInParameter.LEVEL_NAME].AsString() == '01 - Entry Level':
            parameter.Set(DB.UnitUtils.ConvertToInternalUnits(3000, parameter.DisplayUnitType))
        if room.Parameter[DB.BuiltInParameter.LEVEL_NAME].AsString() == '02 - Floor':
            parameter.Set(DB.UnitUtils.ConvertToInternalUnits(2800, parameter.DisplayUnitType))
        if room.Parameter[DB.BuiltInParameter.LEVEL_NAME].AsString() == '03 - Floor':
            parameter.Set(DB.UnitUtils.ConvertToInternalUnits(2500, parameter.DisplayUnitType))
    t.Commit()

sum_volume = 0

for room in all_rooms:
    volume_parameter = room.Parameter[DB.BuiltInParameter.ROOM_VOLUME]
    volume = DB.UnitUtils.ConvertFromInternalUnits(volume_parameter.AsDouble(), volume_parameter.DisplayUnitType)
    sum_volume += volume

print sum_volume