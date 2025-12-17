import requests
from bs4 import BeautifulSoup
from datetime import date

def fetch_jobs():
    url = "https://cutshort.io/jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    today = date.today().isoformat()

    job_cards = soup.find_all("div", class_="job-card")

    for job in job_cards:
        title_tag = job.find("h2")
        company_tag = job.find("h3")
        link_tag = job.find("a", href=True)

        if not title_tag or not link_tag:
            continue

        jobs.append({
            "company": company_tag.text.strip() if company_tag else "Startup",
            "title": title_tag.text.strip(),
            "description": title_tag.text.strip(),
            "url": "https://cutshort.io" + link_tag["href"],
            "date": today,
            "source": "Cutshort"
        })

    print(f"Cutshort jobs fetched: {len(jobs)}")
    return jobs