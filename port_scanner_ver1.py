import socket
from multiprocessing import Pool
from netaddr import IPRange
import itertools


def check_for_open_ports(host: str, port: int):
    """Scan open ports"""
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
    ports_hosts: list = []
    for ip in ip_range:
        single_host = str(ip)
        ports_hosts.append([(single_host, port) for port in ports_to_check])
    scan_data = list(itertools.chain.from_iterable(ports_hosts))
    with Pool(processes=5) as pool:
        pool.starmap(check_for_open_ports, scan_data)
      