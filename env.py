# -*- coding: utf-8 -*-
# @Time    : 2023/11/18 10:42
# @Author  : nongbin
# @FileName: env.py
# @Software: PyCharm
# @Affiliation: tfswufe.edu.cn

import os

from dotenv import load_dotenv, dotenv_values

load_dotenv(".env", override=False)  # take environment variables from .env.
print(f"setting environment variables: {dotenv_values('.env')}")


def get_app_root():
    return os.getcwd()


def get_env_value(key):
    return os.environ.get(key)


if __name__ == '__main__':
    print(get_app_root())
    print(get_env_value('a71accd870b98b5497de4f69821ed80a.EerevZHJXou6DnN1'))
    # print(os.environ.get('PY_DEBUG'))
