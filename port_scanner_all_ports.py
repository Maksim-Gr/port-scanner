import socket
from multiprocessing import Process


def scan_port(hostname, port_number):
    """Scan open ports"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set timeout to catch all ports
    sock.settimeout(1)
    try:
        sock.connect((hostname, port_number))
        print(hostname, "Port: ", port_number, "is open")
    except socket.error:
        pass
    finally:
        sock.close()


if __name__ == "__main__":
    print("\u001b[32mPort Scanner")
    print("Scanner will search for open ports. You have to specify end of ports range.\u001b[0m ")
    ports_range = [port for port in range(int(input("\u001b[4mEnter end of ports range\u001b[0m: ")) + 1)]
    host_name = str(input("\u001b[4mEnter Ip address\u001b[0m: "))
    list_of_scans = []
    try:
        for port in ports_range:
            scan_process = Process(target=scan_port, args=(
                host_name, port), daemon=True)
            list_of_scans.append(scan_process)
        for scan in list_of_scans:
            scan.run()
    except KeyboardInterrupt:
        print("You have manually stop the program")
