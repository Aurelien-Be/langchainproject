import os
import requests
from dotenv import load_dotenv
load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_disc= {"Authorization": f'Bearer {os.getenv("PROXYCURL_API_KEY")}'}
    
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_disc
    )
    data = response.json()
    
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    
    if data.get("groups"):
        for group.dict in data.get("groups"):
            group.dict.pop("profile_pic_url")
            
            
    return data
