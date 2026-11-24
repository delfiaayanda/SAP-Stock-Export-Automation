import subprocess
import time
import keyring
import win32com.client
import pywintypes

CREDENTIAL_NAME = "SAP_ERAJAYA_PS4"
SAP_USERNAME = "DYANDA"

SAP_LOGON_PATH = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"

CONNECTION_NAME = "ERA - PRD S4HANA via Internet NEW"

SAP_COM_TIMEOUT_SECONDS = 45
SAP_COM_RETRY_SECONDS = 1


def get_sap_scripting_engine():
    """Wait for SAP Logon to publish its scripting engine to COM."""
    deadline = time.monotonic() + SAP_COM_TIMEOUT_SECONDS
    last_error = None

    while time.monotonic() < deadline:
        try:
            sap_gui_auto = win32com.client.GetObject("SAPGUI")
            application = sap_gui_auto.GetScriptingEngine
            if application is not None:
                return application
        except pywintypes.com_error as error:
            # SAP Logon registers this COM object only after it has finished
            # starting. While that is in progress, GetObject can return
            # "Invalid syntax" instead of a more useful "not found" error.
            last_error = error

        time.sleep(SAP_COM_RETRY_SECONDS)

    raise RuntimeError(
        "SAP GUI Scripting tidak tersedia setelah 45 detik. Pastikan SAP Logon "
        "sudah terbuka dan SAP GUI Scripting diaktifkan di SAP client/server."
    ) from last_error


def login_sap():

    print("Opening SAP Logon...")

    subprocess.Popen(SAP_LOGON_PATH)

    # Windows Credential Manager stores one generic credential as:
    # target name = service, user name = account, password = secret.
    password = keyring.get_password(CREDENTIAL_NAME, SAP_USERNAME)
    username = SAP_USERNAME

    if not username or not password:
        raise Exception(
            f"Credential '{CREDENTIAL_NAME}' untuk user '{SAP_USERNAME}' "
            "tidak ditemukan di Windows Credential Manager."
        )

    print("Connecting to SAP GUI COM...")

    application = get_sap_scripting_engine()

    print("Opening SAP Connection...")

    application.OpenConnection(CONNECTION_NAME, True)

    #
    # Wait until SAP creates the session
    #
    timeout = time.time() + 30

    while application.Children.Count == 0:
        if time.time() > timeout:
            raise TimeoutError("SAP connection was not created.")
        time.sleep(0.5)

    connection = application.Children(0)

    while connection.Children.Count == 0:
        if time.time() > timeout:
            raise TimeoutError("SAP session was not created.")
        time.sleep(0.5)

    session = connection.Children(0)

    print("Entering username/password...")

    session.findById(
        "wnd[0]/usr/txtRSYST-BNAME"
    ).text = username

    session.findById(
        "wnd[0]/usr/pwdRSYST-BCODE"
    ).text = password

    print("Logging in...")

    session.findById("wnd[0]").sendVKey(0)

    print("Waiting for SAP Easy Access...")

    #
    # Wait until login screen disappears
    #
    timeout = time.time() + 30

    while True:

        title = session.findById("wnd[0]").Text

        if "SAP Easy Access" in title:
            break

        if time.time() > timeout:
            raise TimeoutError("Login timeout.")

        time.sleep(0.5)

    print("Login Success.")
