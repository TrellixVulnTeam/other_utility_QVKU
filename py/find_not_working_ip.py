
import csv
import remove_ip


def get_online_hosts():
    CSV_FILE = r"E:\downloads\grafana_data_export.csv"
    SERVER_IP = "serverip"

    hosts = []
    with open(CSV_FILE, newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            hosts.append(row[SERVER_IP])

    print(f"get {len(hosts)} hosts")
    return hosts


def get_all_hosts():
    GIT_PATH = "E:\\huyadev\\ansible\\"
    SOURCE_FILE = ['prod.ini','tx_part_two.ini','al_sz.ini','tx_chengdu_replace.ini',"tx_8Q.ini","tx_beijing_replace.ini","tx_t4_replace.ini"]

    all_hosts = []
    for file in SOURCE_FILE:
        filename = GIT_PATH+file
        all_hosts+=remove_ip.get_ip_from_file(filename)

    print(f"{len(all_hosts)} all hosts")
    return all_hosts

def main():
    online_hosts = get_online_hosts()

    all_hosts = get_all_hosts()

    UNREACHABLE = ['112.74.175.226','49.233.117.98','81.69.191.51','81.69.202.68']
    for ip in online_hosts:
        all_hosts.remove(ip)

    for ip in UNREACHABLE:
        all_hosts.remove(ip)

    for ip in all_hosts:
        print(ip)


if __name__ == "__main__":
    main()