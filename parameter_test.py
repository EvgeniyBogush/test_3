import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB

elements = FEC(doc).OfClass(DB.WallType)

sum_ids = sum([i.Parameter[DB.BuiltInParameter.ALL_MODEL_TYPE_MARK].Id.IntegerValue for i in elements \
     if i.Parameter[DB.BuiltInParameter.ALL_MODEL_TYPE_MARK] != None])
el_unknown = [i for i in elements if i.Parameter[DB.BuiltInParameter.ALL_MODEL_TYPE_MARK] == None]

el_category =  el_unknown[0].Category.Name
el_parameter =  el_unknown[0].Parameter[DB.BuiltInParameter.ALL_MODEL_TYPE_MARK]

bprint ('{}, {}, {}'.format(sum_ids, el_category, el_parameter))