import PySimpleGUI as sg 
import sys
if len(sys.argv) == 1:
    event, values = sg.Window("我的脚本对话框").Layout([[sg.Text("打开文档")], 
        [sg.Input(), sg.FileBrowse()], [sg.Button("打开"), sg.Button("退出")]]).Read()
    fname = values[0]
else:
    fname = sys.argv[1]
try:
    if not fname:
        sg.Popup("关闭", "没有提供文件名！")
        raise SystemExit("程序关闭：没有提供文件名")
    print("你要打开的文件名是：",fname)
except SystemExit as err:
    print(err)
print("系统输入：", sys.argv)