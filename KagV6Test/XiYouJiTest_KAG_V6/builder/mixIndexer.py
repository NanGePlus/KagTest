import os
import logging
from pathlib import Path
from kag.builder.runner import BuilderChainRunner
from kag.common.conf import KAG_CONFIG



logger = logging.getLogger(__name__)

# 针对TXT文件进行索引构建
def buildMdKB(dir_path):
    try:
        runner = BuilderChainRunner.from_config(
            KAG_CONFIG.all_config.get("md_kag_builder_pipeline")
        )
        if runner is None:
            raise ValueError("Missing 'md_kag_builder_pipeline' configuration.")
        runner.invoke(dir_path)
        logger.info(f"\n\nbuildMdKB successfully for {dir_path}\n\n")
    except Exception as e:
        logger.error(f"Error building MD KB for {dir_path}: {e}")

# 针对DOCX文件进行索引构建
def buildDocxKB(dir_path):
    try:
        runner = BuilderChainRunner.from_config(
            KAG_CONFIG.all_config.get("docx_kag_builder_pipeline")
        )
        if runner is None:
            raise ValueError("Missing 'docx_kag_builder_pipeline' configuration.")
        runner.invoke(dir_path)
        logger.info(f"\n\nbuildDocxKB successfully for {dir_path}\n\n")
    except Exception as e:
        logger.error(f"Error building DOCX KB for {dir_path}: {e}")

# 针对PDF文件进行索引构建
def buildPdfKB(dir_path):
    try:
        runner = BuilderChainRunner.from_config(
            KAG_CONFIG.all_config.get("pdf_kag_builder_pipeline")
        )
        if runner is None:
            raise ValueError("Missing 'pdf_kag_builder_pipeline' configuration.")
        runner.invoke(dir_path)
        logger.info(f"\n\nbuildPdfKB successfully for {dir_path}\n\n")
    except Exception as e:
        logger.error(f"Error building PDF KB for {dir_path}: {e}")

# 索引构建分诊
def process_files(files_dir):
    if not isinstance(files_dir, Path):
        logger.error("Invalid files_dir parameter. Expected a Path object.")
        return

    if not files_dir.exists() or not files_dir.is_dir():
        logger.error(f"Directory {files_dir} does not exist or is not a directory.")
        return

    for file_path in files_dir.iterdir():  # 遍历文件夹中的所有文件和子目录
        if file_path.is_file():  # 确保是文件
            try:
                logger.info(f"Processing file: {file_path}")
                # 根据扩展名和文件名前缀判断类型
                if file_path.suffix == ".md" and file_path.name.startswith("file"):
                    buildMdKB(str(file_path))
                elif file_path.suffix == ".docx" and file_path.name.startswith("file"):
                    buildDocxKB(str(file_path))
                elif file_path.suffix == ".pdf" and file_path.name.startswith("file"):
                    buildPdfKB(str(file_path))
                else:
                    logger.warning(f"Skipped unsupported file type or invalid file: {file_path}")
            except Exception as e:
                logger.error(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        # 获取当前位置路径 并指定文件目录
        current_dir = Path(__file__).parent
        files_dir = current_dir / "data/incremental_inputs"

        # 检查目录是否存在并进行索引构建
        process_files(files_dir)
    except Exception as e:
        logger.critical(f"Unhandled exception in main: {e}")
