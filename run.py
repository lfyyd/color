import pytest
import os

if __name__ == '__main__':
    pytest.main(['-m','smoke'])

# if __name__ == '__main__':
#     pytest.main(['--alluredir','./color/test_file/allure_results'])
#     os.system('allure generate ./color/test_file/allure_results  -o ./color/test_file/reports' )

# 生成html报告，指定目录在前面加路径
# if __name__ == '__main__':
#     pytest.main(['--html=./po/test_file/sm.html'])

# 失败用例重跑两次
# if __name__ == '__main__':
#     pytest.main(['--reruns=2'])

# 运行指定的用例
# if __name__ == '__main__':
#     pytest.main(['./byhy/test_case1.py::test_01'])
