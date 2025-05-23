# 番茄投屏
|![qq群](asset/qq_code.png)|![微信群](asset/qr_code.png)|
|---------------------------|----------------------------------|

  
**实现浏览器控制安卓手机，投屏延迟低至30ms。基于scrcpy3.2，主要功能如下:**
- 权限管理(基于角色权限控制：删除/增加/编辑/投屏/文件管理/shell/应用管理等权限)
- 手机分配(限时：限定给用户分配手机，到期后收回分配)
- 分组管理(不限时：将分组内的所有手机授予用户)
- 列表投屏
- 无线投屏
- 摄像头投屏
- 音频播放
- shell命令行
- 文件管理
- 应用管理
- 录屏播放
- 键盘直连输入
- 视频`码率/编码器/帧率/尺寸`调整
- 音频`码率/编码器`调整
- ...

## 一.下载&使用
### 下载
- lite版本：[番茄投屏lite.exe](../../releases/latest)
- pro版本：敬请期待...

### 使用
1. 配置好adb和手机，adb devices能看到手机列表。[adb配置文档](docs%2Fadb%2Fadb%E6%96%87%E6%A1%A3.md)
2. 点击 `exe`后，浏览器访问 `http://127.0.0.1:8888/` 管理员admin/123456
3. 页面打开 `设备管理>手机`进行手机投屏，若无设备请点击`发现`按钮
4. 杀毒软件若误报病毒，请关闭杀毒软件后再执行
5. 局域网/互联网若无法投屏，请看下面[webcodecs](#%E4%B8%89webcodecs)的关闭chrome浏览器安全限制

## 二.功能截图
### 1.登录页
![0](asset/0.png)
### 2.基础管理
![1](asset/1.png)
![1](asset/1-1.png)
### 3.视图列表页【pro版本】
![2](asset/2.png)
### 4.普通列表页
![3](asset/3.png)
### 5.详情页-配置
![4](asset/4.png)
![4](asset/4-1.png)
![4](asset/4-2.png)
### 6.详情页-命令行【pro版本】
![5](asset/5.png)
### 7.详情页-文件管理【pro版本】
![6](asset/6.png)
![6](asset/6-1.png)
![6](asset/6-2.png)
### 8.详情页-录屏管理【pro版本】
![7](asset/7.png)
![7](asset/7-1.png)
### 9.详情页-应用管理【pro版本】
![8](asset/8.png)
### 10.手机分组管理
![9](asset/9.png)
### 11.手机分配【pro版本】
![10](asset/10.png)
![10](asset/10-1.png)



## 三.webcodecs
由于浏览器安全限制，投屏播放器需要在`https`或者`本地`访问才能使用。  
### 1.chrome关闭特定网址安全限制
浏览器输入 `chrome://flags`
![image](asset/chrome.png)
在`Insecure origins treated as secure`中加入需要关闭安全限制站点，逗号分隔。配置好后选择`启用`, 点击`重启`就可以了

## 四.常用配置
### 1.环境变量
> ***计算机(右键) >属性 >高级系统设置 >环境变量***,  设置完重启软件
![other_env.png](asset%2Fother_env.png)
- ***TOMATO_SERVER_PORT*** 配置服务端口，默认8888  
### 2.配置表
> ***系统管理 >配置管理***, 设置完重启软件
> 
![other_config.png](asset%2Fother_config.png)
### 3.投屏参数配置
> 详见：[投屏参数.py](%E6%8A%95%E5%B1%8F%E5%8F%82%E6%95%B0.py)
### 4.管理员创建/密码重置
![other_cmd_user.png](asset%2Fother_cmd_user.png)
#### (1) 管理员创建：使用命令行直接创建管理员
`tomato.exe create_superuser:admin`
#### (2) 用户密码重置：使用命令行直接重置密码(当忘记密码时)
`tomato.exe reset_passwd:admin`
#### (3) 重置菜单
`tomato.exe reset_menu`