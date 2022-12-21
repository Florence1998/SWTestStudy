import logging
# logging默认设置的级别是warning
# 设置成哪个级别，就会打印这个级别及以上的级别的日志
logging.basicConfig(level=logging.DEBUG)
logging.debug("这是debug日志")
logging.warning("Watch out!")
logging.info("I told you so")
logging.error("这是一条error级别的日志")