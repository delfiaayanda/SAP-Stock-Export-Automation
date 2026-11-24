import win32com.client

sap_gui = win32com.client.GetObject("SAPGUI")
app = sap_gui.GetScriptingEngine

connection = app.Children(0)
session = connection.Children(0)

print("Screen:", session.findById("wnd[0]").text)

try:
    main = session.findById("wnd[0]/usr")
    
    print("Jumlah object:", main.Children.Count)

    for child in main.Children:
        print(child.Id, "|", child.Type)

except Exception as e:
    print("Error:", e)