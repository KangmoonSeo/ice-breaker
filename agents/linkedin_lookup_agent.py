from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page. 
    Your answer should contain only a URL"""

    tools_for_agent = [
        Tool(
            name="Crawl Google for linked profile page",  # mandatory
            func=get_profile_url,  # mandatory
            description="useful for when you need to the Linkedin page URL",  # almost mandatory, flags 4 determination
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

    linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    # 문자열에서 https://로 시작하는 부분 찾기
    start_index = linked_profile_url.find("https://")

    # https://가 발견된 경우에만 해당 부분을 출력
    if start_index != -1:
        print(":( " + linked_profile_url)
        linked_profile_url = linked_profile_url[start_index:]

    return linked_profile_url
