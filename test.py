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

    from bdtime import get_logger, get_all_loggers
    print(get_logger(name='haha'))
    print(get_logger(name='haha'))
    get_all_loggers()




