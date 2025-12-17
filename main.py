from scraper.wellfound import fetch_jobs as fetch_wellfound
from scraper.cutshort import fetch_jobs as fetch_cutshort
import pandas as pd
from datetime import date

# Collect jobs from both sources
jobs = []
jobs.extend(fetch_wellfound())
jobs.extend(fetch_cutshort())

print("Total jobs collected:", len(jobs))

# ❌ NO FILTERING – TEST MODE
final_jobs = []

for job in jobs:
    final_jobs.append(job)

today = date.today().isoformat()

df = pd.DataFrame(final_jobs)
df.to_csv(f"jobs_{today}.csv", index=False)

print("CSV created with", len(final_jobs), "jobs")