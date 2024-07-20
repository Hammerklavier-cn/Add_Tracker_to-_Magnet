"""
    Add Tracker Url to Magnet Url
"""

import os, sys
import MagnetLinkGenerator as mlg

original_magnet_link = input("Initial Magnet link:\t")

urls: list[str] = []

while True:
    try:
        url = input("Tracker Url (Press `Ctrl + D(Unix)/Z(Windows)` to stop):\t")
        if url:
            urls.append(url)
    except EOFError:
        merged_megnet_link = mlg.add_tracker(original_magnet_link, *urls)
        if os.name == "nt": # Windows
            os.system("cls")
        elif os.name == "posix": # Unix-like
            os.system("clear")
        print(f"{'-' * 10} Magnet Link with Tracker: {'-' * 10}\n{merged_megnet_link}")
        input('Press <Enter> to exit...')
        sys.exit(0)