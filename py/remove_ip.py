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

def get_all_ip_from_files(filenames):
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
    OLD_TXT = get_old_files()

    find_duplicated = 0
    if find_duplicated:
        find_duplicated_ip(OLD_TXT)

    OFFLINE_TXT = [r"E:\huyadev\ansible\offline\21-5-12_offline.txt"]
    if len(OFFLINE_TXT):
        offline_hosts = get_all_ip_from_files(OFFLINE_TXT)
        print("find ip in", OLD_TXT)
        for file in OLD_TXT:
            remove_ip_in_file(file, offline_hosts)


def find_duplicated_ip(files):
    ips = get_all_ip_from_files(files)
    duplicated_ip = [x for x in ips if ips.count(x) > 1]

    set_duplicated = set(duplicated_ip)
    print(set_duplicated)


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