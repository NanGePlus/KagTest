# -*- coding: utf-8 -*-
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

import json
from typing import List

from kag.interface import PromptABC


@PromptABC.register("jaychou_std")
class OpenIEEntitystandardizationdPrompt(PromptABC):
    template_zh = """
    {
        "instruction": "input字段包含用户提供的上下文。命名实体字段包含从上下文中提取的命名实体，这些可能是含义不明的缩写、别名或俚语。为了消除歧义，请尝试根据上下文和您自己的知识提供这些实体的官方名称。请注意，具有相同含义的实体只能有一个官方名称。请按照提供的示例中的输出字段格式，以单个JSONArray字符串形式回复，无需任何解释。",
        "example": {
            "input": "周杰伦（Jay Chou），1979年1月18日出生于台湾省新北市，祖籍福建省永春县，华语流行乐男歌手、音乐人、演员、导演、编剧，毕业于淡江中学。\n2000年，发行个人首张音乐专辑《Jay》。2001年，凭借专辑《范特西》奠定其融合中西方音乐的风格。2002年，举行“The One”世界巡回演唱会。2005年，主演个人首部电影《头文字D》，并凭借该片获得第25届香港电影金像奖和第42届台湾电影金马奖的最佳新演员奖。2006年起，连续三年获得世界音乐大奖中国区最畅销艺人奖。",
            "named_entities": [
                            {"name": "周杰伦","category": "Person","description": "周杰伦（Jay Chou）是一位华语流行乐男歌手、音乐人、演员、导演和编剧。"},
                            {"name": "音乐人","category": "Roles","description": "周杰伦（Jay Chou）是一位音乐人。"},
                            {"name": "1979年1月18日","category": "Date","description": "周杰伦（Jay Chou）在1979年1月18日出生。"}, 
                            {"name": "台湾省新北市","category": "GeographicLocation","description": "周杰伦出生在台湾省新北市。"}, 
                            {"name": "福建省永春县","category": "GeographicLocation","description": "周杰伦的祖籍在福建省永春县。"}, 
                            {"name": "淡江中学","category": "Organization","description": "周杰伦毕业于淡江中学。"},
                            {"name": "专辑《Jay》","category": "Albums","description": "专辑《Jay》是周杰伦2000年发行个人首张音乐专辑。"},
                            {"name": "《头文字D》","category": "Works","description": "《头文字D》是周杰伦2005年主演个人首部电影。"},
                            {"name": "金像奖","category": "Awards","description": "2005年，凭借《头文字D》获得第25届香港电影金像奖。"},
                            {"name": "金马奖","category": "Awards","description": "2005年，凭借《头文字D》获得第42届台湾电影金马奖。"},
                        ],
            "output": [
                    {"name": "周杰伦","category": "Person","description": "周杰伦（Jay Chou）是一位华语流行乐男歌手、音乐人、演员、导演和编剧。","official_name": "Jay Chou"},
                    {"name": "音乐人","category": "Roles","description": "周杰伦（Jay Chou）是一位音乐人。","official_name": "音乐从业者"},
                    {"name": "1979年1月18日","category": "Date","description": "周杰伦（Jay Chou）在1979年1月18日出生。","official_name": "1979-01-18"}, 
                    {"name": "台湾省新北市","category": "GeographicLocation","description": "周杰伦出生在台湾省新北市。","official_name": "台湾新北"}, 
                    {"name": "福建省永春县","category": "GeographicLocation","description": "周杰伦的祖籍在福建省永春县。","official_name": "福建永春"}, 
                    {"name": "淡江中学","category": "Organization","description": "周杰伦毕业于淡江中学。","official_name": "淡江高级中学"},
                    {"name": "专辑《Jay》","category": "Albums","description": "专辑《Jay》是周杰伦2000年发行个人首张音乐专辑。","official_name": "专辑Jay"},
                    {"name": "《头文字D》","category": "Works","description": "《头文字D》是周杰伦2005年主演个人首部电影。","official_name": "头文字D"},
                    {"name": "金像奖","category": "Awards","description": "2005年，凭借《头文字D》获得第25届香港电影金像奖。","official_name": "香港电影金像奖"},
                    {"name": "金马奖","category": "Awards","description": "2005年，凭借《头文字D》获得第42届台湾电影金马奖。","official_name": "台湾电影金马奖"},
            ]
        },
        "input": $input,
        "named_entities": $named_entities,
    }    
        """

    template_en = template_zh

    @property
    def template_variables(self) -> List[str]:
        return ["input", "named_entities"]

    def parse_response(self, response: str, **kwargs):
        rsp = response
        if isinstance(rsp, str):
            rsp = json.loads(rsp)
        if isinstance(rsp, dict) and "output" in rsp:
            rsp = rsp["output"]
        if isinstance(rsp, dict) and "named_entities" in rsp:
            standardized_entity = rsp["named_entities"]
        else:
            standardized_entity = rsp
        entities_with_offical_name = set()
        merged = []
        entities = kwargs.get("named_entities", [])
        for entity in standardized_entity:
            merged.append(entity)
            entities_with_offical_name.add(entity["name"])
        # in case llm ignores some entities
        for entity in entities:
            if entity["name"] not in entities_with_offical_name:
                entity["official_name"] = entity["name"]
                merged.append(entity)
        return merged
