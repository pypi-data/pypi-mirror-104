# zengxh_py_tools
python 开发过程中常用到的工具

### 生成发布软件包文件
```shell script
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
```

### 将打包好的项目上传至PyPI
```shell script
python -m pip install --user --upgrade twine
# upload to test PyPI
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# upload to real PyPI
python -m twine upload dist/*
```

### 测试是否发布成功
```shell script
# 在线安装测试版本
pip install -i https://test.pypi.org/simple/ zengxh_py_tools==0.0.2
# 在线安装正式版本
pip install -i https://pypi.org/simple/ zengxh_py_tools==0.0.2
pip install zengxh_py_tools==0.0.2
# 离线安装
pip install dist/zengxh_py_tools-0.0.1-py3-none-any.whl
pip uninstall zengxh_py_tools
```