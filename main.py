# CRUD  de Livros
# titulo, autor, ano, genero, qtd de paginas, indioma
from PySimpleGUI import PySimpleGUI as sg
from functions import books, add_book, find_book

sg.theme('Reddit')

layout = [
    [sg.Input(key='search', size=(20, 1)), sg.Button('Pesquisar'),
    sg.Button('Novo Livro'),
    sg.Button('Atualizar Livro'),
    ],
    [sg.Table(values=books, headings=['Código', 'Título', 'Autor', 'Genero Literário', 'Indioma'], justification='left' , key='TABLE', size=(None, None),num_rows=10, auto_size_columns=True)],
    [sg.Button('Fechar')]
]

window_size = (800, 400)

window = sg.Window('Tela de teste', layout, size=window_size)

#  loop
while True:
    event, values = window.read()
    table = window['TABLE']
    if event == sg.WINDOW_CLOSED or event == 'Fechar':
       break
    if event == 'Pesquisar':
        search = values['search']
        result = find_book(search)
        if result != None:
           table.update(values=[books[result]])
        else:
           table.update(values=books)

