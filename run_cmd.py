# coding:utf-8
import os
import sys

sys.path.append(r'C:\air')
from pack import tk_1st

# cmd = r'hrp run .\testcases\withdraw_test.yaml -g'
cmd = r'hrp run .\testcases\withdraw_test.yaml -g -p http://localhost:8888 -c'

os.system(cmd)
tk_1st.show('run end')
