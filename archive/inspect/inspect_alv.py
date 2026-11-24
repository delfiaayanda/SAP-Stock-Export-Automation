import win32com.client

sap = win32com.client.GetObject("SAPGUI")
app = sap.GetScriptingEngine

conn = app.Children(0)
session = conn.Children(0)

print("TITLE:", session.findById("wnd[0]").Text)

def scan(obj, level=0):
    try:
        for i in range(obj.Children.Count):
            child = obj.Children(i)
            print(" "*level + child.Id, "|", child.Type, "|", getattr(child,"Name",""))
            scan(child, level+2)
    except:
        pass

scan(session.findById("wnd[0]"))