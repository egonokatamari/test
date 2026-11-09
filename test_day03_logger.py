import yaml
from loguru import logger

def test_read_config_and_log():
    # 1.读取配置文件
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # 2.打印日志
    logger.info(f"当前测试环境:{config['env']}")
    logger.debug(f"准备连接数据库:{config['mysql']['host']}")

    assert config['mysql']['user'] == 'root'