# TeacherManagement
---
## 2016 HIT CS&E Software Engineering Project
---

### 1. 环境说明
Python 版本2.7.12
Django 版本1.10

### 2. 相关说明
* 前端使用开源模板Matrix Admin，稍作改动

* 除了注册与登录模块，其他模块全部使用Class Based-On Views ，简称CBV开发，共有以下模块：

> * authentication，负责用户注册、登录、信息更新、个人信息查看
> * notification，负责显示用户的未读消息（教师信息更新+预约进度更新）。通知模块仅针对学生开发，尽管教师用户同样有这一外键，但并不显示在前端并永远为0

> * appointment，负责教师处理预约和设置闲置时间，学生预约教师并查看教师列表；负责为双方显示对方个人信息

> * link，友情链接，没有做后台的管理，添加友情链接直接在django的admin site处理

> * website，负责页面母版的渲染、首页和FrontMixin的多继承处理

### 3、鸣谢
[CommunityManagement](https://github.com/yumendy/CommunityManagement)

这是一只有故事的喵，你可以去他的博客[听雨轩](http://yumendy.com)投喂他

### 4、后续开发
* MySQL接入

* 教师闲置时间的UX优化
