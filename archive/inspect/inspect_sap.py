import win32com.client

sap_gui = win32com.client.GetObject("SAPGUI")
app = sap_gui.GetScriptingEngine

connection = app.Children(0)
session = connection.Children(0)

print("Screen:", session.findById("wnd[0]").text)

for child in session.findById("wnd[0]/usr").Children:
    print(child.Id, child.Type)