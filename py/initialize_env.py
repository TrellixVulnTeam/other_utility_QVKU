
GAME_DATA_DIR r"D:\game_data"
GAME_HOST_CONF = GAME_DATA_DIR + r"\game_host.conf"

import multiprocessing
import platform
import psutil

def task_hardware_config():
    cpu_count = multiprocessing.cpu_count()
    os_version = platform.win32_edition()+platform.version()
    ram_size = round(psutil.virtual_memory().total/1024/1024/1024)
    hardware = f"CPU{cpu_count} RAM{ram_size}GB"
    



def main():


if __name__ == '__main__':
    main()