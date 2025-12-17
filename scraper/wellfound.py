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

    job_cards = soup.find_all("a", href=True)

    for card in job_cards:
        href = card["href"]

        if "/jobs/" not in href:
            continue

        text = card.get_text(" ", strip=True)

        if not text:
            continue

        jobs.append({
            "company": "Unknown Startup",
            "title": text[:80],
            "description": text,
            "url": "https://wellfound.com" + href,
            "date": today,
            "source": "Wellfound"
        })

    print(f"Wellfound jobs fetched: {len(jobs)}")
    return jobs