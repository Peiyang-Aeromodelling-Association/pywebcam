# pywebcam

可以将摄像头视频通过浏览器实时显示出来。基于Flask和OpenCV。

## 运行

### Server端
```bash
python3 server.py
```

### Client端

在`client.py`修改`url`为Server端的IP地址，然后运行

```bash
python3 client.py
```

或者在浏览器中访问对应地址`5000`端口即可。如果端口不可用，更改`main.py`中的`app.run(host='0.0.0.0', port=5000, debug=False)`即可。
