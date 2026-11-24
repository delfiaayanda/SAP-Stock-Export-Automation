from sap import connect
import time
import os
from datetime import datetime


# ==========================================================
# DIRECTORY
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORT_DIR = os.path.join(BASE_DIR, "Hasil Export")


# ==========================================================
# HELPER
# ==========================================================

def wait_sap(session):
    while session.Busy:
        time.sleep(0.2)


# ==========================================================
# OPEN TRANSACTION
# ==========================================================

def open_transaction():

    session = connect()

    print("Opening ZRWBE...")

    session.findById("wnd[0]/tbar[0]/okcd").text = "/nZRWBE"
    session.findById("wnd[0]").sendVKey(0)

    wait_sap(session)

    print("ZRWBE opened.")

    return session


# ==========================================================
# MAIN FLOW
# ==========================================================

def fill_parameters(session):

    print("Filling Plant...")

    session.findById(
        "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpSEL_CRI/"
        "ssub%_SUBSCREEN_SEL_DISP:ZRWBEST01:1010/"
        "ctxtS_WERKS-LOW"
    ).text = "*"

    print("Plant Filled.")

    fill_storage_location(session)
    fill_material(session)
    execute_report(session)
    export_excel(session)


# ==========================================================
# STORAGE LOCATION
# ==========================================================

def fill_storage_location(session):

    print("Opening Storage Location popup...")

    session.findById(
        "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpSEL_CRI/"
        "ssub%_SUBSCREEN_SEL_DISP:ZRWBEST01:1010/"
        "btn%_S_LGORT_%_APP_%-VALU_PUSH"
    ).press()

    wait_sap(session)

    print("Importing storage_locations.txt...")

    session.findById(
        "wnd[1]/tbar[0]/btn[23]"
    ).press()

    wait_sap(session)

    session.findById(
        "wnd[2]/usr/ctxtDY_PATH"
    ).text = DATA_DIR

    session.findById(
        "wnd[2]/usr/ctxtDY_FILENAME"
    ).text = "storage_locations.txt"

    session.findById(
        "wnd[2]/tbar[0]/btn[0]"
    ).press()

    wait_sap(session)

    try:
        session.findById(
            "wnd[2]/usr/btnSPOP-OPTION1"
        ).press()

        wait_sap(session)

    except:
        pass

    session.findById(
        "wnd[1]/tbar[0]/btn[8]"
    ).press()

    wait_sap(session)

    print("Storage Location Imported.")


# ==========================================================
# MATERIAL
# ==========================================================

def fill_material(session):

    print("Opening Material popup...")

    session.findById(
        "wnd[0]/usr/btn%_S_MATNR_%_APP_%-VALU_PUSH"
    ).press()

    wait_sap(session)

    print("Importing materials.txt...")

    session.findById(
        "wnd[1]/tbar[0]/btn[23]"
    ).press()

    wait_sap(session)

    session.findById(
        "wnd[2]/usr/ctxtDY_PATH"
    ).text = DATA_DIR

    session.findById(
        "wnd[2]/usr/ctxtDY_FILENAME"
    ).text = "materials.txt"

    session.findById(
        "wnd[2]/tbar[0]/btn[0]"
    ).press()

    wait_sap(session)

    try:
        session.findById(
            "wnd[2]/usr/btnSPOP-OPTION1"
        ).press()

        wait_sap(session)

    except:
        pass

    session.findById(
        "wnd[1]/tbar[0]/btn[8]"
    ).press()

    wait_sap(session)

    print("Material Imported.")


# ==========================================================
# EXECUTE REPORT
# ==========================================================

def execute_report(session):

    print("Preparing Report...")

    session.findById(
        "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpSEL_CRI/"
        "ssub%_SUBSCREEN_SEL_DISP:ZRWBEST01:1010/"
        "chkP_KZLSO"
    ).selected = True

    session.findById(
        "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpSEL_CRI/"
        "ssub%_SUBSCREEN_SEL_DISP:ZRWBEST01:1010/"
        "chkP_KZLON"
    ).selected = True

    session.findById(
        "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpDIS_LIST"
    ).select()

    session.findById(
        "wnd[0]/usr/tabsTABSTRIP_SEL_DISP/tabpDIS_LIST/"
        "ssub%_SUBSCREEN_SEL_DISP:ZRWBEST01:1020/"
        "radP_KZALV"
    ).select()

    print("Executing Report...")

    session.findById(
        "wnd[0]/tbar[1]/btn[8]"
    ).press()

    wait_sap(session)

    print("Report Finished.")


# ==========================================================
# EXPORT EXCEL
# ==========================================================

def export_excel(session):

    print("Exporting Excel...")

    shell = session.findById(
        "wnd[0]/usr/cntlMATTREE/shellcont/shell"
    )

    shell.pressToolbarContextButton("&MB_EXPORT")
    shell.selectContextMenuItem("&XXL")

    wait_sap(session)

    today = datetime.now().strftime("%Y-%m-%d")

    export_folder = os.path.join(
        EXPORT_DIR,
        today
    )

    os.makedirs(export_folder, exist_ok=True)

    filename = f"Stock_Report_{datetime.now():%Y%m%d_%H%M%S}.xlsx"


    session.findById(
        "wnd[1]/usr/ctxtDY_PATH"
    ).text = export_folder


    session.findById(
        "wnd[1]/usr/ctxtDY_FILENAME"
    ).text = filename


    session.findById(
        "wnd[1]/tbar[0]/btn[0]"
    ).press()


    wait_sap(session)
    time.sleep(1)


    try:
        session.findById(
            "wnd[1]/tbar[0]/btn[0]"
        ).press()

    except:
        pass


    saved_file = os.path.join(
        export_folder,
        filename
    )


    if os.path.exists(saved_file):

        print("\n===================================")
        print("Export Success!")
        print(f"Saved To : {saved_file}")
        print("===================================\n")

    else:

        print("\n===================================")
        print("WARNING : File belum ditemukan.")
        print("===================================\n")