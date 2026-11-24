import win32com.client

sap = win32com.client.GetObject("SAPGUI")
app = sap.GetScriptingEngine
conn = app.Children(0)
session = conn.Children(0)

shell = session.findById(
"/app/con[0]/ses[0]/wnd[0]/usr/cntlMATTREE1/shellcont/shell"
)

print("Type:", shell.Type)

print("Methods:")
print(dir(shell))