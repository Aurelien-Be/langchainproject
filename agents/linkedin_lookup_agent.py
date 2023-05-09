from langchain import PromtTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

def lookup(name: str) -> str:
    return "Linkedin Profil Url"