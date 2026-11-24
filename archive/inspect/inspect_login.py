from pywinauto import Desktop

desktop = Desktop(backend="uia")

for window in desktop.windows():
    title = window.window_text()

    if "SAP GUI for Windows" in title:
        print("=" * 80)
        print(title)
        print("=" * 80)

        try:
            window.print_control_identifiers()
        except Exception as e:
            print(e)