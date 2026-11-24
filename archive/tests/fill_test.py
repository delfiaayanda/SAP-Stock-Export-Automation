import win32com.client
import time

sap = win32com.client.GetObject("SAPGUI")
application = sap.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

# material
session.findById(
    "wnd[0]/usr/ctxtS_MATNR-LOW"
).text = "8100228762"

# plant
session.findById(
    "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpSEL_CRI/ssub%_SUBSCREEN_SEL_DISP:ZRWBEST01:1010/ctxtS_WERKS-LOW"
).text = "BIC1"

# storage location
session.findById(
    "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpSEL_CRI/ssub%_SUBSCREEN_SEL_DISP:ZRWBEST01:1010/ctxtS_LGORT-LOW"
).text = "1005"


print("Filter masuk")

time.sleep(2)