import win32com.client

SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)


paths = [
"/app/con[0]/ses[0]/wnd[0]/usr/cntlMATTREE1/shellcont/shell/shellcont[1]/shell[0]",
"/app/con[0]/ses[0]/wnd[0]/usr/cntlMATTREE1/shellcont/shell/shellcont[1]/shell[1]"
]


for path in paths:
    print("\nTEST:", path)

    try:
        obj = session.findById(path)

        print("TYPE:", obj.Type)

        print("Methods:")
        for m in [
            "RowCount",
            "ColumnCount",
            "GetCellValue",
            "GetColumnNames",
            "SelectedRows",
            "GetHierarchy",
            "PressToolbarButton"
        ]:
            try:
                print(m, "=", getattr(obj,m))
            except:
                pass

    except Exception as e:
        print("ERROR", e)