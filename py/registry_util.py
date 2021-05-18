
import winreg


def registry_HKLM_string(path, value_name, value):
    reg_item = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, path ,0, winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)
    winreg.SetValueEx(reg_item, value_name, 0, winreg.REG_SZ, value)
    winreg.CloseKey(reg_item)
    print("change registry to", value)