import tarfile

def extract_tar_to(dest, src):
    with tarfile.open(src, mode='r:*') as tar_file:
        tar_file.extractall(path = dest)




if __name__ == '__main__':
    DEST = r"E:\py_temp"
    SRC = r"E:\py_temp\pdb.tar.gz"
    extract_tar_to(DEST,SRC)