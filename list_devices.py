"""Lists every device on the Wyze account with its MAC address and model code.

Run this after pairing a new bulb/plug in the Wyze app to get the exact
mac/model values to add to BULB_HARDWARE or PLUG_HARDWARE in wyze_setbulbs.py.
"""

from wyze_setbulbs import get_wyze_client


def main():
    client = get_wyze_client()
    devices = client.devices_list()

    if not devices:
        print("No devices found on this account.")
        input("\nPress Enter to exit...")  # Keeps window open
        return

    for device in devices:
        print(
            f"{device.nickname:<30} "
            f"mac={device.mac:<20} "
            f"model={device.product.model:<12} "
            f"type={device.product.type}"
        )

    input("\nPress Enter to exit...")  # Keeps window open


if __name__ == "__main__":
    main()
