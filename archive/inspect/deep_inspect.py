import win32com.client


SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)


def walk(element, level=0):

    try:
        print(
            " "*level,
            element.Id,
            "|",
            element.Type,
            "|",
            getattr(element, "Name", "")
        )

    except:
        pass


    try:
        children = element.Children

        for i in range(children.Count):
            walk(children(i), level+2)

    except:
        pass



tab = session.findById(
"/app/con[0]/ses[0]/wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpSEL_CRI"
)

walk(tab)