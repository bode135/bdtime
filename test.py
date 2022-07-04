from bdtime import version, tt


if __name__ == '__main__':
    print("--- bdtime version:", version())

    # 默认保留2位小数
    ret = tt.get_current_beijing_time_str()
    print(ret)

    # 这个适合做临时文件的文件名后缀
    # ret = tt.get_current_beijing_time_str(tt.common_date_time_formats.ms_int)
    # print(ret)


