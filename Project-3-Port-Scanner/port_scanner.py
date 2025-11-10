# port_scanner.py
import socket
import sys
import time

def scan_ports(target, ports):
    print(f"\nStarting scan for {target} ...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN]  Port {port}")
            else:
                print(f"[CLOSED] Port {port}")
        except Exception as e:
            print(f"[ERROR] Port {port} -> {e}")
        finally:
            try:
                sock.close()
            except:
                pass
        # tiny delay so output is readable
        time.sleep(0.05)
    print("\nScan complete.\n")

if __name__ == "__main__":
    # Helpful message so you know the program is running
    print("Simple Port Scanner - scans ports 20 to 30 on the target IP.")
    print("IMPORTANT: Only scan machines you own or have permission to test.\n")
    # Prompt for input
    try:
        target_ip = input("Enter target IP (e.g., 127.0.0.1): ").strip()
        if not target_ip:
            print("No IP entered. Exiting.")
            sys.exit(0)
    except EOFError:
        print("\nNo input received. Make sure you run the file in an interactive terminal.")
        sys.exit(1)

    ports_to_scan = range(20, 31)  # ports 20-30 inclusive
    scan_ports(target_ip, ports_to_scan)
