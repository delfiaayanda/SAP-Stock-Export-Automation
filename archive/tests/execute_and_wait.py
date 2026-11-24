import time
import win32com.client

SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

# execute
session.findById(
    "wnd[0]/tbar[1]/btn[8]"
).press()

print("Execute pressed")

# tunggu
for i in range(20):
    time.sleep(1)
    title = session.findById("wnd[0]/titl").Text
    print(i, title)

    if "Full List" in title:
        print("ALV FOUND")
        break