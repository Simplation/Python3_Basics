一、Flask 是一个 python web microframework。 

1、安装flask

```
pip3 install flask


返回

Collecting flask

  Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea9 /Flask-1.0.2-py2.py3-none-any.whl (91kB)

      100% |████████████████████████████████| 92kB 193kB/s


Collecting Werkzeug>=0.14 (from flask)   Downloading https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0 /Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)

      100% |████████████████████████████████| 327kB 533kB/s Collecting click>=5.1 (from flask)

   Downloading

https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1 /click-6.7-py2.py3-none-any.whl (71kB)

      100% |████████████████████████████████| 71kB 1.0MB/s Collecting itsdangerous>=0.24 (from flask)

   Downloading https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab /itsdangerous-0.24.tar.gz (46kB)

      100% |████████████████████████████████| 51kB 1.0MB/s Collecting Jinja2>=2.10 (from flask)

   Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76 /Jinja2-2.10-py2.py3-none-any.whl (126kB)

      100% |████████████████████████████████| 133kB 1.6MB/s Collecting MarkupSafe>=0.23 (from Jinja2>=2.10->flask)

   Downloading https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699a /MarkupSafe-1.0.tar.gz Installing collected packages: Werkzeug, click, itsdangerous, MarkupSafe, Jinja2, flask


   Running setup.py install for itsdangerous ... done

   Running setup.py install for MarkupSafe ... done Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-1.0.2 itsdangerous-0.24
```



2、最简单的flask运行

```
# FlaskTest.py

from flask import Flask

app = Flask(__name__)


@app.route(‘/‘)
def index():
     return ‘Hello, Flask!’

if __name__ == ‘__main__’:
     app.run(debug=True)            # 使用 Flask 自带的服务器

运行 FlaskTest.py, 浏览器访问：http://127.0.1.5000， 就能看到网页显示’Hello, Flask!’。
```



HTTP 方法

| Http方法 | 行为           |
| -------- | -------------- |
| GET      | 获取资源的信息 |
| POST     | 创建新资源     |
| PUT      | 更新资源       |
| DELETE   | 删除资源       |

3、flask 简单演示

flask 功能强大，演示常用的 http 方法，结合 MySQL 数据库连接



3.1、最简单的 flask 应用

```
from flask import Flask

app = Flask(__name__)

@app.route(‘/‘)                                # 最简单的路由
def index():
     return ‘Hello Flask’

if __name__ == ‘__main__’:
     # 使用 Flask 自带的服务器 默认端口是5000
     app.run(port=5000, debug=True) 
```



3.2、GET 请求方式 ———> Flask 默认的是Get请求方式

```
from flask import Flask, request

app = Flask(__name__)

@app.route(‘/‘)
def index():
     return ‘Hello Flask’


# GET 不带参数
@app.route(‘/user’, methods=[‘GET'])        # 可以通过 methods 直接使用声明请求方式，也可以不声明，默认请求方式是 GET

def user():
     return ‘Hello user’ 

# GET 携带参数
@app.route(‘/user/<user_id>’)
def user(user_id):
	 return ‘Hello, User ‘ + user_id

if __name__ == ‘__main__’:
     # 使用 Flask 自带的服务器 默认端口是5000
     app.run(port=5000, debug=True) 
```



3.3、POST 请求方式 

```
from flask import Flask

app = Flask(__name__)

@app.route(‘/‘)
def index():
     return ‘Hello Flask’


@app.route(‘/get_user’, methods=[‘POST’])   # 通过 methods 方式声明请求方式
def get_user():
     return ‘Hello get_user'

if __name__ == ‘__main__’:
     # 使用 Flask 自带的服务器 默认端口是5000
     app.run(port=5000, debug=True) 
```



3.4、PUT 请求方式

```
from flask import Flask

app = Flask(__name__)

@app.route(‘/put_method’, methods=[‘DELETE'])
def put_method():
     return ‘put_method’


if __name__ == ‘__main__’:
     app.run(port=5000, debug=True)
```



3.5、DELETE 请求方式

```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route(‘/delete_method’, methods=[‘DELETE’])
def delete_method():
     return jsonify({‘code’:200})

if __name__ == ‘__main__’:
     app.run(port=5000, debug=True)
```



🌟🌟🌟🌟🌟

二、对 GET 和 POST 请求的封装实现

```
#!/usr/bin/env python
# encoding: utf-8
# 在 class 中封装网络请求 

import requests
import json 

# GET 方式
def get(url, params, headers):
      try:
          r = requests.get(url, params=params, headers=headers)
          print("获取返回的状态码", r.status_code)

          json_r = r.json()
          print("json类型转化成python数据类型", json_r)
      except BaseException as e:
          print("请求失败！", str(e))


# POST 方式 # key：value
def post(url, params, headers):
      try:
          r = requests.post(url, data=params, headers=headers)
          print("获取返回的状态码", r.status_code)

          json_r = r.json()
          print("json类型转化成python数据类型", json_r)

      except BaseException as e:
          print("请求失败！", str(e)) 


# POST 方式  #json

def post_json(url, para, headers):
      try:
          data = para
          data = json.dumps(data)

          # python数据类型转化为json数据类型
          r = requests.post(url, data=data, headers=headers)
          print("获取返回的状态码", r.status_code)

          json_r = r.json()
          print("json类型转化成python数据类型", json_r)

      except BaseException as e:
          print("请求失败！", str(e))



用法

#!/usr/bin/env python
# encoding: utf-8 
# 在 class 中封装网络请求 

from Test import HttpRequest                                         # 进行导入封装的文件

url = '<http://www.artlifeserver.cn/rent/api/login.php>’               # 初始化 URL

params = {"tel":"15934866270", "pwd":"123456”}                       # 初始化参数
headers = {} 

HttpRequest.get(url, params, headers)                                # GET 方式
HttpRequest.post(url, params, headers)                               # POST 方式
HttpRequest.post_json(url, params, headers)                          # POST_JSON 方式
```











