from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile
load_dotenv()

OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")




if __name__ == '__main__':
    print("Hello Langchain")
    
    
    summary_template = """
    given the Linkedin information {information} about a personn from I want you to create:
    1. a short summary of the person
    2. two interesting facts about the person"""
    
    
    summary_promt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
        )
    
    #temperature = how much the model will be creative
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    chain = LLMChain(llm=llm, prompt=summary_promt_template)
    
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/harrison-chase-961287118/")

    print(chain.run(information=linkedin_data))
    
    
