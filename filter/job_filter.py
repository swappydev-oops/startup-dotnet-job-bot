KEYWORDS = [
    ".net", "asp.net", "c#", "entity framework", "dotnet", "mvc", "asp.net core"
]

def is_dotnet_job(text):
    text = text.lower()
    return any(keyword in text for keyword in KEYWORDS)

def estimate_bgv(text):
    text = text.lower()
    if any(x in text for x in ["mnc", "iso", "compliance", "background verification"]):
        return "High"
    if any(x in text for x in ["startup", "early stage", "seed"]):
        return "Low"
    return "Medium"