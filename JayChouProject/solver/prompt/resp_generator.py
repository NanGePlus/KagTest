# 根据已有信息生成最终答案
# 源码在 KAG/kag/solver/prompt/default


import re
from string import Template
from typing import List
import logging

from kag.common.base.prompt_op import PromptOp

logger = logging.getLogger(__name__)


class RespGenerator(PromptOp):
    template_zh = "基于给定的引用信息完整回答问题。" \
                  "\n给定的引用信息：'$memory'\n问题：'$instruction'"
    template_en = template_zh

    def __init__(self, language: str):
        super().__init__(language)

    @property
    def template_variables(self) -> List[str]:
        return ["memory", "instruction"]

    def parse_response(self, response: str, **kwargs):
        logger.debug('推理器判别:{}'.format(response))
        return response
