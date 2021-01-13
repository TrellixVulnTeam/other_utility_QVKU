import sys
import os
import shutil

def clean_dir(dir):
    for f in os.listdir(dir):
        target = os.path.join(dir,f)
        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)


def change_workdir_to_temp():
    WORK_DIR = "E:\\py_temp"

    if not os.path.isdir(WORK_DIR):
        os.mkdir(WORK_DIR)
    else:
        clean_dir(WORK_DIR)

    os.chdir(WORK_DIR)