# CML Lab Controller

**Quickly start and stop Cisco CML / DevNet lab devices with a simple Python script.**

I built this repository to **quickly start and stop my DevNet/CML lab devices**. The script allows you to:  

- Authenticate with Cisco CML  
- Start or stop lab devices **sequentially**  
- Control the **order of devices** (External-Connection and BackBone first, then NXOS, Router1, Router2)  
- Sleep between device operations to allow proper boot/shutdown  

<img width="1334" height="773" alt="image" src="https://github.com/user-attachments/assets/43fe701a-3cc4-4d78-9d35-f7df059f61d5" />


---

## Features

- Interactive **start/stop menu**  
- Sequential execution to avoid resource spikes  
- Automatic **5-minute delay** between devices (configurable)  
- Clear timestamped logs for each operation  
- Fully Python-based (only requires `requests`)  

---

## Prerequisites

- Python 3.8+  
- `requests` library:

```bash
pip install requests

## Usage

1. **Clone or download this repository.**  

2. **Update the configuration** in `cml-lab-start-stop.py`:

```python
CML_IP = "your_cml_ip"
USERNAME = "your_username"
PASSWORD = "your_password"
LAB_ID = "your_lab_id"
```


3. Install the required Python library if not already installed:
```python
pip install requests
```
4. Run the script

```python
python cml-lab-start-stop.py
```


5. Choose option
```python
(.venv) melih$ python cml-lab-start-stop.py 
==============================
CML LAB CONTROLLER
==============================
Choose an option:
1 - START all devices
2 - STOP all devices
Enter 1 or 2: 1
[2026-01-08 22:45:19] Authenticating to CML...
[2026-01-08 22:45:19] Authentication SUCCESS
[2026-01-08 22:45:19] === STARTING DEVICES (SEQUENTIAL) ===
[2026-01-08 22:45:19] Starting device: External-Connection
[2026-01-08 22:45:19] External-Connection START command accepted
[2026-01-08 22:45:19] Sleeping 120 seconds before next device...
[2026-01-08 22:47:25] Starting device: BackBone
[2026-01-08 22:47:25] BackBone START command accepted
[2026-01-08 22:47:25] Sleeping 120 seconds before next device...
[2026-01-08 22:49:29] Starting device: NXOS
[2026-01-08 22:49:30] NXOS START command accepted
[2026-01-08 22:49:30] Sleeping 120 seconds before next device...
[2026-01-08 22:51:36] Starting device: Router1
[2026-01-08 22:51:36] Router1 START command accepted
[2026-01-08 22:51:36] Sleeping 120 seconds before next device...
[2026-01-08 22:53:42] Starting device: Router2
[2026-01-08 22:53:42] Router2 START command accepted
[2026-01-08 22:53:42] Sleeping 120 seconds before next device...
[2026-01-08 22:55:48] ALL DEVICES STARTED

(.venv) melih$ python cml-lab-start-stop.py 
==============================
CML LAB CONTROLLER
==============================
Choose an option:
1 - START all devices
2 - STOP all devices
Enter 1 or 2: 2
[2026-01-08 22:56:52] Authenticating to CML...
[2026-01-08 22:56:52] Authentication SUCCESS
[2026-01-08 22:56:52] === STOPPING DEVICES (SEQUENTIAL) ===
[2026-01-08 22:56:52] Stopping device: External-Connection
[2026-01-08 22:56:52] External-Connection STOP command accepted
[2026-01-08 22:56:52] Stopping device: BackBone
[2026-01-08 22:56:53] BackBone STOP command accepted
[2026-01-08 22:56:53] Stopping device: NXOS
[2026-01-08 22:56:54] NXOS STOP command accepted
[2026-01-08 22:56:54] Stopping device: Router1
[2026-01-08 22:56:54] Router1 STOP command accepted
[2026-01-08 22:56:54] Stopping device: Router2
[2026-01-08 22:56:55] Router2 STOP command accepted
[2026-01-08 22:56:55] ALL DEVICES STOPPED

```
