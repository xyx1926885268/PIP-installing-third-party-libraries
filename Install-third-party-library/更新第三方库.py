import os
libs = ["basemap",'chardet','Cython','docutils','fs','h11','idna','importlib-metadata','kivy-deps.sdl2','matplotlib','mistune',
'numpy','numpy-quaternion','pathlib2','psygnal','pydantic','pymongo','pyshp','pytools','pywinpty','requests','rfc3986','six','sympy','turtle','urllib3']
try:
	for lib in libs:
		os.system("pip install --upgrade "+lib)
	print("安装成功")
except:
	print("安装失败")