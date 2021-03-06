# Django 基础教程 - 动态 URL
*使用正则来动态匹配 URL*

- Django 的处理请求过程
- 动态 URL 示例
- 开启服务， 访问地址


### 1、Django 的处理请求过程
- 1.1.请求 /hello/。
- 1.2.Django 查看 ROOT_URLCONF 设置，找到根 URL 配置。
- 1.3.Django 比较 URL 配置中的各个 URL 模式，找到与 /hello/ 匹配的那个。
- 1.4.如果找到匹配的模式，调用对应的视图函数。
- 1.5.视图函数返回一个 HttpResponse 对象。
- 1.6.Django 把 HttpResponse 对象转换成正确的 HTTP 响应，得到网页。

### 2、动态 URL 示例
- 2.1.在 views.py文件中编写如下代码
  
      from django.http import HttpResponse, Http404
      import datetime


      def hello(request):
        return HttpResponse("Hello world")


      def current_time(request):
        now = datetime.datetime.now()
        html = "It is now %s." % now
        return HttpResponse(html)
        
        
      def hours_ahead(request, offset):
          try:
              offset = int(offset)
          except ValueError:
              raise Http404

          dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
          html = 'In %s hours, it will be %s.' %(offset, dt)
          return HttpResponse(html)
       

- 2.2.配置 URL

      from django.conf.urls import path, re_path
      from django.conf.urls import url
      
      from django.contrib import admin
      from learning import views
      
      urlpatterns = [
        path('admin/', include(admin.site.urls)),
        path('hello/', views.hello),
        path('current_time/', views.current_time),
        
        # 以下两种方式支持正则： re_path() / url()，但是需要导入相应的包
        re_path(r'another_time/plus/(\d{1,2})/$', views.hours_ahead),
        url(r'another_time/plus/(\d{1,2})/$', views.hours_ahead),
      ]
      
### 3、开启服务，访问地址
请分别访问一下地址, 进行相应的测试(注意：必须开启服务，否则无法访问！！！)：

-  http://127.0.0.1:8000/current_time/
  
-  http://127.0.0.1:8000/another_time/plus/3/
  
-  http://127.0.0.1:8000/another_time/plus/5/
  

