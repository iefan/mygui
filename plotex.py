import PySimpleGUI as sg

# layout = [      
#     [sg.Canvas(size=(100, 100), background_color='red', key= 'canvas')],      
#     [sg.T('改变圆的颜色:'), sg.Button('红色'), sg.Button('蓝色')]      
#     ]

# window = sg.Window('画布测试')      
# window.Layout(layout)      
# window.Finalize()

# canvas = window.FindElement('canvas')      
# cir = canvas.TKCanvas.create_oval(50, 50, 100, 100)

# while True:      
#     event, values = window.Read()      
#     if event is None:      
#         break      
#     if event == '蓝色':      
#         canvas.TKCanvas.itemconfig(cir, fill="Blue")      
#     elif event == '红色':      
#         canvas.TKCanvas.itemconfig(cir, fill="Red")
# window.Close()

layout = [      
            [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0,0), graph_top_right=(400, 400), background_color='red', key='graph')],      
            [sg.T('改变颜色:'), sg.Button('红色'), sg.Button('蓝色'), sg.Button('移动')]      
            ]      

window = sg.Window('图形测试')      
window.Layout(layout)      
window.Finalize()      

graph = window.FindElement('graph')      
circle = graph.DrawCircle((75,75), 25, fill_color='black',line_color='white')      
point = graph.DrawPoint((75,75), 10, color='green')      
oval = graph.DrawOval((25,300), (100,280), fill_color='purple', line_color='purple'  )      
rectangle = graph.DrawRectangle((25,300), (100,280), line_color='purple'  )      
line = graph.DrawLine((0,0), (100,100))      

while True:      
    event, values = window.Read()      
    if event is None:      
        break      
    if event is '蓝色':      
        graph.TKCanvas.itemconfig(circle, fill = "Blue")      
    elif event is '红色':      
        graph.TKCanvas.itemconfig(circle, fill = "Red")      
    elif event is '移动':      
        graph.MoveFigure(point, 10,10)      
        graph.MoveFigure(circle, 10,10)      
        graph.MoveFigure(oval, 10,10)      
        graph.MoveFigure(rectangle, 10,10)

window.Close()