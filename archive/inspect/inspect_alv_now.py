import win32com.client

SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)


def walk(obj, level=0):
    try:
        print(
            " " * level,
            obj.Id,
            "|",
            obj.Type
        )
    except:
        pass

    try:
        for i in range(obj.Children.Count):
            walk(obj.Children(i), level + 2)
    except:
        pass


print("TITLE:", session.findById("wnd[0]/titl").Text)

walk(session.findById("wnd[0]/usr"))