from bdtime import version, tt
from bdtime.get_cpu_info import main as get_cpu_info


if __name__ == '__main__':
    # CPU相关
    print("--- bdtime version:", version())

    get_cpu_info()

    # --- 日期时间相关
    # tt.set_default_decimal_places(0)            # 全局设置默认保留多少位小数
    current_beijing_time_str = tt.get_current_beijing_time_str()
    print(f"*** current_beijing_time_str: [{current_beijing_time_str}]")

    # 这个适合做临时文件的文件名后缀
    ret = tt.get_current_beijing_time_str(tt.common_date_time_formats.s_int)
    print(f"时间编号: {ret}")

    # --- package 的版本控制
    from bdtime import show_all_loggers, version, package_version_utils

    package_name = 'bdtime'
    # current_version = get_current_version(package_name)
    current_version = version()
    last_version = package_version_utils.get_latest_version(package_name)
    # print(package_version_utils.compare_version(current_version, last_version))
    _, _, _, msg = package_version_utils.check_version_by_package_name('bdtime')
    print(f"check_version_by_package_name msg: {msg}")
    # show_all_loggers()




