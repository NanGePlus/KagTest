import os
import logging
from kag.common.registry import import_modules_from_path
from kag.builder.runner import BuilderChainRunner

logger = logging.getLogger(__name__)


def buildKB(dir_path):
    from kag.common.conf import KAG_CONFIG

    runner = BuilderChainRunner.from_config(
        KAG_CONFIG.all_config["kag_builder_pipeline"]
    )
    runner.invoke(dir_path)

    logger.info(f"\n\nbuildKB successfully for {dir_path}\n\n")


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.abspath(__file__))
    import_modules_from_path(dir_path)

    data_dir_path = os.path.join(dir_path, "data/jay.txt")
    buildKB(data_dir_path)