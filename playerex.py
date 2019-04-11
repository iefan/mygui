import PySimpleGUI as sg
def MediaPlayerGUI():
    background = '#F0F0F0'
    sg.SetOptions(background_color=background, element_background_color=background)
    image_pause = './pause.png'
    image_restart = './prev.png'
    image_next = './next.png'
    image_exit = './exit.png'
    layout= [[sg.Text('Media File Player',size=(17,1), font=("Helvetica", 25))],
             [sg.Text('', size=(15, 2), font=("Helvetica", 14), key='output')],
             [sg.Button('', button_color=(background,background),
                image_filename=image_restart, image_size=(60, 60), image_subsample=1, border_width=0, key='Restart Song'),
              sg.Text(' ' * 2),
              sg.Button('', button_color=(background,background),
                image_filename=image_pause, image_size=(60, 60), image_subsample=1, border_width=0, key='Pause'),
              sg.Text(' ' * 2),
              sg.Button('', button_color=(background,background), 
                image_filename=image_next, image_size=(60, 60), image_subsample=1, border_width=0, key='Next'), 
              sg.Text(' ' * 2),
              sg.Button('', button_color=(background,background),
                image_filename=image_exit, image_size=(60, 60), image_subsample=1, border_width=0, key='Exit')],
            [sg.Text('_'*20)],
            [sg.Text(' '*30)],
            [
             sg.Slider(range=(-10, 10), default_value=0, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(-10, 10), default_value=0, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(-10, 10), default_value=0, size=(10, 20), orientation='vertical', font=("Helvetica", 15))],
             [sg.Text('   Bass', font=("Helvetica", 15), size=(9, 1)),
             sg.Text('Treble', font=("Helvetica", 15), size=(7, 1)),
             sg.Text('Volume', font=("Helvetica", 15), size=(7, 1))]
             ]
    window = sg.Window('Media File Player', auto_size_text=True, default_element_size=(20, 1),
                       font=("Helvetica", 25)).Layout(layout)
    while(True):
        event, values = window.Read(timeout=100)        # Poll every 100 ms
        if event == 'Exit' or event is None:
            break
        if event != sg.TIMEOUT_KEY:
            window.FindElement('output').Update(event)

MediaPlayerGUI()