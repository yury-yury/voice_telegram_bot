import os
import openai
from dotenv import load_dotenv


load_dotenv()

openai.organization = "org-Om2l4QLOx5iWWY7yV7P3Xtol"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()