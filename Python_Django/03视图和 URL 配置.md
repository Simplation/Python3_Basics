# Django 基础教程

## 视图和 URL 配置

*通过一个简单的例子，来说明视图和 URL 的配置.*

- 视图
- URL配置
- 定义项目：python manage.py runserver

### 1、第一个 Django 页面： Hello World

- 1.1、第一个视图

  ```
  from django.shortcuts import render
  from django.http.response import HttpResponse
  
  # Create your views here.
  
  def hello(request):
      return HttpResponse('Hello World.')
  ```

- 1.2、第一个 URL 配置

  ```
  """my_blog URL Configuration

  The `urlpatterns` list routes URLs to views. For more information please see:
      https://docs.djangoproject.com/en/2.1/topics/http/urls/
  Examples:
  Function views
      1. Add an import:  from my_app import views
      2. Add a URL to urlpatterns:  path('', views.home, name='home')
  Class-based views
      1. Add an import:  from other_app.views import Home
      2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
  Including another URLconf
      1. Import the include() function: from django.urls import include, path
      2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
  """
  from django.contrib import admin
  from django.urls import path, include

  // 导入上边定义的 view
  from blog import views as v

  urlpatterns = [
      # Admin 账户的地址
      path('admin/', admin.site.urls),
    
      # 引入 view 中定义的函数
      path('hello/', v.hello),
  ]
  ```

- 1.3、运行项目 `python manage.py runserver`

  等待项目运行起来之后，不指定 IP 和 Port， 默认的是 127.0.0.1:8000。

  当然你也可以在后边指定 IP 和 Port： `python manage.py runserver 127.0.0.1:8088`

  如果不指定刚才定义的 URL 的话，页面显示的依旧是 Django 的欢迎页，需要访问的链接是：127.0.0.2:8000/hello/，这样页面就会显示刚才 View 定义的 Hello World. 
  
  运行成功的页面如下图所示：
  
  ![视图和 URL 配置](https://github.com/Simplation/Python3_Basics/blob/master/assets/%E8%A7%86%E5%9B%BE%E5%92%8C%20URL%20%E9%85%8D%E7%BD%AE.png)
