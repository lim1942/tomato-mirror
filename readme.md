![banner.jpg](asset%2Findex%2Fbanner.jpg)
# 番茄投屏
|![qq群](asset/qq_code.png)|![微信群](asset/qr_code.png)|
|---------------------------|----------------------------------|

  
**实现浏览器控制安卓手机，投屏延迟低至30ms。主要功能如下:**  
- [x] 权限管理(基于角色权限控制：删除/增加/编辑/投屏/文件管理/shell/应用管理等权限)
- [x] 手机分配(限时：限定给用户分配手机，到期后收回分配)
- [x] 分组管理(不限时：将分组内的所有手机授予用户)
- [x] 列表投屏
- [x] 无线投屏
- [x] 摄像头投屏
- [x] 音频播放
- [x] adb命令行
- [x] 文件管理
- [x] 应用管理
- [x] 录屏播放
- [x] 键盘直连输入
- [x] 视频`码率/编码器/帧率/尺寸`调整
- [x] 音频`码率/编码器`调整
- [ ] 手机访问投屏: 开发中

## 一.下载
### 1.lite版本
> 功能截图：[用户管理，手机分组管理](lite.md)  
> 下载地址：[番茄投屏lite.exe](../../releases/latest)
### 2.pro版本(群控版本)
> 功能截图：[手机群控，手机限时分配，文件管理，adb命令行，手机录屏，应用管理...](pro.md)  
> 下载地址：`请加qq交流群(957034905)联系群主`

## 二. 使用教程
> [演示视频](https://www.bilibili.com/video/BV1sgJTztE14/)
1. 配置好adb和手机，adb devices能看到手机列表。[adb配置文档](docs%2Fadb%2Fadb%E6%96%87%E6%A1%A3.md)
2. 点击 `exe`后，浏览器访问 `http://127.0.0.1:8888/` 管理员admin/123456
3. 页面打开 `设备管理>手机`进行手机投屏，若无设备请点击`发现`按钮
4. 杀毒软件若误报病毒，请关闭杀毒软件后再执行
5. 局域网/互联网若无法投屏，请看下面[webcodecs](#%E4%B8%89webcodecs)的关闭chrome浏览器安全限制



## 三.chrome播放配置
由于浏览器安全限制，需要域名为`https`或者`本地`访问才能投屏播放。  
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