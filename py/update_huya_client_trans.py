import shutil
import http_util
import sys
from base import archive_util 
import dir_util
import pdb
import argparse
import os
import codecs
import pathlib

def main(dest_dir, url, is_pc_sdk):
    if not url.endswith("/"):
        url = url+"/"

    print('dst: ',dest_dir)
    print('src: ', url)

    CURRENT_DIR = dir_util.change_workdir_to_temp()

    PDB = "pdb.tar.gz"
    BIN = "bin.tar.gz"
    DEV = "dev.tar.gz"
    tar_files = [PDB, BIN, DEV]
    for item in tar_files:
        http_util.download_file_from_url(item, url+item)
        archive_util.extract_tar_to(".", item)
        print("success download & extract ",item )

    utf8_to_gb2312()

    if is_pc_sdk:
        src = os.path.join(CURRENT_DIR,r"bin\x86\release")
        dst = os.path.join(dest_dir,r"bin\Player\huyasdk")
        shutil.copytree(src, dst,dirs_exist_ok=True)
        print("copy bin files to: ", dst)

        src = os.path.join(CURRENT_DIR,r"include")
        dst = os.path.join(dest_dir,r"huyaplayerhelper\huyasdk")
        shutil.copytree(src, dst,dirs_exist_ok=True)
        print("copy include files to: ", dst)
        return 

    COPY_DIR = ["pdb","lib",r"bin\x86","include"]

    #dest_dir = r"E:\test"
    for folder in COPY_DIR:
        src = os.path.join(CURRENT_DIR,folder)
        last_name = os.path.basename(src)
        dst = os.path.join(dest_dir,last_name)
        shutil.copytree(src,dst ,dirs_exist_ok=True)
        print(f"copy {folder} files to: {dst}" )
        

def get_convert_file_path(dest_dir):
    ret = []
    record = os.path.join(dest_dir, "change_encode.txt")
    with open(record,"rt") as read_file:
        for line in read_file.readlines():
            ret.append(line.strip())
    return ret

def utf8_to_gb2312():
    dest_dir = pathlib.Path(__file__).parent.absolute()
    target_files = get_convert_file_path(dest_dir)
    for item in target_files:
        one_file = os.path.join(".","include",item)
        resave_to_gb2312(one_file)


BOM_STR = str(codecs.BOM_UTF8,'utf8')
def resave_to_gb2312(one_file):
    with open(one_file,'r',encoding='utf8') as f:
        text = f.read()

        if text.startswith(BOM_STR):
            text = text[len(BOM_STR):]
    
    with open(one_file,"w",encoding="gb2312") as f:
        f.write(text)

    print(f"resave {one_file} from utf8 to GB2312 ")


def get_work_dir(workspace_index):
    if workspace_index == '2':
        return r"E:\huyadev\dev2\crservice\thirdparty\huya-client-trans"
    elif workspace_index == '1':
        return r"E:\huyadev\crservice\thirdparty\huya-client-trans"
    elif workspace_index == 'pc':
        return r"E:\huyadev\huya-cloudgame-pc\source"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="update audio/video push sdk")
    parser.add_argument('-w','--workspace',required=True)
    parser.add_argument('url')
    args = parser.parse_args()

    dir = get_work_dir(args.workspace)
    if dir:
        main(dir, args.url, args.workspace == 'pc')
    else:
        print("ERROR: unknown workspace")


