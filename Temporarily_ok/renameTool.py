import pymel.core as pm

def rename_tool(args):
    Obj = pm.ls(selection=True)
    re_Obj = Obj[::-1]
    inPutName = pm.textField('TFRN',query=1,text=1)
    Obj.insert(0,'x') 
    for i in re_Obj:
        split1 = i.split('|')[-1]
        pm.rename(i ,inPutName + str(Obj.index(i)))

def inserting(args):
    sel_Obj = pm.ls(selection=1,long=1)
    list_Obj = pm.listRelatives(allDescendents=1,fullPath=1,type='transform')
 
    inPutName = pm.textField('TFPre',query=1,text=1)
 
    if list_Obj is not None:
        for one01 in list_Obj:
            split01 = one01.split('|')[-1]
            pm.rename(one01,inPutName+split01)

 
        for one02 in sel_Obj:
            split02 = one02.split('|')[-1]
            pm.rename(one02,inPutName+split02)
 

def makeWindow():
    with pm.window(title="rename"): 
        with pm.frameLayout(label='リネーム', labelAlign='top'):
            pm.rowColumnLayout(numberOfColumns=4)
            pm.text(label=' New Name : ')
            pm.textField('TFRN',text='',width=227)
            pm.text(label='    ')
            pm.button(label='OK',width=50,command=rename_tool) 

        with pm.frameLayout(label='name前に挿入', labelAlign='center'):

            pm.rowColumnLayout(numberOfColumns=4)
            pm.text(label=' Before inserting : ')
            pm.textField('TFPre',text='',width=200)
            pm.text(label='    ')
            pm.button(label='input',width=50,command=inserting)

makeWindow()