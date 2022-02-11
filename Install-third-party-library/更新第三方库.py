import os
libs = ["basemap",'chardet','Cython','docutils','fs','h11','idna','importlib-metadata','kivy-deps.sdl2','matplotlib','mistune',
'numpy','numpy-quaternion','pathlib2','psygnal','pydantic','pymongo','pyshp','pytools','pywinpty',
	'requests','rfc3986','six','sympy','turtle','urllib3']
#First, run the PIP list -o command under the CMD window to get the name of the library to libs after the update library is needed, and then execute.
#先在cmd窗口下运行pip list -o 命令，得到需要更新的库之后把库的名字添加到libs中，再执行。
try:
	for lib in libs:
		os.system("pip install --upgrade "+lib)
	print("安装成功")
except:
	print("安装失败")
