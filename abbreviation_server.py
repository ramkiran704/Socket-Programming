import socket
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

TIMEZONE_MAP = {
    "UTC": "UTC",
    "GMT": "Etc/GMT",
    "EST": "America/New_York",
    "EDT": "America/New_York",
    "CST": "America/Chicago",
    "CDT": "America/Chicago",
    "MST": "America/Denver",
    "MDT": "America/Denver",
    "PST": "America/Los_Angeles",
    "PDT": "America/Los_Angeles",
    "IST": "Asia/Kolkata",
    "BST": "Europe/London",
    "CET": "Europe/Paris",
    "JST": "Asia/Tokyo",
    "AEST": "Australia/Sydney",
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("0.0.0.0", 5000))

print("Abbreviation Time Server running on port 5000...")

while True:
    data, address = server_socket.recvfrom(1024)

    abbrev = data.decode().strip().upper()

    print(f"Received request for '{abbrev}' from {address}")

    if abbrev in TIMEZONE_MAP:
        try:
            tz_name = TIMEZONE_MAP[abbrev]

            now = datetime.now(ZoneInfo(tz_name))

            response = now.strftime(
                f"%Y-%m-%d %H:%M:%S {abbrev}"
            )

        except ZoneInfoNotFoundError:
            response = "ERROR: Timezone database entry not found on server."

    else:
        valid_options = ", ".join(TIMEZONE_MAP.keys())

        response = (
            f"ERROR: Unknown abbreviation '{abbrev}'. "
            f"Valid abbreviations:\n{valid_options}"
        )

    server_socket.sendto(response.encode(), address)