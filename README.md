# pywebcam

可以将摄像头视频通过浏览器实时显示出来。基于Flask和OpenCV。

## 运行

```bash
python3 main.py
```

访问`5000`端口即可。如果端口不可用，更改`main.py`中的`app.run(host='0.0.0.0', port=5000, debug=True)`即可。
