# Django 基础教程 - Django 模板

*通过简单的示例来说明 Django 模板的相关用法*

- Django 模板系统基础
- 使用 Django 模板的步骤

### 1、什么是 Django 模板基础
Django 模板是一些文本字符串，作用就是把文档的表现和数据分开。模板定义一些占位符和基本的逻辑，规定如何显示文档。通常，模板用于生成 HTML， 不过 Django 模板可以生成任何基于文本的格式。

*模板系统的设计目的主要是呈现表现，而不是程序逻辑*


    `基础模板示例
    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/html">
    <head>
        <meta charset="UTF-8">
        <title>Ordering notice</title>
    </head>
    <body>
    <h1>Ordering notice</h1>
    <p>Dear {{ person_name }}</p>

    <p>Thanks for placing an order from {{ company }}, It's scheduled to ship on {{ ship_date| date:"F j, Y" }}.</p>

    <p>Here are the items you've ordered:</p>

    <ul>
        {% for item in item_list %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>

    {% if ordered_warranty %}
        <p>Your warranty information will be included in the plackaging.</p>
    {% else %}
        <p>You didn't order a warrant, so you're on your own when the products inevitably stop working.</p>
    {% endif %}

    <p>Sincerely, <br/>{{ company }}</p>
    </body>
    </html>`
    
### 2、Django 模板的使用步骤
Django 自带一个内置的后端，用于支持自身模板引擎， 名称为： Django Template Lanage（DTL）
使用步骤如下：
  - 2.1.以字符串的形式提供原始的模板代码，创建 Template 对象。
  - 2.2.在 Template 对象上调用 render() 方法， 传入一系列变量，返回的是完全渲染模板后得到的字符串，模板中的变量和模板中的标签已经根据上下文对象得到结果。


    `from django import template`
    
    `t = template.Template("My name is {{ name }}.")`
    
    `c = template.Context({"name":"Simplation"})`
    
    `print(t.render(c))`
    
    `My name is Simplation. # 输出的结果`
  
  
  
  
