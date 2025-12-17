KEYWORDS = [
    ".net", "dotnet", "asp", "c#",
    "backend", "full stack", "api",
    "software engineer", "developer"
]

def is_dotnet_job(text):
    text = text.lower()
    return any(k in text for k in KEYWORDS)

def estimate_bgv(text):
    text = text.lower()
    if any(x in text for x in ["mnc", "iso", "compliance", "background verification"]):
        return "High"
    if any(x in text for x in ["startup", "early stage", "seed"]):
        return "Low"
    return "Medium"