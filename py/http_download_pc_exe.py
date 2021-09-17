
import time
import http_util

def main():
    item = "D:\\foo.exe"
    url = "https://repo.huya.com/dwbuild/dwinternal/hycgpc/liuzhuzhai/20210601181354-459-rab68593b4da11b26a4b501b69dbc7d1a1cf6d86d/channel/HYCGClient.exe"


    before = time.time()
    http_util.download_file_from_url(item, url)

    print("use ", time.time() - before)



if __name__ == '__main__':
    main()