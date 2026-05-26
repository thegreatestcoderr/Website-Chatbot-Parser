import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

def crawl_website(start_url, max_pages=50):
    visited = set()
    queue = deque([start_url])
    domain = urlparse(start_url).netloc
    all_text = []

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue

        try:
            print(f"Crawling: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print(f"Failed: {url} ({e})")
            continue

        visited.add(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract readable text
        page_text = soup.get_text(separator="\n", strip=True)
        all_text.append({
            "url": url,
            "text": page_text
        })

        # Find internal links
        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(url, href)
            parsed = urlparse(full_url)

            if parsed.netloc == domain and full_url not in visited:
                queue.append(full_url)

    return all_text
