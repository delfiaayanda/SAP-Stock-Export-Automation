import time
import win32com.client

# ======================================
# CONNECT SAP
# ======================================

SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

# ======================================
# LOAD FILE
# ======================================

with open("materials.txt", "r") as f:
    materials = [line.strip() for line in f if line.strip()]

with open("storage_locations.txt", "r") as f:
    storage_locations = [line.strip() for line in f if line.strip()]

plant = "*"

print(f"Material Loaded : {len(materials)}")
print(f"Storage Loaded  : {len(storage_locations)}")

# ======================================
# 1. PLANT
# ======================================

session.findById(
    "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpSEL_CRI/"
    "ssub%_SUBSCREEN_SEL_DISP:ZRWBEST01:1010/"
    "ctxtS_WERKS-LOW"
).text = plant

# ======================================
# 2. STORAGE LOCATION
# ======================================

session.findById(
    "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpSEL_CRI/"
    "ssub%_SUBSCREEN_SEL_DISP:ZRWBEST01:1010/"
    "btn%_S_LGORT_%_APP_%-VALU_PUSH"
).press()

time.sleep(0.5)

for i, loc in enumerate(storage_locations):
    session.findById(
        f"wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/"
        f"ssubSCREEN_HEADER:SAPLALDB:3010/"
        f"tblSAPLALDBSINGLE/"
        f"ctxtRSCSEL_255-SLOW_I[1,{i}]"
    ).text = loc

session.findById("wnd[1]/tbar[0]/btn[8]").press()

time.sleep(0.5)

# ======================================
# 3. MATERIAL
# ======================================

session.findById(
    "wnd[0]/usr/btn%_S_MATNR_%_APP_%-VALU_PUSH"
).press()

time.sleep(0.5)

print("Material popup opened")

# STOP DULU DI SINI
input("Tekan ENTER setelah popup Material muncul...")

print("Done")