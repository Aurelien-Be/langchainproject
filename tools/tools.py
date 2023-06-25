from langchain.serpapi import SerpAPIWrapper

def get_profile_url(text:str) ->str:
    """"Searches for Linkedin profile page"""
    search = SerpAPIwrapper()
    res = search.run(f"{text}")
    return res
    
    