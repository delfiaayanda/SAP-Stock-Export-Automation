import win32com.client

sap_gui = win32com.client.GetObject("SAPGUI")
app = sap_gui.GetScriptingEngine

connection = app.Children(0)
session = connection.Children(0)

usr = session.findById("wnd[0]/usr")

for child in usr.Children:
    if "Button" in child.Type:
        print("BUTTON:", child.Id, "|", child.text)