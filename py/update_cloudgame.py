
import sys
import psutil
import os
import shutil
import winreg
import time


HOST_SREVICE = "host_service.exe"
ARCHIVE_PREFIX = "win32.release.crservice_"
TOOLS_7Z = r"D:\tools\7z.exe"
TOOLS_PSEXEC = r"D:\tools\PsExec.exe"
VERSION_FILE = "D:\\game_data\\version.txt"

def main():
    ON_DEBUG = 0
    if ON_DEBUG:
        version = "1.0.0.199"
        password = "asdf"
    else:
        version = sys.argv[2]
        password = sys.argv[1]

    same_version = is_same_version(version)

    if not same_version:
        insure_tools()
        download_bin(version)
        write_registry(version)
        update_version_file(version)
        launch_if_not_exist(version, password)
    else:
        print("same version")



def is_same_version(version):
    running_process = get_running_process(HOST_SREVICE)
    if running_process and version in running_process:
        return True
    else:
        return False

def get_running_process(process_name):
    for proc in psutil.process_iter(['name','exe']):
        if process_name == proc.info['name']:
            return proc.info['exe']
    return ''

def insure_tools():
    #for item in ['']
    #insure_file()
    pass

def download_bin(version):
    upper_dir = "D:\\" + ARCHIVE_PREFIX + version
    if os.path.exists(upper_dir):
        if os.path.isdir(upper_dir):
            shutil.rmtree(upper_dir,ignore_errors=True)
        else:
            os.remove(upper_dir)

    os.mkdir(upper_dir)

    param = get_ftp_param(version)
    results = ftp_download([param], upper_dir)

    #解压
    cmd = f"{TOOLS_7Z} x {results[0]} -o{upper_dir}" 
    print(cmd)
    os.system(cmd)



def write_registry(version):
    value =  version
    reg_item = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\CloudGame" ,0, winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)
    winreg.SetValueEx(reg_item, "VersionString", 0, winreg.REG_SZ, value)
    winreg.CloseKey(reg_item)
    print("change registry to", value)

def update_version_file(version):
    i = 0
    while i < 3:
        with open(VERSION_FILE, "wt") as fd:
            fd.write(version)
        time.sleep(0.04)
        with open(VERSION_FILE, "rt") as read_fd:
            writed_version = read_fd.read()
            print("write to version file",writed_version)
            if version == writed_version:
                return
        i = i + 1
    raise ValueError("update version failed")



def launch_if_not_exist(version, password):
    running_process = get_running_process(HOST_SREVICE)
    if running_process == '':
        middle = ARCHIVE_PREFIX + version
        fullpath = f"D:\\{middle}\\{middle}\\{HOST_SREVICE}"
        cmd = f"{TOOLS_PSEXEC} -accepteula -h -i 1 -d -u cloudgame1 -p {password} {fullpath}" 
        print(cmd)
        os.system(cmd)




DICT_KEY_PATH = "path"
DICT_KEY_FILENAME = "filename"




def get_ftp_param(version):
    PATH = "/build_archive/dist"
    SUFFIX = ".7z"
    item = {
        DICT_KEY_PATH: PATH,
        DICT_KEY_FILENAME: ARCHIVE_PREFIX+version+SUFFIX
    }
    return item



def ftp_download(params, local_path):
    from ftplib import FTP

    HOST = "47.106.161.48"
    
    ftp = FTP(HOST)
    ftp.login()

    return_files = []

    for param in params:
        ftp.cwd(param[DICT_KEY_PATH])
        filename = param[DICT_KEY_FILENAME]
        full_filepath = f"{local_path}\\{filename}"
        handle = open(full_filepath, "wb")
        ftp.retrbinary(f"RETR {filename}", handle.write)
        handle.close()
        print(f"download {filename} success")
        return_files.append(full_filepath)

    return return_files


if __name__ == "__main__":
    main()