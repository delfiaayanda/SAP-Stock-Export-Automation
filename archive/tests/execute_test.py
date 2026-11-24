import win32com.client
import time

sap = win32com.client.GetObject("SAPGUI")
application = sap.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

session.findById("wnd[0]/tbar[1]/btn[8]").press()

time.sleep(5)

print("Title:", session.findById("wnd[0]").text)