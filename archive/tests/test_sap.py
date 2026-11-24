import win32com.client

try:
    sap_gui = win32com.client.GetObject("SAPGUI")
    app = sap_gui.GetScriptingEngine

    print("✅ SAP GUI terhubung")
    print("Jumlah koneksi:", app.Children.Count)

except Exception as e:
    print("❌ Gagal konek SAP")
    print(e)