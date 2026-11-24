import win32com.client

SapGuiAuto = win32com.client.GetObject("SAPGUI")
app = SapGuiAuto.GetScriptingEngine

print("Connections before:", app.Children.Count)

connection = app.OpenConnection(
    "ERA - PRD S4HANA via Internet NEW",
    True
)

print("OpenConnection() finished")

print("Connections after:", app.Children.Count)