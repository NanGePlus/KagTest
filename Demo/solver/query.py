import logging
import os

from kag.common.env import init_kag_config
from kag.solver.logic.solver_pipeline import SolverPipeline




logger = logging.getLogger(__name__)

class KagDemo:

    def __init__(self):
        pass

    def qa(self, query):
        # 创建一个 SolverPipeline 实例，负责查询的逻辑处理
        resp = SolverPipeline()
        answer, trace_log = resp.run(query)
        return answer,trace_log

if __name__ == "__main__":
    demo = KagDemo()
    query = "张三九的基本信息"
    answer,trace_log = demo.qa(query)

    print(f"answer:{answer}\ntraceLog:{trace_log}")
