import pymel.core as pm

def rtod(an,v):
    if an in ['rx', 'ry', 'rz']:
        v = v / (2*3.1415) * 360.0
    return v

def copyKey(an, fn):
    s = pm.selected()
    attr1 = s[0].attr(an)
    attr2 = s[1].attr(an)
    cn = pm.findKeyframe(attr1, c=True)
    c = pm.PyNode(cn[0])
    for i in range(c.numKeys()):
        pm.currentTime(c.getTime(i) + fn)
        attr2.set(rtod(an, c.getValue(i)))
        pm.setKeyframe(attr2)
                        
def copyKeys(ws):
    fn = ws['SliderGrp'].getValue()
    s = pm.selected()
    if ws['tx'].getValue():
        copyKey('tx', fn)
    if ws['ty'].getValue():
        copyKey('ty', fn)
    if ws['tz'].getValue():
        copyKey('tz', fn)
    if ws['rx'].getValue():
        copyKey('rx', fn)
    if ws['ry'].getValue():
        copyKey('ry', fn)
    if ws['rz'].getValue():
        copyKey('rz', fn)

        
def makeWindow():
    ws = {}
    with pm.window():
        with pm.autoLayout():
            ws = { }
            with pm.horizontalLayout():
                ws['tx'] = pm.checkBox(label='tx', value=True)
                ws['ty'] = pm.checkBox(label='ty', value=True)
                ws['tz'] = pm.checkBox(label='tz', value=True)
            with pm.horizontalLayout():
                ws['rx'] = pm.checkBox(label='rx', value=True)
                ws['ry'] = pm.checkBox(label='ry', value=True)
                ws['rz'] = pm.checkBox(label='rz', value=True)
            with pm.horizontalLayout():
                ws['SliderGrp'] = pm.intSliderGrp(label='遅延フレーム数', field=True,min=0.0, max=100.0, value=0)
            with pm.horizontalLayout():
                pm.button(label='キーのコピー', command =pm.Callback(copyKeys,ws))
makeWindow()

                
