import win32com.client
import time

sap_gui = win32com.client.GetObject("SAPGUI")
app = sap_gui.GetScriptingEngine

connection = app.Children(0)
session = connection.Children(0)

print("SAP title:", session.findById("wnd[0]").text)

session.findById("wnd[0]/tbar[0]/okcd").text = "/nZRWBE"
session.findById("wnd[0]").sendVKey(0)

time.sleep(3)

print("Transaksi berhasil dijalankan")