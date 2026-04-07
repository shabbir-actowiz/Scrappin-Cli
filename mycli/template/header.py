import itertools

HEADERS_LIST = [
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    },
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/17.0 Safari/605.1.15",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/121.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    },
]


def generate_headers():
    headers = []
    base = HEADERS_LIST

    for i in range(20):
        h = base[i % len(base)].copy()

        # Add slight realistic variations
        h["Accept-Language"] = [
            "en-US,en;q=0.9",
            "en-GB,en;q=0.8",
            "en-IN,en;q=0.9",
            "en-US,en;q=0.8,hi;q=0.6"
        ][i % 4]

        h["Cache-Control"] = ["max-age=0", "no-cache"][i % 2]

        headers.append(h)

    return headers


header_cycle = itertools.cycle(generate_headers())

def get_headers():
    return next(header_cycle)