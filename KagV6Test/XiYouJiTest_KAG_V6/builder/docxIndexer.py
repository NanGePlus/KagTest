import logging
from pathlib import Path
from kag.builder.runner import BuilderChainRunner
from kag.common.conf import KAG_CONFIG

logger = logging.getLogger(__name__)

# 索引构建
def buildKB(files_dir):
    runner = BuilderChainRunner.from_config(
        KAG_CONFIG.all_config["docx_kag_builder_pipeline"]
    )
    runner.invoke(files_dir)
    logger.info(f"\n\nbuildKB successfully for {files_dir}\n\n")



if __name__ == "__main__":
    # 获取当前位置路径 并指定文件目录
    current_dir = Path(__file__).parent
    files_dir = current_dir / "data/inputs/file2.docx"

    buildKB(str(files_dir))

