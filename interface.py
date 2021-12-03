from PySimpleGUI import PySimpleGUI as sg
from projeto import backup, entrada, createBucket

createBucket()

sg.theme('Reddit')

def TelaPrincipal():    
    layout = [
        [sg.Text("Digite o texto para ser traduzido e convertido em audio")],
        [sg.InputText(key='textoIn')],
        [sg.Text(key='confirmacao')],
        [sg.Button("Converter"),sg.Button('Backup'), sg.Button("Fechar")]
    ]
    return sg.Window('Projeto-IV LinaldoQuirino', layout = layout, finalize=True)

def Confirmacao():
    layout = [
        [sg.Text("Pronto!")],
        [sg.Button("Fechar")]
    ]

    return sg.Window('Confirmação', layout, layout, finalize=True)



janela1, janela2 = TelaPrincipal(), None

while True:
    window, event, value = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Converter':
        entrada(value['textoIn'])
        janela2 = Confirmacao()
    if window == janela1 and event == 'Fechar':
        break
    if window == janela2 and event == 'Fechar':
        janela2.hide()
    if window == janela1 and event == 'Backup':
        backup()

        

