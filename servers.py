import os
import platform

def ping_server(server):
    """Ping a server and return True if reachable, False otherwise."""
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    response = os.system(f"ping {param} {server} > /dev/null 2>&1")
    return response == 0

# Read server names from file
try:
    with open("servers.txt", "r") as file:
        servers = [line.strip() for line in file.readlines()]

    # Ping each server
    for server in servers:
        if server:
            status = "✅ Reachable" if ping_server(server) else "❌ Unreachable"
            print(f"{server}: {status}")

except FileNotFoundError:
    print("❌ Error: servers.txt not found!")
except Exception as e:
    print(f"❌ An error occurred: {e}")