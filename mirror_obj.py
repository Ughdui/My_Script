import pymel.core as pm

def Mirror_X():
    
    #Merge X
    pm.delete(ch=1)
    mirrorErMergeFirstSelectedObject=pm.ls(sl=1)
    pm.Duplicate()
    mirrorErMergeSecondSelectedObject=pm.ls(sl=1)
    pm.scale(-1, 1, 1, r=1)
    pm.FreezeTransformations()
    pm.select(mirrorErMergeFirstSelectedObject, add=1)
	


def Mirror_Y():
    
    #Merge Y
    pm.delete(ch=1)
    mirrorErMergeFirstSelectedObject=pm.ls(sl=1)
    pm.Duplicate()
    mirrorErMergeSecondSelectedObject=pm.ls(sl=1)
    pm.scale(1, -1, 1, r=1)
    pm.FreezeTransformations()
    pm.select(mirrorErMergeFirstSelectedObject, add=1)
    	


def Mirror_Z():
    
    #Merge Z
    pm.delete(ch=1)
    mirrorErMergeFirstSelectedObject=pm.ls(sl=1)
    pm.Duplicate()
    mirrorErMergeSecondSelectedObject=pm.ls(sl=1)
    pm.scale(1, 1, -1, r=1)
    pm.FreezeTransformations()
    pm.select(mirrorErMergeFirstSelectedObject, add=1)
	

pm.window(toolbox=True,resizeToFitChildren=True, title="mirror")
pm.columnLayout(adjustableColumn=True)
pm.setParent('..')
pm.rowColumnLayout(numberOfRows=1)
pm.iconTextButton(style="textOnly", 
    
    width=109, 
    command=lambda *args: pm.mel.Mirror_X(), 
    backgroundColor=(2, 0.5, 2), 
    label="mirror object X")
pm.setParent('..')
pm.rowColumnLayout(numberOfRows=1)
pm.iconTextButton(style="textOnly", 
    
    width=109, 
    command=lambda *args: pm.mel.Mirror_Y(), 
    backgroundColor=(1, 2, 0), 
    label="mirror object Y")
pm.setParent('..')
pm.rowColumnLayout(numberOfRows=1)
pm.iconTextButton(style="textOnly", 
    
    width=109, 
    command=lambda *args: pm.mel.Mirror_Z(), 
    backgroundColor=(0, 1,2), 
    label="mirror object Z")
pm.showWindow()
