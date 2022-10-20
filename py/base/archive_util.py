import tarfile

def extract_tar_to(dest, src):
    with tarfile.open(src, mode='r:*') as tar_file:
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar_file, path=dest)




if __name__ == '__main__':
    DEST = r"E:\py_temp"
    SRC = r"E:\py_temp\pdb.tar.gz"
    extract_tar_to(DEST,SRC)