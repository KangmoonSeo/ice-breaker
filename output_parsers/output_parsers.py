from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

"""
pydantic 이란 무엇인가?
파이썬의 내장 데이터 클래스와 매우 유사하지만, 실은 외부 라이브러리
데이터 유효성 검사와 설정 관리에 유용함
"""

from typing import List


class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Interesting facts about the person")
    topics_of_interest: List[str] = Field(
        description="Topics that may interest the person"
    )
    ice_breakers: List[str] = Field(
        description="Create ice breakers to open a conversation"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers,
        }


"""
input_parser를 추후에 프롬프트 템플릿에 연결함
프롬프트 템플릿을 만들 때마다 아웃풋 파서에 연결하여
LLM에게 어떻게 답변을 돌려받을 지 명령하게 됨
json, xml, yaml? 
"""
person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
