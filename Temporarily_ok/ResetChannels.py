import pymel.core as pm

def ResetChannels():
	
    Selected=0
    channels=pm.channelBox('mainChannelBox', q=1, soa=1, ssa=1, sma=1)
    if len(channels)>0:
        Selected=1
		
    for element in pm.ls(sl=1):
        if Selected == 0:
            channels=pm.listAttr(element, k=1)
			
        for channel in channels:
            if pm.objExists(str(element) + "." + str(channel)):
                if pm.getAttr((str(element) + "." + str(channel)), k=1):
                    if not pm.getAttr((str(element) + "." + str(channel)), l=1):
                        default=pm.mel.eval("attributeQuery -n " + str(element) + " -ld " + str(channel))
                        pm.setAttr((str(element) + "." + str(channel)), default[0])



ResetChannels()


#Reference 
#https://felugoblog.wordpress.com/2013/11/06/maya-tip-reset-channels/
