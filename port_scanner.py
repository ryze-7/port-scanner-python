import socket
from datetime import datetime
import os
import time

ports = [21, 22, 25, 80, 443, 67, 68]
ip_addr = input("Enter IPv4 for port scanning: ")
ports_name = ["ftp", "ssh", "smtp", "http", "https", "dhcp", "dhcp"]
now = datetime.now()

start_time = time.time()

response = os.system(f"ping -c 1 {ip_addr} > /dev/null 2>&1")
print(f"Starting Port Scan at {now}")
print(f"Port Scan Report for {ip_addr}\n")

if response == 0:
    print(f"{'PORT':<8} {'STATE':<8} {'SERVICE':<8} {'VERSION'}")
    
    for i in range(len(ports)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5.0)
        try:
            s.connect((ip_addr, ports[i]))
            print(f"{str(ports[i])+'/tcp':<8} {'open':<8} {ports_name[i]:<8}", end=" ")
            
            try:
                s.settimeout(2.0)
                banner = s.recv(1024).decode().strip()
                print(f"{banner}")
                
            except:
                print("")
            
        except socket.timeout:
            print(f"{str(ports[i])+'/tcp':<8} {'filtered':<8} {ports_name[i]:<8}")
            
        except ConnectionRefusedError:
            print(f"{str(ports[i])+'/tcp':<8} {'close':<8} {ports_name[i]:<8}")

        finally:
            s.close()

else:
    print(f"Host seems down.")

end_time = time.time()

total_time = end_time - start_time
print(f"\nPort Scan done for {ip_addr} in {total_time:.2f} seconds")
