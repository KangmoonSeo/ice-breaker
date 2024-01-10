from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linked_profile

if __name__ == "__main__":
    summary_template = """
        주어진 한 사람의 대한 정보 {information} 에 대해 다음 내용을 만들어 생성하고 한글로 출력해 줘.:
        1. 간단한 요약
        2. 그 사람에 대한 2개의 fun facts
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linked_profile(
        linkedin_profile_url="https://www.linkedin.com/in/harrison-chase-961287118"
    )

    print(f"linkedin_data: {linkedin_data}")
    response = chain.run(information=linkedin_data)
    print(response)
