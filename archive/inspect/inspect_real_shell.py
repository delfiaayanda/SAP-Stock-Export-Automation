import win32com.client
import time

SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

paths = [
"/app/con[0]/ses[0]/wnd[0]/usr/cntlMATTREE1/shellcont/shell/shellcont[1]/shell[0]",
"/app/con[0]/ses[0]/wnd[0]/usr/cntlMATTREE1/shellcont/shell/shellcont[1]/shell[1]"
]

for p in paths:
    try:
        shell = session.findById(p)
        print("FOUND:", p)
        print("TYPE:", shell.Type)
        print("ROWS:", shell.RowCount)
        print("COLS:", shell.ColumnCount)

    except Exception as e:
        print("FAILED:", p)
        print(e)