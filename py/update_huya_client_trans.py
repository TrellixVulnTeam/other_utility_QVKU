import http_util
import sys
from base import archive_util 
import dir_util
import pdb
import argparse
import os

def main(dir, url):
    if not url.endswith("/"):
        url = url+"/"

    MIDDLE_PATH = r"\thirdparty\huya-client-trans"
    dir = os.path.join(dir, MIDDLE_PATH)

    print(dir)
    print(url)

    dir_util.change_workdir_to_temp()

    PDB = "pdb.tar.gz"
    BIN = "bin.tar.gz"
    DEV = "dev.tar.gz"
    tar_files = [PDB, BIN, DEV]
    for item in tar_files:
        http_util.download_file_from_url(item, url+item)
        archive_util.extract_tar_to(".", item)
        print("success download & extract ",item )

    COPY_DIR = ["pdb","lib",r"bin\x86","include"]

    #for folder in COPY_DIR:
        
def get_work_dir(workspace_index):
    if workspace_index == '2':
        return r"E:\huyadev\dev2\crservice"
    elif workspace_index == '1':
        return r"E:\huyadev\crservice"
    elif workspace_index == 'pc':
        return r"E:\huyadev\huya-cloudgame-pc\source\bin\Player\huyasdk"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="update audio/video push sdk")
    parser.add_argument('-w','--workspace',required=True)
    parser.add_argument('url')
    args = parser.parse_args()

    dir = get_work_dir(args.workspace)
    if dir:
        main(dir, args.url)
    else:
        print("ERROR: unknown workspace")


