"""
    Add Tracker Url to Magnet Url
"""

import os
import MagnetLinkGenerator as mlg

original_magnet_link = input("Initial Magnet link:\t")

urls: list[str] = []

while True:
    try:
        url = input("Tracker Url (Press `Ctrl + D` to stop):\t")
        if url:
            urls.append(url)
    except EOFError:
        merged_megnet_link = mlg.add_tracker(original_magnet_link, *urls)
        os.system("clear")
        print(f"{'-' * 10}Magnet Link with Tracker: {'-' * 10}\n{merged_megnet_link}")
        exit(0)