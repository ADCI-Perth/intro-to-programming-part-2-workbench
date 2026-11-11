"""Section 2.3: JSON. Writes device.json next to this file, then reads it."""

import json
from pathlib import Path

HERE = Path(__file__).parent
device_file = HERE / "device.json"

device = {
    "name": "front-desk-pc",
    "address": "192.0.2.15",
    "ports": [80, 443],
    "patched": True,
    "owner": None,
}

# dumps: Python value -> JSON string.
text = json.dumps(device)
print(text)
print(type(text))

# indent=2 makes the string easier for people to read.
print(json.dumps(device, indent=2))

# loads: JSON string -> Python value.
incoming = '{"user": "user01", "attempts": 3, "locked": false}'
record = json.loads(incoming)
print(record)
print(record["attempts"] + 1)
print(type(record["locked"]))

# dump: Python value -> JSON file.
with open(device_file, "w", encoding="utf-8") as file:
    json.dump(device, file, indent=2)

# load: JSON file -> Python value.
with open(device_file, "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded["name"])
print(loaded["ports"])
print(loaded == device)

# Two things change on the way through JSON.
changed = json.loads(json.dumps({"point": (3, 4), 200: "OK"}))
print(changed)

# Text that is not JSON raises an error you can catch.
try:
    json.loads("{'user': 'user01'}")
except json.JSONDecodeError:
    print("That text is not valid JSON.")


# An object cannot go straight into JSON.
class Device:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def to_dict(self):
        return {"name": self.name, "address": self.address}


printer = Device("printer-2", "192.0.2.40")

try:
    json.dumps(printer)
except TypeError as error:
    print("TypeError:", error)

# Turn the object into a dictionary first.
print(json.dumps(printer.to_dict()))

# A list of objects becomes a list of dictionaries.
devices = [printer, Device("scanner-1", "192.0.2.41")]
print(json.dumps([d.to_dict() for d in devices], indent=2))
