import win32com.client

sap_gui = win32com.client.GetObject("SAPGUI")
app = sap_gui.GetScriptingEngine

connection = app.Children(0)
session = connection.Children(0)

print("WINDOW:", session.findById("wnd[0]").text)

toolbar = session.findById("wnd[0]/tbar[1]")

for child in toolbar.Children:
    print(child.Id, "|", child.Type, "|", child.text)