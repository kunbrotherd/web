import os
import time

import pytest
if __name__ == '__main__':

    pytest.main()
    time.sleep(3)
    # 将temps文件里的json文件报告，编辑输出为HTML格式报告存到reports文间里，每生成一次清理一次
    os.system("allure generate ./temps -o ./reports --clean")
