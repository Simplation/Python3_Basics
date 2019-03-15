# Flask 的使用

1、安装：

    pip install flask

2、导入：

    from flask import Flask, render_template
    
3、编写程序

    # 导入库文件
    from flask import Flask
    
    app = Flask(__name__)
   
   
    # 编写路由
    @app.route('/user_hello')
    def user_hello():
        # 调用本地 h5 页面
        return render_template('index.html')
    
    
    if __name__ == "__main__":
        # 指定模式和端口号
        app.run(debug=True, port=8866)
