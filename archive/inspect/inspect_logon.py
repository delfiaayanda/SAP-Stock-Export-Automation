from pywinauto import Application

app = Application(backend="win32").connect(title_re=".*SAP Logon.*")

dlg = app.top_window()

dlg.print_control_identifiers()