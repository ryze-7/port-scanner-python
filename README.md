# Port Scanner

A Python-based port scanner similar to Nmap for network reconnaissance and service detection.

## Features

- [ ] Version Scan
- [ ] Port State Detection (Open, Filtered, Closed)
- [ ] Ping Scan to determine if host is up or down

## How to Use

```bash
python port_scanner.py
```

When prompted, enter the IPv4 address for scanning:

```
Enter IPv4 for scanning: <ip_addr>
```

## How It Works

### Socket Configuration
Uses the `socket` module for low-level networking operations:
- `AF_INET` for IPv4 addressing
- `SOCK_STREAM` for TCP protocol

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### Host Detection
Uses the `os` module to perform ping scans and verify if the host is reachable:

```python
response = os.system(f"ping -c 1 {ip_addr} > /dev/null 2>&1")
```

### Version Detection
Retrieves service banners using the `recv()` function to identify running services:

```python
banner = s.recv(1024).decode().strip()
```

---

**Author:** Shourya Kashyap  
**Date:** May 2026