import win32com.client
import time

sap = win32com.client.GetObject("SAPGUI")
application = sap.GetScriptingEngine

connection = application.Children(0)
session = connection.Children(0)

print("TITLE:", session.findById("wnd[0]").Text)


def scan(obj, level=0):
    try:
        count = obj.Children.Count
    except:
        return

    for i in range(count):
        try:
            child = obj.Children(i)

            print(
                " " * level,
                i,
                child.Id,
                "|",
                child.Type
            )

            scan(child, level+2)

        except Exception as e:
            pass


root = session.findById("wnd[0]/usr")

scan(root)