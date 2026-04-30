import os
import platform
import socket
import subprocess
import time

def clear_screen():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if platform.system().lower() == 'windows' else 'clear')

def typewriter_print(text, delay=0.02):
    """Prints text with a typing animation effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_banner():
    """Displays the Mr_NABIN v2 ASCII art banner."""
    banner = r"""
  __  __         _   _  ____  ____ ___ _   _ 
 |  \/  |_ __   | \ | |/ _  || __ )_ _| \ | |
 | |\/| | '__|  |  \| | (_| ||  _ \ | ||  \| |
 | |  | | |     | |\  |\__,_|| |_) || || |\  |
 |_|  |_|_|     |_| \_||___/ |____/___||_| \_|
                                          v2.0
    ==========================================
    [+] Website & IP Ping Tool
    [+] Created for Network Diagnostics
    ==========================================
    """
    print(banner)

def resolve_host(hostname):
    """Converts a URL/Domain to an IP address."""
    clean_host = hostname.replace("http://", "").replace("https://", "").split('/')[0]
    try:
        ip = socket.gethostbyname(clean_host)
        return clean_host, ip
    except socket.gaierror:
        return clean_host, None

def start_tool():
    clear_screen()
    print_banner()
    
    typewriter_print("[?] Enter the target URL or IP address below...")
    target = input("Mr_NABIN >> ").strip()
    
    domain, ip = resolve_host(target)
    
    if not ip:
        print(f"\n[!] Error: Unable to resolve '{domain}'")
        return

    print(f"\n[!] Target Locked: {domain} ({ip})")
    print("[!] Initializing packets... Press Ctrl+C to exit.\n")
    time.sleep(1.5)

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    try:
        while True:
            # Running the system ping command
            command = ['ping', param, '1', ip]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            if result.returncode == 0:
                # Formatting the output to look cleaner
                print(f"  [PING SUCCESS] -> {ip} | Status: Online")
            else:
                print(f"  [PING FAILED]  -> {ip} | Status: Offline")
            
            time.sleep(1) # Interval between pings
            
    except KeyboardInterrupt:
        print("\n\n[!] Session Terminated. Goodbye Mr_NABIN.")

if __name__ == "__main__":
    start_tool()