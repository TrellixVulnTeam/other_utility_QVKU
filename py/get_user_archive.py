import argparse
import os
import http_util
import time


ARCHIVE_DOWNLOADED_URL = "http://cloudgame-biz.huya.com/get_game_archive/{uid}/{game_id}/"

LOCAL_SAVE = r"E:\py_temp"




def parser_commandline():
    parser = argparse.ArgumentParser(description="get user last archive of gameid")
    parser.add_argument('uid')
    parser.add_argument('game_id')
    return parser.parse_args()

def main():
    args = parser_commandline()
    download_url = ARCHIVE_DOWNLOADED_URL.format(uid = args.uid, game_id = args.game_id)

    #download_url = ARCHIVE_DOWNLOADED_URL.format(uid = '1199543338096', game_id = 'zzglm')
    result = http_util.request_get_json(download_url)
    if result['rs'] == 0:
        size = result['archive_size'] / 1024
        print(f"{result['uid']} size :{size} MB")

        url = result['download_url']
        filepath = os.path.join(LOCAL_SAVE, result['key'])

        now = time.time()
        http_util.download_file_from_url(filepath,url)
        used_time = time.time() - now
        print(f"download {filepath} success, use {used_time} seconds")

    else :
        print(result)


if __name__ == '__main__':
    main()