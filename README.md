# pip批量安装第三方库

#### 介绍
批量安装python第三方库
本人将会不断的完善本项目
#### 软件架构
软件架构说明:
用os库执行os.system()方法，for循环遍历所有需要安装的库，传递给os.system()进行安装。
#### 安装教程

建议在cmd命令窗口以管理员权限运行文件：Install-third-party-library.py
也可以在编辑器里执行

#### 使用说明
1.先安装os库,否则无法执行:
    pip install os
2.pip 安装有一定的失败概率，如果无法用pip 安装请先去下载.whl文件再进行pip离线安装
安装方法：
首先在线搜索并下载你需要的第三方库：网址https://pypi.org/project/
安装whl包： pip install  **.whl（前提是要安装好pip和wheel）
安装tar.gz包：cd到解压后路径,python setup.py install（安装pip和wheel都可以参照这种方法）