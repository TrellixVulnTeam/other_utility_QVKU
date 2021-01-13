import http_util
import sys
import download_cloudgame_bin
import dir_util

def main(argv):

    dir_util.change_workdir_to_temp()
    
    url = "https://repo.huya.com/dwbuild/dwinternal/huya-client-trans/banana_statistics_dev_full_support/20201230173406-101-r20c999c71fecab6ec1fe6c61d3d605c15c922490/"

    PDB = "pdb.tar.gz"
    BIN = "bin.tar.gz"
    tar_files = [PDB, BIN]
    for item in tar_files:
        http_util.download_file_from_url(item, url+item)

    download_cloudgame_bin.unzip_files(tar_files,".")


if __name__ == "__main__":
    main(sys.argv)