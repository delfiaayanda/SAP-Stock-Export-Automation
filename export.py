import time


def fill_parameter(session):
    print("Filling parameter...")

    session.findById(
        "wnd[0]/usr/btn%_S_MATNR_%_APP_%-VALU_PUSH"
    ).press()

    time.sleep(1)

    print("Material popup opened.")