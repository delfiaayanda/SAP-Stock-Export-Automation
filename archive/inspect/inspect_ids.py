import win32com.client

SapGuiAuto = win32com.client.GetObject("SAPGUI")
app = SapGuiAuto.GetScriptingEngine

session = app.Children(0).Children(0)

print("Window:", session.findById("wnd[0]").Text)
print()

usr = session.findById("wnd[0]/usr")

print("Children:", usr.Children.Count)
print()

for i in range(usr.Children.Count):
    child = usr.Children(i)

    print(f"{i}")
    print("ID   :", child.Id)
    print("Type :", child.Type)
    print("Name :", child.Name)
    print("Text :", getattr(child, "Text", ""))
    print("-" * 50)