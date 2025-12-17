from scraper.wellfound import fetch_jobs as fetch_wellfound
from scraper.cutshort import fetch_jobs as fetch_cutshort
from filter.job_filter import is_dotnet_job, estimate_bgv
from email_template.email_generator import generate_email
import pandas as pd
from datetime import date

jobs = []
jobs.extend(fetch_wellfound())
jobs.extend(fetch_cutshort())

print("Total jobs collected:", len(jobs))

final_jobs = []

for job in jobs:
    combined_text = job["title"] + " " + job["description"]

    if is_dotnet_job(combined_text):
        job["bgv"] = estimate_bgv(combined_text)
        job["email_template"] = generate_email(job["company"], job["title"])
        final_jobs.append(job)

today = date.today().isoformat()
df = pd.DataFrame(final_jobs)
df.to_csv(f"jobs_{today}.csv", index=False)

print("Final matching jobs:", len(final_jobs))