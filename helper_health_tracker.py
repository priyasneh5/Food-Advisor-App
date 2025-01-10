from langchain_huggingface import HuggingFaceEndpoint 
import os
from langchain import PromptTemplate, LLMChain
from langchain.chains import LLMChain

api_key = os.getenv('ACCESS_TOKEN')
repo_id ="mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=api_key)




def generate_response(question):
    prompt_template_name = PromptTemplate(
        input_variables=['food_item'],
        template="What is the gylcamic load of {food_item}? Write in 1 line"
    )

    chain = LLMChain(llm=llm,prompt=prompt_template_name)
    response = chain.run(question)
    return response

if __name__ == "__main__":
    print(generate_response("Chapati"))