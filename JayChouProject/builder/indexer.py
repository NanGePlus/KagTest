import os
import logging
from kag.builder.component.reader import DocxReader, PDFReader, MarkDownReader, CSVReader, TXTReader, JSONReader
from kag.builder.component.splitter import LengthSplitter
from knext.builder.builder_chain_abc import BuilderChainABC
from kag.builder.component.extractor import KAGExtractor
from kag.builder.component.vectorizer.batch_vectorizer import BatchVectorizer
from kag.builder.component.writer import KGWriter




# 初始化日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# 获取当前脚本所在的目录路径
file_path = os.path.dirname(__file__)

# 定义文件后缀与对应读取器类的映射，用于动态选择合适的读取器
suffix_mapping = {
    "docx": DocxReader,
    "pdf": PDFReader,
    "md": MarkDownReader,
    "csv": CSVReader,
    "txt": TXTReader,
    "json": JSONReader
}

class KagDemoBuildChain(BuilderChainABC):
    def build(self, **kwargs):
        try:
            # 1、定义文件读取 读取文件内容
            file_path = kwargs.get("file_path")
            if not os.path.exists(file_path):
                logging.error(f"File not found: {file_path}")
                raise FileNotFoundError(f"The file {file_path} does not exist.")

            suffix = file_path.split(".")[-1]
            reader_class = suffix_mapping.get(suffix)
            if reader_class is None:
                logging.error(f"Unsupported file format: {suffix}")
                raise NotImplementedError(f"No reader implemented for file type: {suffix}")

            reader = reader_class()

            # 2、定义文本分割 切分为chunk
            project_id = os.getenv("KAG_PROJECT_ID")
            if project_id is None:
                logging.error("Environment variable KAG_PROJECT_ID is not set.")
                raise EnvironmentError("Missing environment variable: KAG_PROJECT_ID")

            project_id = int(project_id)
            splitter = LengthSplitter(split_length=800, window_length=100)

            # 3、定义知识提取 提取知识
            extractor = KAGExtractor(project_id=project_id)

            # 4、定义批量生成文本向量表示 将文本转化为向量
            vectorizer = BatchVectorizer()

            # 5、定义知识写入 将最终的知识数据写入向量数据库
            writer = KGWriter()

            # 6、将定义的各组件按顺序串联成构建索引的chain并返回
            chain = reader >> splitter >> extractor >> vectorizer >> writer
            return chain
        except Exception as e:
            logging.error(f"An error occurred during the build process: {e}")
            raise

# 构建知识图谱
def buildKG(test_file, **kwargs):
    try:
        if not os.path.exists(test_file):
            logging.error(f"File not found: {test_file}")
            raise FileNotFoundError(f"The file {test_file} does not exist.")

        # 创建 KagDemoBuildChain 对象，传入文件路径
        chain = KagDemoBuildChain(file_path=test_file)

        # 调用 chain.invoke 方法执行构建，设置并发任务数量为 10
        chain.invoke(test_file, max_workers=10)
    except FileNotFoundError as e:
        logging.error(f"File error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during the knowledge graph build process: {e}")

if __name__ == "__main__":
    try:
        # 文件输入
        test_file = os.path.join(file_path, "./data/jay.txt")

        # 构建知识图谱
        buildKG(test_file)
    except Exception as e:
        logging.critical(f"Critical error: {e}")
