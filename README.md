# Add_Tracker_to_Magnet  --  将 Tracker 添加到磁链

向磁链中添加TrackerURL。
Add Tracker URL to Magnet.

## 生成可执行文件  -- To generate binary code

需要 python3.8 或更高；需安装`pyinstaller`

```shell
pip install pyinstaller # If `pyinstaller` is not installed yet.
pyinstaller --optimize=2 -c -F main.py --distpath ./ -n add_tracker_to_magnet
```

## 使用方法  --  Usage

### 命令行版本  --  Shell Version

python3.8 以上版本中运行：(git 下载源码)

```shell
python3 main.py
```

或直接运行发行版：

```shell
./add_tracker_to_magnet
```

- 在`Initial Magnet link:`后输入原本的 magnet link。回车输入。
- 在``Tracker Url (Press `Ctrl + D` to stop):``后输入tracker地址。注意：每个tracker占一行。可以输入空白行。
- 回车，在空白行按`Ctrl + D`触发EOF，完成 Tracker Url 的输入。
- `---------- Magnet Link with Tracker: ----------`之后的即为添加tracker后的magnet link。
