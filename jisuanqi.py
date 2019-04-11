import PySimpleGUI as sg
# import PySimpleGUIQt as sg
def jisuanqi():
    layout = [[sg.Text("计算器")], 
        [sg.InputText(do_not_clear=True, size=(7,3), key="_SHU1_",font=('Helvetica', 20)), sg.Text("__", font=('宋体', 20),justification='center',key="_FUHAO_",size=(3,3)), sg.InputText(font=('Helvetica', 20),do_not_clear=True, size=(7,3), key="_SHU2_"), sg.Text("=",font=('Helvetica', 20)), sg.Text("", size=(3,3),font=('Helvetica', 20),key="_RESULT_")],
    ]
    #将0~9及加减乘除排列成四行四列
    lst0_9 = [1,2,3,"+",4,5,6,"-",7,8,9,"×","",0,"","÷"]
    # lst0_9 = lst(range(1,10))
    # lst0_9.extend(["+","-","×", "÷"])
    tmp_shuzifuhao_lst = []
    for item in lst0_9:
        tmp_shuzifuhao_lst.append(sg.Button(str(item), size=(6,3)))
        if len(tmp_shuzifuhao_lst) == 4:
            layout.append(tmp_shuzifuhao_lst)
            tmp_shuzifuhao_lst = []
    
    layout.append([sg.Button("计算", size=(8,2)), sg.Button("清空",size=(8,2)), sg.Button("退出",size=(8,2))])

    window = sg.Window("计算器").Layout(layout)

    while True:
        button, values = window.Read()
        if button is None or button=="退出":
            break
        elif button=="清空":
            window.FindElement("_SHU1_").Update("")
            window.FindElement("_SHU2_").Update("")
            window.FindElement("_FUHAO_").Update("__")
            window.FindElement("_RESULT_").Update("")
        elif button=="计算":
            shu1 = values["_SHU1_"]
            shu2 = values["_SHU2_"]
            # fuhao = values["_FUHAO_"]
            fuhao = window.FindElement("_FUHAO_").DisplayText
            res_str = shu1+fuhao+shu2
            res_str = res_str.replace("×", "*")
            res_str = res_str.replace("÷", "/")
            # print(shu1+fuhao+shu2)
            result = eval(res_str)
            window.FindElement("_RESULT_").Update(str(result))
        else:
            if button in ["+","-","×","÷"]:
                window.FindElement("_FUHAO_").Update(button)
                # window.FindElement("_FUHAO_").DisplayText = button
                # window.FindElement("_FUHAO_").Update(str(fuhao))
            else:
                shu1 = values["_SHU1_"]
                shu2 = values["_SHU2_"]
                fuhao = window.FindElement("_FUHAO_").DisplayText
                # print(fuhao.DisplayText)
                # fuhao = values["_FUHAO_"]
                if fuhao == "__":
                    shu1 += button
                else:
                    shu2 += button
                window.FindElement("_SHU1_").Update(str(shu1))
                window.FindElement("_SHU2_").Update(str(shu2))


    window.Close()

def jisuanqi2():
    layout = [[sg.Text("计算器")], 
        [sg.InputText(do_not_clear=True, size=(19,3), key="_SHU1_",font=('Helvetica', 20))],
    ]
    #将0~9及加减乘除排列成四行四列
    lst0_9 = [1,2,3,"+",4,5,6,"-",7,8,9,"×","",0,"","÷"]
    # lst0_9 = lst(range(1,10))
    # lst0_9.extend(["+","-","×", "÷"])
    tmp_shuzifuhao_lst = []
    for item in lst0_9:
        tmp_shuzifuhao_lst.append(sg.Button(str(item),button_color=('black', 'orange'), size=(4,2),font=('Helvetica', 18)))
        if len(tmp_shuzifuhao_lst) == 4:
            layout.append(tmp_shuzifuhao_lst)
            tmp_shuzifuhao_lst = []
    
    layout.append([sg.Button("计算", button_color=('white', 'springgreen4'), font=('黑体', 16), size=(7,2)), 
        sg.Button("清空",button_color=('white', 'springgreen4'), font=('黑体', 16),size=(7,2)), 
        sg.Button("退出",button_color=('white', 'springgreen4'), font=('黑体', 16),size=(7,2))])

    window = sg.Window("计算器").Layout(layout)

    while True:
        button, values = window.Read()
        if button is None or button=="退出":
            break
        elif button=="清空":
            window.FindElement("_SHU1_").Update("")
            # window.FindElement("_SHU2_").Update("")
            # window.FindElement("_FUHAO_").Update("__")
            # window.FindElement("_RESULT_").Update("")
        elif button=="计算":
            shu1 = values["_SHU1_"]
            # shu2 = values["_SHU2_"]
            # # fuhao = values["_FUHAO_"]
            # fuhao = window.FindElement("_FUHAO_").DisplayText
            # res_str = shu1+fuhao+shu2
            res_str = shu1.replace("×", "*")
            res_str = res_str.replace("÷", "/")
            # print(shu1+fuhao+shu2)
            try:
                result = eval(res_str)
                shu1 += "=" 
                shu1 += str(result)
                window.FindElement("_SHU1_").Update(shu1)
            except:
                window.FindElement("_SHU1_").Update("表达式有误，请查证！")

        else:
            shu1 = values["_SHU1_"]
            # if shu1.find("+")+shu1.find("-")+shu1.find("×")+shu1.find("÷")==-4:#无符号
            # print(shu1=="", button, button not in ["+","-","×","÷"])
            if shu1 == "" and (button not in ["+","-","×","÷"]):
                shu1 = button
            elif shu1 == "" and (button in ["+","-","×","÷"]):
                pass
            else:                
                if shu1[-1] in ["+","-","×","÷"] and (button in ["+","-","×","÷"]):
                    pass
                else:
                    shu1 += button
            window.FindElement("_SHU1_").Update(str(shu1))


    window.Close()


if __name__ == "__main__":
    jisuanqi2()

