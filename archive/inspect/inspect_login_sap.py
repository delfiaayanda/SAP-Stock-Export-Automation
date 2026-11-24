from pywinauto import Application

app = Application(backend="win32").connect(
    title_re="SAP GUI for Windows.*"
)

dlg = app.top_window()

print("Window title:", dlg.window_text())
print(type(dlg))

dlg.print_control_identifiers()