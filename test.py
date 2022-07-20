from bdtime import version, tt
from bdtime.get_cpu_info import main as get_cpu_info
from bdtime import log_config_dc
from bdtime import log as bd_log
import logging


if __name__ == '__main__':
    log = logging.getLogger("bdtime")
    # logging.basicConfig()
    # log.setLevel(logging.DEBUG)
    # bd_log.setLevel(logging.DEBUG)

    # logging.basicConfig(**log_config_dc.simple)
    logging.basicConfig(**log_config_dc.usual)
    # bd_log.setLevel(logging.WARNING)
    # logging.basicConfig(**log_config_dc.complex)


    # CPU相关
    log.info(f"--- bdtime version: {version()}")

    # get_cpu_info()

    # --- 日期时间相关
    # tt.set_default_decimal_places(0)            # 全局设置默认保留多少位小数
    current_beijing_time_str = tt.get_current_beijing_time_str()
    log.info(f"*** current_beijing_time_str: [{current_beijing_time_str}]")

    # 这个适合做临时文件的文件名后缀
    ret = tt.get_current_beijing_time_str(tt.common_date_time_formats.s_int)
    log.info(f"时间编号: {ret}")

    # --- package 的版本控制
    from bdtime import show_all_loggers, version, package_version_utils

    package_name = 'bdtime'
    # package_name = 'psutil'
    # current_version = get_current_version(package_name)
    current_version = version()
    last_version = package_version_utils.get_latest_version(package_name)
    # print(package_version_utils.compare_version(current_version, last_version))
    _, _, _, msg = package_version_utils.check_version_by_package_name(package_name)
    log.info(f"--- check_version_by_package_name: [{package_name}] --- msg: [{msg}]")
    # show_all_loggers()




