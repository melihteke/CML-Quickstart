#!/usr/bin/env python3

import requests
import time
from datetime import datetime
import sys
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==================================================
# CONFIG
# ==================================================
CML_IP = "192.168.178.X"
USERNAME = "admin"
PASSWORD = "XXXXXXX"

LAB_ID = "df02a4c4-57d4-49e7-b464-e79e64221377"

DEVICES = [
    {"name": "External-Connection", "id": "226157a9-fa31-4d94-a037-badff6150831"},
    {"name": "BackBone",            "id": "c504a9cd-938d-4274-8713-2777a72e0269"},
    {"name": "NXOS",                "id": "a38f1e50-6238-493d-beaa-666aeaf7950e"},
    {"name": "Router1",             "id": "a95ec305-4baf-4b53-ba66-95d3cc791661"},
    {"name": "Router2",             "id": "6ec29151-dbf1-49c4-a469-3e884dab3adb"},
]

BASE_URL = f"https://{CML_IP}"
START_SLEEP_SECONDS = 120   # 2 minutes

# ==================================================
# UTILS
# ==================================================
def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def fatal(message):
    log(f"FATAL: {message}")
    sys.exit(1)

# ==================================================
# AUTHENTICATION
# ==================================================
def authenticate():
    log("Authenticating to CML...")
    url = f"{BASE_URL}/api/v0/authenticate"

    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    try:
        r = requests.post(url, json=payload, verify=False, timeout=30)
    except Exception as e:
        fatal(f"Authentication request failed: {e}")

    if r.status_code != 200:
        fatal(f"Authentication failed (HTTP {r.status_code}): {r.text}")

    # CML returns token as a plain string
    token = r.text.strip().strip('"')

    if not token:
        fatal("Authentication returned an empty token")

    log("Authentication SUCCESS")
    return token

# ==================================================
# NODE CONTROL
# ==================================================
def start_device(headers, device):
    log(f"Starting device: {device['name']}")
    url = f"{BASE_URL}/api/v0/labs/{LAB_ID}/nodes/{device['id']}/state/start"

    try:
        r = requests.put(url, headers=headers, verify=False, timeout=30)
    except Exception as e:
        fatal(f"START request failed for {device['name']}: {e}")

    if r.status_code not in (200, 204):
        fatal(f"START failed for {device['name']} (HTTP {r.status_code}): {r.text}")

    log(f"{device['name']} START command accepted")
    log(f"Sleeping {START_SLEEP_SECONDS} seconds before next device...")
    time.sleep(START_SLEEP_SECONDS)

def stop_device(headers, device):
    log(f"Stopping device: {device['name']}")
    url = f"{BASE_URL}/api/v0/labs/{LAB_ID}/nodes/{device['id']}/state/stop"

    try:
        r = requests.put(url, headers=headers, verify=False, timeout=30)
    except Exception as e:
        fatal(f"STOP request failed for {device['name']}: {e}")

    if r.status_code not in (200, 204):
        fatal(f"STOP failed for {device['name']} (HTTP {r.status_code}): {r.text}")

    log(f"{device['name']} STOP command accepted")

# ==================================================
# MAIN
# ==================================================
def main():
    # Ask user what they want to do
    print("\n==============================")
    print("CML LAB CONTROLLER")
    print("==============================")
    print("Choose an option:")
    print("1 - START all devices")
    print("2 - STOP all devices")
    choice = input("Enter 1 or 2: ").strip()

    if choice not in ("1", "2"):
        fatal("Invalid choice. Exiting.")

    token = authenticate()
    headers = {"Authorization": f"Bearer {token}"}

    if choice == "1":
        log("=== STARTING DEVICES (SEQUENTIAL) ===")
        for device in DEVICES:
            start_device(headers, device)
        log("ALL DEVICES STARTED")

    elif choice == "2":
        log("=== STOPPING DEVICES (SEQUENTIAL) ===")
        for device in DEVICES:
            stop_device(headers, device)
        log("ALL DEVICES STOPPED")

# ==================================================
if __name__ == "__main__":
    main()
