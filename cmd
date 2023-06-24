https://httprunner.com/docs/user-guide/enhance-tests/
配置环境
首次以管理员执行 hrp startproject 命令，会自动配置venv虚拟环境, 后续执行即可初始化指定名称的项目工程。
hrp startproject demo

pip install --target=path_name package_name命令，将package_name安装到path_name
pip install allure-pytest --target=C:\Users\Administrator\.hrp\venv\Lib\site-packages -i https://pypi.tuna.tsinghua.edu.cn/simple

查看pip install 安装的某个包的路径
可以使用pip uninstall package-name命令，此时终端会报出该包的安装路径，并问是否确认卸载，选择不卸载即可

转换生成测试用例
hrp convert .\har\popup.har .\har\popup2.har --to-yaml -d .\testcases

# 将输入的 demo.har 转化为 json 测试用例 demo_test.json，并进行全局替换
$ hrp convert demo.har --profile profile.yaml

# 将输入的 demo.har 转化为 pytest 测试用例 demo_test.py，并进行全局覆盖
$ hrp convert demo.har --to-pytest --profile profile_override.yaml

运行接口测试
hrp run .\testcases\reciveReward_test.yaml -c -g -p http://localhost:8888

运行性能测试
hrp boom testcases/demo_requests.yml --spawn-count 100 --spawn-rate 10 --loop-count 1000
在该示例中，我们指定了 100 个并发用户，按照每秒 100 个的速率初始化用户，预计在 10s 后可完成初始化。
每个用户循序运行 1000 次，预计总共运行 100*1000=10w 次。

Flags:
  -c, --continue-on-failure   continue running next step when failure occurs
  -g, --gen-html-report       generate html report
  -h, --help                  help for run
      --http-stat             turn on HTTP latency stat (DNSLookup, TCP Connection, etc.)
      --log-plugin            turn on plugin logging
      --log-requests-off      turn off request & response details logging
  -p, --proxy-url string      set proxy url
  -s, --save-tests            save tests summary

Global Flags:
      --log-json           set log to json format
  -l, --log-level string   set log level (default "INFO")