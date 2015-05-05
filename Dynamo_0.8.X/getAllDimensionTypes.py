#Copyright(c) 2015, Konrad K Sobon
# @arch_laboratory, http://archi-lab.net

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN

dTypes = FilteredElementCollector(doc).OfClass(DimensionType)
sTypes = FilteredElementCollector(doc).OfClass(SpotDimensionType)

sTypesName = []
for i in sTypes:
	sTypesName.append(i.ToDSType(True).Name)

dimensionTypes = []
for i in dTypes:
	if i.ToDSType(True).Name not in sTypesName:
		dimensionTypes.append(i.ToDSType(True))

#Assign your output to the OUT variable
OUT = dimensionTypes
