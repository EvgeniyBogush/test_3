import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredWorksetCollector as FWC
from Autodesk.Revit.DB import WorksetKind

set1 = len(list(FWC(doc).OfKind(WorksetKind.ViewWorkset)))
set2 = len(list(FWC(doc).OfKind(WorksetKind.FamilyWorkset)))

print set1 + set2