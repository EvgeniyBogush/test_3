import sys
sys.path.append(r'D:\Revit\test_3')
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit import DB
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from elements import get_type_name 


element = FEC(doc).OfClass(DB.Wall)


with DB.Transaction(doc, 'Set Comments Value') as t:
    t.Start()
    for element in elements :
        type_name = get_type_name(element)
        parameter = element.Parameter[DB.BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS]
        parameter.Set(type_name)
    t.Commit()
    if t.GetStatus() == DB.TransactionStatus.Committed:
        print 'Значения успешно присвоены !'


