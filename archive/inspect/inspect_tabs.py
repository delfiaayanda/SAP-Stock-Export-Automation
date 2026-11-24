import win32com.client


SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)


tabs = session.findById(
"/app/con[0]/ses[0]/wnd[0]/usr/tabsTABSTRIP_SEL_DISP"
)

print("Jumlah tab:", tabs.Children.Count)

for i in range(tabs.Children.Count):
    try:
        child = tabs.Children(i)
        print(i, child.Id, child.Text)
    except:
        pass