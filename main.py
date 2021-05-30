import wx
import cv2
import pickle

countcrowd = False
humanTracking = False
weaponDetection = False
sensitiveArea = False
anomalyDetection = False
emotionDetection = False
calculateLineCross = False

videoSource = 0


def GetAvailableSource():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(str(index))
        cap.release()
        index += 1
    return arr


# calculation flags
def countcrowd(e):
    sender = e.GetEventObject()
    isChecked = sender.GetValue()

    global countcrowd
    if isChecked:
        countcrowd = True
        print(countcrowd)
    else:
        countcrowd = False
        print(countcrowd)


def humanTracking(e):
    sender = e.GetEventObject()
    isChecked = sender.GetValue()

    global humanTracking
    if isChecked:
        humanTracking = True
        print(humanTracking)
    else:
        humanTracking = False
        print(humanTracking)


def weaponDetection(e):
    sender = e.GetEventObject()
    isChecked = sender.GetValue()

    global weaponDetection
    if isChecked:
        weaponDetection = True
        print(weaponDetection)
    else:
        weaponDetection = False
        print(weaponDetection)


def sensitiveArea(e):
    sender = e.GetEventObject()
    isChecked = sender.GetValue()

    global sensitiveArea
    if isChecked:
        sensitiveArea = True
        print(sensitiveArea)
    else:
        sensitiveArea = False
        print(sensitiveArea)


# visual flags
def anomalyDetection(e):
    sender = e.GetEventObject()
    isChecked = sender.GetValue()

    global anomalyDetection
    if isChecked:
        anomalyDetection = True
        print(anomalyDetection)
    else:
        anomalyDetection = False
        print(anomalyDetection)


def emotionDetection(e):
    sender = e.GetEventObject()
    isChecked = sender.GetValue()

    global emotionDetection
    if isChecked:
        emotionDetection = True
        print(emotionDetection)
    else:
        emotionDetection = False
        print(emotionDetection)


def CalculateLineCross(e):
    sender = e.GetEventObject()
    isChecked = sender.GetValue()

    global calculateLineCross
    if isChecked:
        calculateLineCross = True
        print(calculateLineCross)
    else:
        calculateLineCross = False
        print(calculateLineCross)


class App(wx.Frame):
    def __init__(self, parent, title):
        super(App, self).__init__(parent, title=title)
        self.widgets()
        self.Show()
        self.SetSize(370, 500)

    # Declare a function to add new buttons, icons, etc. to our app
    def widgets(self):
        pnl = wx.Panel(self)
        # Check box show direction
        cbcountcrowd = wx.CheckBox(pnl, label='Crowd Detection and Counting', pos=(10, 0))
        cbcountcrowd.SetValue(False)
        cbcountcrowd.Bind(wx.EVT_CHECKBOX, countcrowd)

        # Check box Show people count
        cbShowCount = wx.CheckBox(pnl, label='Weapon Detection', pos=(10, 20))
        cbShowCount.SetValue(False)
        cbShowCount.Bind(wx.EVT_CHECKBOX, humanTracking)

        # Check box Show people count
        cbweaponDetection = wx.CheckBox(pnl, label='Human Tracking', pos=(10, 40))
        cbweaponDetection.SetValue(False)
        cbweaponDetection.Bind(wx.EVT_CHECKBOX, weaponDetection)

        # Check box Show people count
        cbsensitiveArea = wx.CheckBox(pnl, label='Face Emotion Detection', pos=(10, 60))
        cbsensitiveArea.SetValue(False)
        cbsensitiveArea.Bind(wx.EVT_CHECKBOX, sensitiveArea)

        # Check box Show people count
        cbanomalyDetection = wx.CheckBox(pnl, label='Anomaly Detection', pos=(10, 80))
        cbanomalyDetection.SetValue(False)
        cbanomalyDetection.Bind(wx.EVT_CHECKBOX, anomalyDetection)

        # Check box Show people count
        cbemotionDetection = wx.CheckBox(pnl, label='Sensitive Area Monitoring', pos=(10, 100))
        cbemotionDetection.SetValue(False)
        cbemotionDetection.Bind(wx.EVT_CHECKBOX, emotionDetection)

        lblList = ['Default Camera', 'External Video']

        self.rbox = wx.RadioBox(pnl, label='Video Source', pos=(10, 170), choices=lblList,
                                majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.SetVal)

        self.basicText = wx.TextCtrl(pnl, -1, 'http://root:root@192.168.70.52/mjpg/1/video.mjpg', size=(300, -1),
                                     pos=(10, 230))

        # self.labelDetection = wx.StaticText(pnl, label="Enter the detections", pos=(10, 260), style=0)

        self.basicTextt = wx.TextCtrl(pnl, -1, size=(0, -1), pos=(0, 0))
        closeButton = wx.Button(pnl, label='Start detection', pos=(10, 310))

        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

    def OnClose(self, e):
        parameterlist = []
        classlist = []
        classlist.append(self.basicTextt.GetValue().split(","))

        parameterlist.append(anomalyDetection)  # anomalyDetection
        parameterlist.append(emotionDetection)  # emotionDetection
        parameterlist.append(countcrowd)  # countcrowd
        parameterlist.append(sensitiveArea)  # calculateSpeed
        parameterlist.append(humanTracking)  # humanTracking
        parameterlist.append(weaponDetection)  # weaponDetection
        parameterlist.append(classlist)

        stateVal = self.rbox.GetSelection()
        print(classlist)
        global videoSource
        if stateVal == 2:
            videoSource = self.basicText.GetValue()
            print(videoSource)
        parameterlist.append(videoSource)
        with open('settings.data', 'wb') as filehandle:
            pickle.dump(parameterlist, filehandle)
        self.Close()

    def SetVal(self, event):
        state1 = self.rbox.GetSelection()
        global videoSource
        if state1 == 0:
            videoSource = 0
            print(videoSource)
        elif state1 == 1:
            videoSource = 1
            print(videoSource)


def main():
    myapp = wx.App()
    App(None, title='Crowd Behaviour Analysis')
    myapp.MainLoop()


main()
