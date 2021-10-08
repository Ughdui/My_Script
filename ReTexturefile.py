import pymel.core as pm

def TextureFile():
	
	Temp=pm.ls(tex=1)
	Name0="getAttr file"
	Name1=".fileTextureName"
	Name3="setAttr -type \"string\" file"
	i = 0
	for i in range(1,len(Temp) + 1):
		Name2=Name0 + str(i) + Name1
		Temp0=str(pm.mel.eval(Name2))
		Name4=Name3 + str(i) + Name1 + " " + "\"" + Temp0 + "\""
		pm.mel.eval(Name4)
		
	

TextureFile()
