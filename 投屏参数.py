DEFAULT_SCRCPY_KWARGS = {
    # 超时配置， 总超时时间 = mirror_retry * (mirror_timeout + mirror_retry_wait)
    # 投屏创建失败重试次数。(会覆盖配置表的MIRROR_RETRY)
    "mirror_retry": 5,
    # 投屏创建的超时时间(秒)，单次若超时还未成功直接停止开始下次 (会覆盖配置表的MIRROR_TIMEOUT)
    "mirror_timeout": 6,
    # 投屏创建失败后等待时间(秒),上次失败后可能需要等待一会开始下次重试 (会覆盖配置表的MIRROR_RETRY_WAIT)
    "mirror_retry_wait": 1,
    # uhid键盘鼠标是否打开
    "uhid_keyboard": False,
    "uhid_mouse": False,
    # 是否打开录屏
    "recorder_enable": False,
    # # 录屏文件封装格式，支持mp4和mkv两种类型
    "recorder_format": "mp4",
    # scrcpy adb-socket-id, 用于手机区分多个启动的scrcpy。每次运行自动生成
    "scid": -1,
    # scrcpy日志等级
    "log_level": "verbose",
    # 是否开启画面
    "video": True,
    # 是否开启声音
    "audio": True,
    # 视频编码类型，一般有h264,h265
    "video_codec": "h264",
    # 音频编码类型,一把有aac，opus
    "audio_codec": "aac",
    # 视频来源， 来源有屏幕display， 摄像头camera
    "video_source": 'display',
    # 声音来源，来源有喇叭output， 麦克风mic
    "audio_source": "output",
    # 投屏时，设备是否一直播放声音
    "audio_dup": True,
    # 画面最大尺寸
    "max_size": 720,
    # 视频比特率
    "video_bit_rate": 800000,
    # 音频比特率
    "audio_bit_rate": 128000,
    # 视频帧率
    "max_fps": 25,
    # 视频旋转角度
    'angle': '0',
    # 通过tunnel_forward方式创建adb-socket
    "tunnel_forward": True,
    # 画面裁剪
    "crop": "",
    # 开启控制
    "control": True,
    # 录制画面id，默认是0
    "display_id": 0,
    # 显示屏幕点击
    "show_touches": False,
    # 保持设备唤醒
    "stay_awake": True,
    # screen_off_timeout
    'screen_off_timeout': 10,
    # 视频编码参数，次参数为视频OMX.google.h264.encoder在有些机型报错
    "video_codec_options": "profile=1,level=2",
    # 音频编码参数
    "audio_codec_options": "",
    # 视频具体编码
    "video_encoder": "",
    # 音频具体编码
    "audio_encoder": "",
    # scrcpy解锁设备锁屏
    "power_off_on_close": False,
    # clipboard_autosync为False需要主动触发来获取，True为剪切板变动就获取内容
    "clipboard_autosync": False,
    # 录屏编码错误，降低录屏尺寸适配
    "downsize_on_error": True,
    # 开启清理线程。恢复[触摸显示|保持唤醒|输入法策略]等设置
    "cleanup": True,
    # 启动亮屏
    "power_on": True,
    # 列出支持的编码，为True时列出，此时server不运行
    "list_encoders": False,
    # 列出display_id,为True时列出，此时server不运行
    "list_displays": False,
    # 列出所有相机
    "list_cameras": False,
    # 列出所有相机尺寸
    "list_camera_sizes": False,
    # 列出所有安装的app
    "list_apps": False,
    # 相机id，安卓12及以上设备使用
    "camera_id": "",
    # 摄像头尺寸，比如1920x1080，错误的尺寸会导致相机报错
    "camera_size": "",
    # # 前后摄像头，有back,front,external,安卓12及以上设备使用
    "camera_facing": "back",
    # # 相机横纵比，比如 16:9，4:3等， 安卓12及以上设备使用
    "camera_ar": "",
    # # 相机fps，安卓12以上设备使用
    "camera_fps": 60,
    # # 相机快速模式，安卓12以上设备使用
    "camera_high_speed": False,
    # # 虚拟显示屏的尺寸，为空时即默认尺寸。  比如1920x1080，/240， 1920x1080/420
    'new_display': '',
    # # 虚拟显示屏关闭时，是否在主屏显示。True不在主屏显示
    'vd_destroy_content': True,
    # # 是否开启虚拟显示屏
    'vd_system_decorations': False,
    # locked to 水平翻转 + 180°旋转
    'capture_orientation': "@flip180",
    # local|fallback|hide。虚拟显示中ime的显示选项
    "display_ime_policy": 'local',
    # 发送设备源信息，设备名，分辨率等
    "send_device_meta": True,
    # 发送帧源信息
    "send_frame_meta": True,
    # 发送video socket连接成功dummy_byte
    "send_dummy_byte": True,
    # 发送编码源信息
    "send_codec_meta": True,
    # 仅发送裸流，此时send_device_meta，send_frame_meta，send_dummy_byte，send_codec_meta会被置为False
    "raw_stream": False
}