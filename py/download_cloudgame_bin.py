

import sys

def get_commandline_version():
    return '136'


DICT_KEY_PATH = "path"
DICT_KEY_FILENAME = "filename"


def get_bins_param(version):
    PREFIX = "/build_archive/"
    SUFFIX = ".7z"
    NAME_PART = "win32.release.crservice_1.0.0."

    urls = []
    for middle in [("dist",""), ("pdb","pdb.")]:
        item = {
            DICT_KEY_PATH: f"{PREFIX}{middle[0]}",
            DICT_KEY_FILENAME: f"{middle[1]}{NAME_PART}{version}{SUFFIX}"
        }
        urls.append(item)
    return urls



def ftp_download(params, local_path):
    from ftplib import FTP

    HOST = "47.106.161.48"
    
    ftp = FTP(HOST)
    ftp.login()

    for param in params:
        ftp.cwd(param[DICT_KEY_PATH])
        filename = param[DICT_KEY_FILENAME]
        handle = open(f"{local_path}\\{filename}", "wb")
        ftp.retrbinary(f"RETR {filename}", handle.write)
        handle.close()
        print(f"download {filename} success")


def main():
    version = get_commandline_version()

    TEMP_PATH = r"E:\dump\temp"

    bins_url = get_bins_param(version)
    ftp_download(bins_url,TEMP_PATH)

if __name__ == "__main__":
    main()