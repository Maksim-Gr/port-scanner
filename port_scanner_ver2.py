import socket
from multiprocessing import Pool
from netaddr import IPRange


def check_for_open_ports(args):
    """Scan open ports"""
    host, port = args
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set timeout to catch all ports
    sock.settimeout(1)
    try:
        sock.connect((host, port))
        print(f"{host} Port:  {port} is open")
    except socket.error:
        pass
    finally:
        sock.close()


if __name__ == "__main__":
    ports_to_check: list = [
        43, 80, 109, 110,
        115, 118, 119, 143,
        194, 220, 443, 540,
        585, 591, 1112, 1433,
        1443, 3128, 3197, 3306,
        3899, 4224, 4444, 5000,
        6379, 8080, 1000
    ]

    # preparing data set for scanning
    ip_start_range, ip_end_range = input(
        "Enter Range in format IP-IP: ").split("-")
    ip_range = IPRange(ip_start_range, ip_end_range)
    pool = Pool(processes=5)
    for ip in ip_range:
        host_to_scan = str(ip)
        pool.map(check_for_open_ports, [(host_to_scan, port) for port in ports_to_check])
