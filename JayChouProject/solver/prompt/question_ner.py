# question_ner.py	对问题进行ner识别 作用范围 chunk检索
# 源码在 KAG/kag/solver/prompt/default



import json
from string import Template
from typing import List, Optional

from kag.common.base.prompt_op import PromptOp
from knext.schema.client import SchemaClient


class QuestionNER(PromptOp):

    template_zh = """
{
    "instruction": "你是命名实体识别的专家。请从输入中提取与模式定义匹配的实体。如果不存在该类型的实体，请返回一个空列表。请以JSON字符串格式回应。你可以参照example进行抽取。",
    "schema": $schema,
    "example": [
        {
            "input": "周杰伦（Jay Chou），1979年1月18日出生于台湾省新北市，祖籍福建省永春县，华语流行乐男歌手、音乐人、演员、导演、编剧，毕业于淡江中学。\n2000年，发行个人首张音乐专辑《Jay》。2001年，凭借专辑《范特西》奠定其融合中西方音乐的风格。2002年，举行“The One”世界巡回演唱会。2005年，主演个人首部电影《头文字D》，并凭借该片获得第25届香港电影金像奖和第42届台湾电影金马奖的最佳新演员奖。2006年起，连续三年获得世界音乐大奖中国区最畅销艺人奖。",
            "output": [
                    {"entity": "周杰伦","category": "Person","description": "周杰伦（Jay Chou）是一位华语流行乐男歌手、音乐人、演员、导演和编剧。"},
                    {"entity": "音乐人","category": "Roles","description": "周杰伦（Jay Chou）是一位音乐人。"},
                    {"entity": "1979年1月18日","category": "Date","description": "周杰伦（Jay Chou）在1979年1月18日出生。"}, 
                    {"entity": "台湾省新北市","category": "GeographicLocation","description": "周杰伦出生在台湾省新北市。"}, 
                    {"entity": "福建省永春县","category": "GeographicLocation","description": "周杰伦的祖籍在福建省永春县。"}, 
                    {"entity": "淡江中学","category": "Organization","description": "周杰伦毕业于淡江中学。"},
                    {"entity": "专辑《Jay》","category": "Albums","description": "专辑《Jay》是周杰伦2000年发行个人首张音乐专辑。"},
                    {"entity": "《头文字D》","category": "Works","description": "《头文字D》是周杰伦2005年主演个人首部电影。"},
                    {"entity": "金像奖","category": "Awards","description": "2005年，凭借《头文字D》获得第25届香港电影金像奖。"},
                    {"entity": "金马奖","category": "Awards","description": "2005年，凭借《头文字D》获得第42届台湾电影金马奖。"},
                ]
        }
    ],
    "input": "$input"
}    
    """

    template_en = template_zh

    def __init__(
            self, language: Optional[str] = "en", **kwargs
    ):
        super().__init__(language, **kwargs)
        self.schema = SchemaClient(project_id=self.project_id).extract_types()
        self.template = Template(self.template).safe_substitute(schema=self.schema)

    @property
    def template_variables(self) -> List[str]:
        return ["input"]

    def parse_response(self, response: str, **kwargs):
        rsp = response
        if isinstance(rsp, str):
            rsp = json.loads(rsp)
        if isinstance(rsp, dict) and "output" in rsp:
            rsp = rsp["output"]
        if isinstance(rsp, dict) and "named_entities" in rsp:
            entities = rsp["named_entities"]
        else:
            entities = rsp

        return entities
