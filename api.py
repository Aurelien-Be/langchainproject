from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

if __name__ == '__main__':
    print("Hello Langchain")
    
    summary_template = """
    given the information {information} about a personn from I want you to create:
    1. a short summary of the person
    2. two interesting facts about the person
    """
    
    summary_promt_template = PromptTemplate(input_variables="information", template=summary_template)