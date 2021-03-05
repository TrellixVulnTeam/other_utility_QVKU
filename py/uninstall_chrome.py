import os
import sys
import re

def get_re_subdir(main_dir, re_express):
    subdir = []
    for f in os.listdir(main_dir):
        target = os.path.join(main_dir,f)
        if os.path.isdir(target):
            pattern = re.compile(re_express)
            match_ret = pattern.fullmatch(f)
            if match_ret:
                subdir.append(target)
    return subdir

def get_setup_exe():
    MAIN_DIR = r"C:\Program Files (x86)\Google\Chrome\Application"
    #MAIN_DIR = r"C:\Program Files\Google\Chrome\Application"
    INSTALLER = "Installer"
    EXE = "setup.exe"
    if not os.path.isdir(MAIN_DIR):
        return []

    version_subdirs = get_re_subdir(MAIN_DIR, r"[\d]{2}\.[\d]\.[\d]{4}\.[\d]*")
    return [os.path.join(MAIN_DIR,version_subdir,INSTALLER, EXE) for version_subdir in version_subdirs]

def run_uninstall_cmd(setup):
    if os.path.exists(setup):
        command = f"\"{setup}\" --uninstall --system-level --force-uninstall"
        print(command)
        os.system(command)
    else:
        print(f"{setup} not exists")

def task_uninstall_chrome():
    setup_exes = get_setup_exe()
    for setup_exe in setup_exes:
        run_uninstall_cmd(setup_exe)


if __name__ == "__main__":
    task_uninstall_chrome()