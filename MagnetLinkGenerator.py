def add_tracker(original_link: str, *tracker_urls: str) -> str:
    link = original_link
    for url in tracker_urls:
        link += url
    return link

def write_result(magnet_link: str):
    pass