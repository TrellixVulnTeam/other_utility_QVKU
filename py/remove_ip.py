import os

def is_ip_str(s):
    import ipaddress
    try:
        ipaddress.ip_address(s)
    except Exception:
        return False
    return True

def get_ip_from_file(filename):
    ips = []
    with open(filename, "rt") as fd:
        for line in fd:
            ip = line.strip()
            if is_ip_str(ip):
                ips.append(ip)
    return ips

def get_all_offline_host(filenames):
    hosts = []
    for i in filenames:
        hosts += get_ip_from_file(i)

    print(f"{len(hosts)} ip will remove")
    return hosts


def remove_ip_in_file(file,ips):
    with open(file,"r+t") as fd:
        data = fd.read()
        for ip in ips:
            data = data.replace(ip,'')
        fd.seek(0)
        fd.write(data)
        fd.truncate()

def main():
    WORK_DIR = "E:\\huyadev\\ansible\\"
    os.chdir(WORK_DIR)

    OFFLINE_TXT = ['offline\\multi_offline.txt']

    OLD_TXT = get_old_files()

    offline_hosts = get_all_offline_host(OFFLINE_TXT)

    print("find ip in", OLD_TXT)

    for file in OLD_TXT:
        remove_ip_in_file(file, offline_hosts)


def get_ini_under(dir):
    files = []
    for f in os.listdir(dir):
        target = os.path.join(dir,f)
        if not os.path.isdir(target):
            if f.endswith(".ini"):
                files.append(target)
    return files
def get_old_files():
    files = get_ini_under(".")
    files += get_ini_under("hosts")
    return files


if __name__ == "__main__":

    main()