from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0.4, model_name="gpt-3.5-turbo")

    template = """given the name {name_of_person} I want you to find a link to their Twitter profile page, 
    and extract from it their username.
    In Your Final answer only the person's username"""

    tools_for_agent = [
        Tool(
            name="Crawl Google for Twitter profile page",  # mandatory
            func=get_profile_url,  # mandatory
            description="useful for when you need to the Twitter page URL",  # almost mandatory, flags 4 determination
        ),
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,  # 가장 중요한 매개 변수, 추론 과정의 상세한 로깅을 요청 여부
    )

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"],
    )

    twitter_username = agent.run(prompt_template.format_prompt(name_of_person=name))

    return twitter_username
