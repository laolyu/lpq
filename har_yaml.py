# coding:utf-8
import os

# 定义要遍历的文件夹路径
folder_path = r'har'


# 遍历指定文件夹及子文件夹下所有文件
def traverse_folder(path):
    file_list = os.listdir(path)
    s = ''
    for file_name in file_list:
        full_path = os.path.join(path, file_name)
        if os.path.isdir(full_path):
            s += traverse_folder(full_path)
        elif file_name.endswith('.har'):
            # print(full_path)
            s += full_path + ' '
    # print(s)
    return s


hars = traverse_folder(folder_path)  # 调用遍历函数
cmd = f'hrp convert {hars}--to-yaml -d ./testcases'
# print(cmd)
os.system(cmd)
