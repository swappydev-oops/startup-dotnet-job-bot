import requests
from bs4 import BeautifulSoup
from datetime import date

def fetch_jobs():
    url = "https://wellfound.com/jobs?posted_today=true"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    today = date.today().isoformat()

    links = soup.find_all("a", href=True)

    for a in links:
        href = a["href"]

        if "/jobs/" not in href:
            continue

        text = a.get_text(strip=True)
        if not text:
            continue

        jobs.append({
            "source": "Wellfound",
            "company": "Unknown",
            "title": text[:100],
            "description": text,
            "url": "https://wellfound.com" + href,
            "date": today
        })

    print("Wellfound jobs fetched:", len(jobs))
    return jobs