from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """
이재용(李在鎔, 1968년 6월 23일~)은 대한민국의 기업인이다. 삼성그룹 제3대 총수, 삼성전자 회장이다.

생애
1968년 6월 23일 이건희와 홍라희 사이의 1남 3녀 중 장남으로 태어났다. 경기초등학교, 청운중학교, 경복고등학교, 서울대학교에서 동양사학 학사, 게이오기주쿠 대학 대학원 경영학 석사, 아이비 리그 하버드대학교 경영대학원(Harvard Business School) 경영학 박사를 수료하였다.

1998년 6월 임창욱의 장녀 임세령과 결혼하였고 임세령과의 사이에 아들 한 명과 딸 한 명을 두었다. 임세령이 2009년 2월 12일에 '소송이혼' 절차를 밟았으나 이후 이 소송을 취하하고 2009년 2월 18일 조정이혼으로 이혼이 완료되면서 '합의이혼'으로 마무리되었다.[4][5][6][7][8][9]

1991년 삼성전자에 입사하였고, 회사 임원으로 있으면서 미국과 일본에서 대학원 과정을 유학하고 돌아와 2001년 삼성전자 경영기획팀 상무보로 승진했고 2년 뒤인 2003년 삼성전자 경영기획팀 상무로 승진을 했으며 4년 뒤인 2007년 전무로 승진하면서 경영진으로 편입하였다.[9][10]
"""

if __name__ == "__main__":
    summary_template = """
        주어진 한 사람의 대한 정보 {information} 에 대해 다음 내용을 만들어 줘:
        1. 간단한 요약
        2. 그 사람에 대한 2개의 fun facts
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))

    print("hello LangChain!")
