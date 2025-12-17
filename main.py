from scraper.wellfound import fetch_jobs
from filter.job_filter import is_dotnet_job, estimate_bgv
from email_template.email_generator import generate_email
import pandas as pd
from datetime import date

jobs = fetch_jobs()
final_jobs = []

for job in jobs:
    if is_dotnet_job(job["title"]):
        job["bgv"] = estimate_bgv(job["description"])
        job["email_template"] = generate_email(job["company"], job["title"])
        final_jobs.append(job)

today = date.today().isoformat()
df = pd.DataFrame(final_jobs)
df.to_csv(f"jobs_{today}.csv", index=False)

print("CSV file created")