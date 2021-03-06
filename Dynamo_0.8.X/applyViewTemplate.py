# Copyright(c) 2015, Konrad Sobon
# @arch_laboratory, http://archi-lab.net

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN

views = UnwrapElement(IN[0])
viewTempName = IN[1]

try:
	errorReport = None
	
	collector = FilteredElementCollector(doc).OfClass(View)
	for i in collector:
		if i.IsTemplate == True and i.Name == viewTempName:
			viewTemp = i
			
	TransactionManager.Instance.EnsureInTransaction(doc)
	for i in views:
		i.ViewTemplateId = viewTemp.Id
	TransactionManager.Instance.TransactionTaskDone()
except:
	# if error accurs anywhere in the process catch it
	import traceback
	errorReport = traceback.format_exc()

#Assign your output to the OUT variable
if errorReport == None:
	OUT = views
else:
	OUT = errorReport
