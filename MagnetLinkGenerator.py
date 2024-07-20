def add_tracker(original_link: str, *tracker_urls: str) -> str:
    link_list: list[str] = [original_link]
    for url in tracker_urls:
        link_list.append(url)
    new_link = "&tr=".join(link_list)
    return new_link

def write_result(magnet_link: str):
    pass