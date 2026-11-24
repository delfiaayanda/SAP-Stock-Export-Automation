import win32com.client

SapGui = win32com.client.GetObject("SAPGUI")
app = SapGui.GetScriptingEngine
conn = app.Children(0)
session = conn.Children(0)

def walk(obj, level=0):
    try:
        print(" " * level + obj.Id + " | " + obj.Type)
        for i in range(obj.Children.Count):
            walk(obj.Children(i), level + 2)
    except:
        pass

print("WINDOWS:", session.Children.Count)

for i in range(session.Children.Count):
    wnd = session.Children(i)
    print("\n" + "=" * 50)
    print(f"WINDOW {i}: {wnd.Text}")
    walk(wnd)