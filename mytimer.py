import PySimpleGUI as sg 
layout = [[sg.Text("计时器", size=(20,2), justification="center")],
            [sg.Text("", size=(10,2), font=("宋体", 20), justification="center", key="_OUTPUT_")],
            [sg.Text(" "*5), sg.Button("启动/停止", focus=True), sg.Button("退出")]]
window = sg.Window("计时器").Layout(layout)

timer_running = True
i = 0
while True:
    i += 1 * (timer_running is True)
    event, values = window.Read(timeout=10)
    if event is None or event == "退出":
        break
    elif event == "启动/停止":
        timer_running = not timer_running
    window.FindElement('_OUTPUT_').Update('{:02d}:{:02d}:{:02d}'.format(i//100//60, (i//100)%60, i%100))

window.Close()