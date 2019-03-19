# Django 基础教程

## 动态视图和 URL

- Django 的处理请求过程
- 动态视图和 URL

### 1、Django 的处理请求过程
- 1.1.请求 /hello/。
- 1.2.Django 查看 ROOT_URLCONF 设置，找到根 URL 配置。
- 1.3.Django 比较 URL 配置中的各个 URL 模式，找到与 /hello/ 匹配的那个。
- 1.4.如果找到匹配的模式，调用对应的视图函数。
- 1.5.视图函数返回一个 HttpResponse 对象。
- 1.6.Django 把 HttpResponse 对象转换成正确的 HTTP 响应，得到网页。

### 2、动态视图和 URL
- 2.1.在 views.py文件中编写如下代码
  
      from django.http import HttpResponse
      import datetime

      def hello(request):
        return HttpResponse("Hello world")

      def current_datetime(request):
        now = datetime.datetime.now()
        html = "It is now %s." % now
        return HttpResponse(html)

- 2.2.配置 URL

      from django.conf.urls import include, url
      from django.contrib import admin
      from mysite.views import hello, current_datetime
      
      urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^hello/$', hello),
        url(r'^time/$', current_datetime),
      ]

