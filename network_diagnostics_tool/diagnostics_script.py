import os
import platform

def run_command(command):
    result = os.popen(command).read()
    return result

def network_diagnostics(target):
    print(f"\n Pinging {target}...")
    print(run_command(f"ping -n 4 {target}" if platform.system()=="Windows" else f"ping -c 4 {target}"))

    print(f"\n Tracerouting {target}...")
    traceroute_cmd = "tracert" if platform.system()=="Windows" else "traceroute"
    print(run_command(f"{traceroute_cmd} {target}"))

    print(f"\n DNS Lookup for {target}...")
    print(run_command(f"nslookup {target}"))

if __name__ == "__main__": 
    target = input("Enter domain or IP to diagnose: ")
    network_diagnostics(target)
