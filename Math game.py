import easygui

def mathquiz():
    points = 0

    points = str(points)
    urespons = easygui.buttonbox("How much is 10 * 9?",
                                 title = "Math game " + points + " points",
                                 choices = ("900","90","9"))
    urespons = int(urespons)
    points = int(points)

    if urespons == 90:
        points = points + 1
        points = str(points)
        easygui.msgbox("correct")
        urespons = easygui.buttonbox("How much is 28 : 4?",
                                     title = "Math game " + points + " points",
                                     choices = ("7","3","14"))
    else:
        easygui.msgbox("incorrect")
        points = str(points)
        urespons = easygui.buttonbox("How much is 28 : 4?",
                                     title = "Math game " + points + " points",
                                     choices = ("7","3","14"))
    points = int(points)
    urespons = int(urespons)

    if urespons == 7:
        points = points + 1
        points = str(points)
        easygui.msgbox("correct")
        urespons = easygui.buttonbox("How much is 100 : 100 *100?",
                                     title = "Math game " + points + " points",
                                     choices = ("0","10000","100"))
    else:
        easygui.msgbox("incorrect")
        points = str(points)
        urespons = easygui.buttonbox("How much is 100 : 100 *100?",
                                     title = "Math game " + points + " points",
                                     choices = ("0","10000","100"))
    points = int(points)
    urespons = int(urespons)

    if urespons == 100:
        points = points + 1
        points = str(points)
        easygui.msgbox("correct")
    else:
        easygui.msgbox("incorrect")
        
    urespons = str(urespons)
    points = int(points)
    return points

points = mathquiz()

if points > 1:
    points = str(points)
    easygui.msgbox("You are good your points are " + points)
elif points <= 1:
    points = int(points)
    urespons = easygui.buttonbox(choices = ("ok","try again"))
    if urespons == "try again":
        mathquiz()
