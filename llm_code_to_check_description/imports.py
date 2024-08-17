import json
from langchain.prompts import PromptTemplate

from langchain.evaluation.qa import QAEvalChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

