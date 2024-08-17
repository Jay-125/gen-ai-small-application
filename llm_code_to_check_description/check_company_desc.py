from schemas import *
from imports import *

class Company():

    def __init__(self, llm) -> None:
        self.llm = llm

    def check_company_description(self, company_desc):
        prompt = PromptTemplate(
        input_variables=["company_desc"],
        template="""You are an excellent analyser in a company and you are reviewing some company data. You are given the description of the company
        and your task is to check whether the company is a technology based company or not. Below is the company description.
        {company_desc}.

        And remember to give output only in json form that has only two keys:
        1. Company name
        2. Yes or No (whether the company is technology based or not) 
        """
        ,
        )
        llmchain = LLMChain(llm=self.llm, prompt=prompt)
        company_chain = llmchain({"company_desc":company_desc})
        check_company = json.loads(company_chain['text'])
        return check_company
