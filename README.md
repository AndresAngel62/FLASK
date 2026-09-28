# Flask Network API

This project is a small Flask application that loads network device information from `API.json` and exposes it through HTTP routes for reading device metadata such as MAC address, name, protocols, VLAN configuration, ports, IP, and SSH status.

## Project purpose

The app reads a JSON inventory of devices and exposes:

- the first device entry from the dataset
- device lookup by MAC address
- static mock responses for testing and API demonstration

## Repository and branch status

Current local development branch:

- `feature/FlaskV01`

Remote target branch referenced by the project:

- `feature` on GitHub: https://github.com/AndresAngel62/FLASK/tree/feature

## Project structure

```text
FLASK/
├── API.json              # Network inventory source data
├── app.py                # Flask app and route definitions
├── C1.py                 # Additional exercise or prototype file
├── C2.py
├── C3.py
├── C4.py
├── Ejem1.py
├── lol.py
├── PreExamen.py/         # Classroom exercises folder
├── postman/              # Postman collections and related files
├── req.txt               # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Local environment exclusions
└── venv/                 # Virtual environment (ignored by git)
```

## Requirements

The app depends on Flask and the standard Python runtime.

```bash
python -m venv venv
venv\Scripts\activate
pip install -r req.txt
```

## Run the application

```bash
python app.py
```

Then open:

- http://127.0.0.1:5000/

## Routes defined in `app.py`

The API exposes 10 core endpoints for viewing network device information and the application state.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/` | Returns the first device record loaded from `API.json`. |
| GET | `/json/<mac>` | Returns a compact summary for a single device by MAC address. |
| GET | `/servidor_1` | Returns a static mock JSON response representing a sample server configuration. |
| GET | `/devices` | Returns a dictionary with all MAC addresses mapped to their device names. |
| GET | `/devices/all` | Returns the complete inventory from `API.json`. |
| GET | `/device/<mac>` | Returns the full JSON object for one specific device. |
| GET | `/device/<mac>/name` | Returns the name of a specific device. |
| GET | `/device/<mac>/status` | Returns whether the device is active or inactive. |
| GET | `/device/<mac>/protocols` | Returns the network protocols configured on the device. |
| GET | `/device/<mac>/vlans` | Returns the VLAN information associated with the device. |

### Endpoint details

#### 1) `/`

Returns the default device object from the JSON inventory. This is useful for quick testing of the application startup and initial payload.

```json
{
  "Name": "R1",
  "Protocolos": ["OSPF", "ST"],
  "Status": true,
  "VLANs": {
    "VL1": {
      "Ports": ["G0/1"],
      "Plicies": ["ACL1"],
      "ET": true,
      "IP": "192,168.10.1",
      "SSH": true
    }
  }
}
```

#### 2) `/json/<mac>`

Returns a simplified summary of a device using the MAC address as the lookup key.

```json
{
  "mac": "3D:RF:09:7F:02",
  "name": "R2",
  "status": false,
  "protocols": ["RIP", "ST"],
  "vlan_count": 1
}
```

#### 3) `/servidor_1`

Returns a mock server payload used for testing or as a sample API response.

```json
{
  "0001": {
    "ip": "192.168.0.1",
    "divice": "Router",
    "policy": ["Ro", "Not Allowed", [0.2, 0.3, 0.5]],
    "status": true
  }
}
```

#### 4) `/devices`

Returns all devices as a dictionary of MAC address → device name.

```json
{
  "3D:RF:09:7F:01": "R1",
  "3D:RF:09:7F:02": "R2"
}
```

#### 5) `/devices/all`

Returns the complete JSON dataset from `API.json`, giving the full device inventory.

#### 6) `/device/<mac>`

Returns the complete record of a single device, including its metadata, protocols, and VLAN structure.

#### 7) `/device/<mac>/name`

Returns only the device name for the requested MAC address.

```json
{
  "mac": "3D:RF:09:7F:02",
  "name": "R2"
}
```

#### 8) `/device/<mac>/status`

Returns the current status of the device, typically as a boolean value.

```json
{
  "mac": "3D:RF:09:7F:02",
  "status": false
}
```

#### 9) `/device/<mac>/protocols`

Returns the communication or routing protocols enabled on the device.

```json
{
  "mac": "3D:RF:09:7F:02",
  "protocols": ["RIP", "ST"]
}
```

#### 10) `/device/<mac>/vlans`

Returns the VLAN definitions for the device, including their configuration details.

```json
{
  "mac": "3D:RF:09:7F:02",
  "vlans": {
    "VL1": {
      "Ports": ["G0/1"],
      "SSH": true,
      "IP": "192.168.10.1"
    }
  }
}
```

> Additional routes exist in the application for deeper inspection, such as ports, SSH status, and health checks, but the 10 main endpoint groups above are the core API routes used for device querying.

## Visual route map

```mermaid
flowchart LR
    A[Client / Browser / Postman] --> B[/]
    A --> C[/json/<mac>]
    A --> D[/servidor_1]
    A --> E[/devices]
    A --> F[/devices/all]
    A --> G[/device/<mac>]
    A --> H[/device/<mac>/name]
    A --> I[/device/<mac>/status]
    A --> J[/device/<mac>/protocols]
    A --> K[/device/<mac>/vlans]
    A --> L[/device/<mac>/ports]
    A --> M[/device/<mac>/ssh]
    A --> N[/health]

    B --> O[Returns first device]
    C --> P[Device summary]
    D --> Q[Mock server JSON]
    E --> R[Device list]
    F --> S[Full JSON collection]
    G --> T[Single device data]
    H --> U[Name lookup]
    I --> V[Status lookup]
    J --> W[Protocol lookup]
    K --> X[VLAN lookup]
    L --> Y[Port lookup]
    M --> Z[SSH check]
    N --> AA[Health check]
```

## Notes

- The application currently uses a static JSON file instead of a database.
- The route behavior is intentionally simple for educational and prototype use.
- Some values in the dataset contain formatting inconsistencies such as `IP`: `"192,168.10.1"` with a comma instead of a dot; this may need normalization later.
