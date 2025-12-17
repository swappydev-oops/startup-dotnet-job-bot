import requests
from bs4 import BeautifulSoup
from datetime import date

def fetch_jobs():
    url = "https://wellfound.com/jobs?posted_today=true"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    today = date.today().isoformat()

    for job in soup.select("div[data-test='JobCard']"):
        title = job.select_one("h2")
        company = job.select_one("h3")
        link = job.find("a", href=True)

        if not title or not company or not link:
            continue

        jobs.append({
            "company": company.text.strip(),
            "title": title.text.strip(),
            "description": title.text.strip(),
            "url": "https://wellfound.com" + link["href"],
            "date": today
        })

    return jobs