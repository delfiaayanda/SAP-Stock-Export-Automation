import win32com.client

sap = win32com.client.GetObject("SAPGUI")
application = sap.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

tab = "/app/con[0]/ses[0]/wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpDIS_LIST"

session.findById(tab).select()

print("List display selected")

for child in session.findById(
"/app/con[0]/ses[0]/wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpDIS_LIST"
).Children:
    print(child.Id, child.Type)