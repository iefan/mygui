import PySimpleGUI as sg 
import subprocess

def ExecuteCommand(command, *args):
    try:
        sp = subprocess.Popen([command, *args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("gbk"))
        if err:
            print(err.decode("gbk"))
    except:
        print("所输入的命令无法有效执行!")

layout = [
    [sg.Text("脚本输出...", size=(40,1))],
    [sg.Output(size=(88,20), key="_OUTPUT_")],
    [sg.Button("脚本1"), sg.Button("脚本2"), sg.Button("退出")],
    [sg.Text("命令：",size=(15,1)), sg.InputText(focus=True), sg.Button("运行",bind_return_key=True)]
]

window = sg.Window("脚本执行器").Layout(layout)

while True:
    event, values = window.Read()
    if event is None or event == "退出":
        break
    if event == "脚本1":
        ExecuteCommand('pip', 'list')
        # window.FindElement("_OUTPUT_").clear()
    elif event == "脚本2":
        ExecuteCommand("python", "--version")
    elif event == "运行":
        cmdtmp = values[0]
        cmdtmp = cmdtmp.split(" ")
        if len(cmdtmp) == 2:
            ExecuteCommand(cmdtmp[0],cmdtmp[1])
        elif len(cmdtmp) == 1:
            ExecuteCommand(cmdtmp[0])
        else:
            print("所输入的命令超过可执行能力，请输入'pip list'类似样式的命令！")


window.Close()