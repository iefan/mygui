import PySimpleGUI as sg    

tab1_layout =  [[sg.T('第一个页面的文本')]]    

tab2_layout = [[sg.T('第二个页面的文本')],    
               [sg.In(key='in')]]    

layout = [[sg.TabGroup([[sg.Tab('页面1', tab1_layout, tooltip='tip'), sg.Tab('页面2', tab2_layout)]], tooltip='TIP2')],    
          [sg.Button('读取数据')]]    

window = sg.Window('多页面窗口', default_element_size=(20,1)).Layout(layout)    

while True:    
    event, values = window.Read()    
    if event is None:           # always,  always give a way out!    
        break  
    print(event,values)    
window.Close()