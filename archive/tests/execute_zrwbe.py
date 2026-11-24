import win32com.client
import time

sap_gui = win32com.client.GetObject("SAPGUI")
app = sap_gui.GetScriptingEngine

connection = app.Children(0)
session = connection.Children(0)

print("Current screen:", session.findById("wnd[0]").text)

# Klik Execute / F8
session.findById("wnd[0]/tbar[1]/btn[8]").press()

time.sleep(5)

print("Execute selesai")
print("New screen:", session.findById("wnd[0]").text)