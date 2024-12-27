import os
from kag.builder.component.reader import DocxReader, PDFReader, MarkDownReader
from kag.builder.component.splitter import LengthSplitter, OutlineSplitter
from knext.builder.builder_chain_abc import BuilderChainABC
from kag.builder.component.extractor import KAGExtractor
from kag.builder.component.vectorizer.batch_vectorizer import BatchVectorizer
from kag.builder.component.writer import KGWriter
from kag.solver.logic.solver_pipeline import SolverPipeline
import logging
from kag.common.env import init_kag_config




# 获取当前脚本所在的目录路径
file_path = os.path.dirname(__file__)

# 定义文件后缀与对应读取器类的映射，用于动态选择合适的读取器
suffix_mapping = {
    "docx": DocxReader,
    "pdf": PDFReader,
    "md": MarkDownReader
}


class KagDemoBuildChain(BuilderChainABC):
    def build(self, **kwargs):
        # 获取文件路径
        file_path = kwargs.get("file_path", "a.docx")
        # 根据文件后缀从suffix_mapping中选择合适的读取器
        suffix = file_path.split(".")[-1]
        reader = suffix_mapping[suffix]()
        # 若未实现某种格式的读取器，则抛出 NotImplementedError
        if reader is None:
            raise NotImplementedError

        # 项目ID
        project_id = int(os.getenv("KAG_PROJECT_ID"))
        # 将文本切分为长度为 2000 的块
        splitter = LengthSplitter(split_length=2000)
        # 将文本数据转化为向量
        vectorizer = BatchVectorizer()
        # 提取知识的核心组件，使用环境变量 KAG_PROJECT_ID 指定项目 ID
        extractor = KAGExtractor(project_id=project_id)
        # 将最终的知识数据写入输出
        writer = KGWriter()
        # 各组件按顺序串联成构建chain
        chain = reader >> splitter >> extractor >> vectorizer >> writer
        # 返回chain
        return chain


# 构建知识图谱
def buildKG(test_file, **kwargs):
    # 创建 KagDemoBuildChain 对象，传入文件路径
    chain = KagDemoBuildChain(file_path=test_file)
    # 调用 chain.invoke 方法执行构建，设置并发任务数量为 10
    chain.invoke(test_file, max_workers=10)


if __name__ == "__main__":
    # 文件输入
    test_file = os.path.join(file_path, "./data/健康档案.pdf")
    # 构建知识图谱
    buildKG(test_file)



