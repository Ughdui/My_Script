import pymel.core as pm

def makecircle1():

    s=float(1)
    d = new_func1()
    circle1=pm.circle(sweep=270)
    pm.scale(s, s, s)
    circle2=pm.circle(sweep=270)
    pm.scale(d, d, d)
    cur1=str(pm.curve(p=[(-3, 3, 0), (-5, 3, 0), (-2, 6, 0), (1, 3, 0), (-1, 3, 0)], k=[0, 1, 2, 3, 4], d=1))
    pm.rotate(-90, 0, 0)
    pm.scale(0.248, 0.248, 0.248)
    pm.move(-0.743, 0.757, 0)
    pm.attachCurve(circle1[0], circle2[0], cur1, ch=1, bb=0.5, kmk=1, m=0, bki=1, p=0.1, rpo=0)
    pm.delete(circle1[0], circle2[0], cur1)

def new_func1():
    d = new_func()
    return d

def new_func():
    d=1.5
    return d



def makecircle2():
	
    s=float(1)
    d=1.5
    circle4=pm.circle(sweep=-270)
    pm.scale(s, s, s)
    circle5=pm.circle(sweep=-270)
    pm.scale(d, d, d)
    cur2=str(pm.curve(p=[(-3, 3, 0), (-5, 3, 0), (-2, 6, 0), (1, 3, 0), (-1, 3, 0)], k=[0, 1, 2, 3, 4], d=1))
    pm.rotate(90, 0, 0)
    pm.scale(0.248, 0.248, 0.248)
    pm.move(0.742, 1.749, 0)
    pm.attachCurve(circle4[0], circle5[0], cur2, ch=1, bb=0.5, kmk=1, m=0, bki=1, p=0.1, rpo=0)
    pm.delete(circle4[0], circle5[0], cur2)
	


def makecircle3():
	
    pm.curve(p=[(0, 0, -6), (-2, 0, -4), (-1, 0, -4), (-1, 0, -1), (-4, 0, -1), (-4, 0, -2), (-6, 0, 0), (-4, 0, 2), (-4, 0, 1), (-1, 0, 1), (-1, 0, 4), (-2, 0, 4), (0, 0, 6), (2, 0, 4), (1, 0, 4), (1, 0, 1), (4, 0, 1), (4, 0, 2), (6, 0, 0), (4, 0, -2), (4, 0, -1), (1, 0, -1), (1, 0, -4), (2, 0, -4), (0, 0, -6)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)

def makeWindow():
    with pm.window(title="Toolbar"):
        with pm.gridLayout():
            pm.iconTextButton(image1="rotate1.png", command = pm.Callback(makecircle1))
            pm.iconTextButton(image1="rotate2.png", command = pm.Callback(makecircle2))
            pm.iconTextButton(image1="Transform1.png", command = pm.Callback(makecircle3))

makeWindow()
