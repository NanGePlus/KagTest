import os
from kag.common.env import init_kag_config
from kag.solver.logic.solver_pipeline import SolverPipeline



# 定义了一个封装问答系统功能的类 提供问答功能的接口
class SolverDemo:
    # 确保问答系统在使用前正确初始化
    def __init__(self, configFilePath):
        self.configFilePath = configFilePath
        init_kag_config(self.configFilePath)


    # 执行问答，使用 SolverPipeline 类的实例 resp 处理查询，并返回答案和跟踪日志
    def qa(self, query):
        resp = SolverPipeline(max_run=2)
        answer, trace_log = resp.run(query)
        # print(f"\n\nso the answer for '{query}' is: {answer}\n\n")
        return answer, trace_log



if __name__ == "__main__":
    configFilePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../kag_config.cfg")

    demo = SolverDemo(configFilePath=configFilePath)
    query = "周杰伦出生日期？"

    answer, trace_log = demo.qa(query)

    print(f"answer:\n{answer}\n\ntraceLog:\n{trace_log}")
