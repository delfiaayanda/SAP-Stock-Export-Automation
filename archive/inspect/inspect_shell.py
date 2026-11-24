import win32com.client
import time

SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

shell = session.findById(
    "wnd[0]/usr/cntlMATTREE1/shellcont/shell"
)

print("TYPE:", shell.Type)

print("ROWS:", shell.RowCount)

print("COLUMNS:")

for i in range(shell.ColumnCount):
    try:
        print(
            i,
            shell.GetColumnTitle(i)
        )
    except:
        pass