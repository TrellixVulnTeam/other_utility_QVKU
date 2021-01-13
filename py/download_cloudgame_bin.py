

import sys
import shutil
import os

def get_commandline_version(version):
    return str(version)


DICT_KEY_PATH = "path"
DICT_KEY_FILENAME = "filename"

def directory_name(version, prefix):
    NAME_PART = "win32.release.crservice_1.0.0."
    return prefix+NAME_PART+version


def get_bins_param(version):
    PREFIX = "/build_archive/"
    SUFFIX = ".7z"
   

    urls = []
    for middle in [("dist",""), ("pdb","pdb.")]:
        item = {
            DICT_KEY_PATH: f"{PREFIX}{middle[0]}",
            DICT_KEY_FILENAME: f"{directory_name(version, middle[1])}{SUFFIX}"
        }
        urls.append(item)
    return urls



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

def unzip_files(paths,dest):
    UNZIP_EXE = r"C:\Users\Administrator\AppData\Local\SourceTree\app-3.3.9\tools\7z.exe"
    for path in paths:
        excute = f"{UNZIP_EXE} x -o{dest} {path}"
        os.system(excute)
        print(excute)
        
    
    

def move_files(location, version):
    src = location+'\\'+directory_name(version,"")
    dst = location+'\\'+directory_name(version,"pdb.")

    # all_files = os.listdir(src)
    # for file in all_files:
    #     try:
    #         shutil.move(os.path.join(src, file),dst)
    #     except Exception :
    #         pass
        
    shutil.copytree(src, dst, dirs_exist_ok = True)

    print("copy finished")
    shutil.rmtree(src)
    

def main(argv):
    version = get_commandline_version(argv[1])

    TEMP_PATH = r"E:\dump\temp"
    DESTINATION = r"E:\dump"

    bins_url = get_bins_param(version)
    file_paths = ftp_download(bins_url,TEMP_PATH)

    unzip_files(file_paths,DESTINATION)

    move_files(DESTINATION, version)


if __name__ == "__main__":
    main(sys.argv)