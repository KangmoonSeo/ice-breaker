from typing import Tuple

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.linkedin import scrape_linked_profile
from third_parties.twitter import scrape_user_tweets
from output_parsers.output_parsers import person_intel_parser, PersonIntel


def ice_break(name: str, is_twitter: bool = False) -> Tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linked_profile(linkedin_profile_url=linkedin_profile_url)

    twitter_data = "no_data"
    if is_twitter:
        twitter_username = twitter_lookup_agent(name=name)
        twitter_data = scrape_user_tweets(username=twitter_username, num_tweets=5)

    summary_template = """
    given the Linkedin information {linkedin_information} 
    and Twitter {twitter_information} about a person from I want you to create in Korean:
    1. a short summary
    2. two interesting facts about them
    3. A topic that may interest them
    4. 2 creative Ice breakers to open a conversation with them 
    \n{format_instructions}
    """
    # 템플릿 끝애 format_instructions를 추가해서 output 형식을 알려줌
    # output_parser의 추상화

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    result = chain.run(
        linkedin_information=linkedin_data, twitter_information=twitter_data
    )
    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")
