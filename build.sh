echo "运行容器python执行自动化"
#-w=$WORKSPACE：指定workspace
#--volumes-from=jenkins_save01：将jenkins容器中的workspace映射到python容器中，此时jenkins中git拉下来的代码就会被映射进去
#docker run --rm -w=$WORKSPACE --volumes-from=jenkins python:lpq
docker run -dit --name python --network=host -v /usr/bin/python3:/usr/bin/python3 -v /usr/local/jenkins:/var/jenkins_home -w=$WORKSPACE python:lpq bash

#python3 run_cmd.py
echo "python执行自动化执行成功"