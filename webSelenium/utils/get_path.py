import os.path
import sys
from logging import Logger, StreamHandler

import yaml


def get_par_path():
    root_path = os.path.abspath(os.path.dirname(__file__)).split('utils')[0]
    return root_path


def get_yaml_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        file_data = f.read()
        data = yaml.load(file_data, yaml.FullLoader)
        return data


# class conf:
#     @staticmethod
#     def logcon():
#         log = Logger('测试日志')
#         StreamHandler(sys.stdout).push_application()
#         return log
