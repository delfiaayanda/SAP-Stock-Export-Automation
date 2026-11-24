import win32com.client

SapGuiAuto = win32com.client.GetObject("SAPGUI")
app = SapGuiAuto.GetScriptingEngine

print("Connections:", app.Children.Count)

conn = app.Children(0)
print("Sessions:", conn.Children.Count)

try:
    session = conn.Children(0)
    print("Session object exists!")

    print("Window:", session.findById("wnd[0]").Text)

except Exception as e:
    print(type(e).__name__)
    print(e)