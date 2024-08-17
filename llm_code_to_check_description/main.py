from typing import Union
from fastapi import FastAPI
import uvicorn


import json
import os

from imports import *
from schemas import *
from check_company_desc import *

app = FastAPI()

#llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

llm = Ollama(temperature=0.0,
            model="mistral",
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

@app.post("/api/check_description")
def evaluate_company_data(body: description):
    company_obj = Company(llm)
    print(body.description)
    check_company = company_obj.check_company_description(body.description)
    return check_company


if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=8000, reload=True)