from PySimpleGUI import PySimpleGUI as sg
from functions import add_book, find_book, updade_book, delete_book
# CRUD  de Livros
# titulo, autor, ano, genero, qtd de paginas, indioma
sg.theme('DarkBlue13')

books = [
   ['01', 'Teste', 'JJ', 'fantasia', 'portugues'],
   ['02', 'Teste 2', 'pp', 'fantasia', 'ingles'],
   ['03', 'Teste 3', 'bb', 'drama', 'portugues']
]

def tela_principal():
  print(books)
  table_values = books[:]
  #  cabeçalho da tabela
  headers= ['Código', 'Título', 'Autor', 'Genero Literário', 'Indioma']
  layout = [
      [sg.Input(key='search', pad=((5, 5), 0), size=(20, 1)), sg.Button('Pesquisar', pad=((5, 215), 0)),
      sg.Button('Novo Livro'),
      sg.Button('Editar Livro'),
      ],
      [sg.Table(values=table_values, headings=headers, justification='left' , key='TABLE', num_rows=10, auto_size_columns=False, bind_return_key=True, col_widths=[5, 20, 15, 15])],
      [sg.Button('Fechar', pad=((5, 460), 0)), sg.Button('Deletar Livro')]
  ]
  window = sg.Window('Livros', layout)
  #  loop
  while True:
      event, values = window.read()
      table = window['TABLE']
     
      if event == sg.WINDOW_CLOSED or event == 'Fechar':
        break

      if event == 'Pesquisar':
         search = values['search']
         result = find_book(books, search)
         if result != None:
            table_values.clear()
            table_values.append(result[0])
            table.update(values=table_values)
         else:
            table_values = books[:]
            table.update(values=books)

      if event == 'Novo Livro':
        window.close()
        tela_cadastro(table)
    
      if event == 'Editar Livro':
        if values['TABLE']:
            selected_row = values['TABLE'][0]
            print(selected_row)
            row_data = table_values[selected_row]
            print('Dados do Item Clicado:', row_data)
            window.close()
            tela_editar(table, row_data)
        else: 
            sg.popup_ok('Nenhum registro selecionado. Selecione um registro para editar.')

      if event == 'Deletar Livro':
         if values['TABLE']:
            confirmar = sg.popup_ok_cancel('Deseja Deletar este livro?')
            if confirmar == 'OK':
               selected_row = values['TABLE'][0]
               book_to_delete = table_values[selected_row]
               delete_book(books, book_to_delete)
               table.update(values=books)
         else:
            sg.popup_ok('Nenhum registro selecionado. Selecione um registro para deletar.')


        

def tela_cadastro(table):
   layout_cadastro = [
      [sg.Text('CADASTRAR NOVO LIVRO')],
      [sg.HorizontalSeparator()],
      [sg.Text('Código:')],
      [sg.Input(key='code', size=(50, 1))],
      [sg.Text('Título:')],
      [sg.Input(key='title', size=(50, 1))],
      [sg.Text('Autor:')],
      [sg.Input(key='author', size=(50, 1))],
      [sg.Text('Genero Literário:')],
      [sg.Input(key='gen', size=(50, 1))],
      [sg.Text('Indioma do Livro:')],
      [sg.Input(key='linguage', size=(50, 1))],
      [sg.Button('Cadastrar'), sg.Button('Cancelar')]
   ]
   janela_cadastro = sg.Window('Cadastrar Novo Livro', layout_cadastro)
   while True:
      event, values = janela_cadastro.read()
      if event == sg.WINDOW_CLOSED or event == 'Cancelar':
         janela_cadastro.close()
         tela_principal()
         break
      elif event == 'Cadastrar':
         # Capturar valores dos campos de entrada
         code = values['code']
         title = values['title']
         author = values['author']
         gen = values['gen']
         linguage = values['linguage']
         new = [code, title, author, gen, linguage]
         all_not_empty = True
         for data in new:
            if data == '':
               all_not_empty = False

         if not all_not_empty:
            sg.popup_ok('O registro não pode ter campos vazios.')
         else:
            add_book(books, new)      
            # Atualizar tabela com a nova lista de books
            janela_cadastro.close()
            tela_principal()
            table.update(values=books)
            # Fechar a janela de cadastro


def tela_editar(table, book):
    layout_editar = [
       [sg.Text('EDITAR LIVRO')],
       [sg.HorizontalSeparator()],
       [sg.Text('Título:')],
       [sg.Input(key='title', size=(50, 1), default_text=book[1])],
       [sg.Text('Autor:')],
       [sg.Input(key='author', size=(50, 1), default_text=book[2])],
       [sg.Text('Genero Literário:')],
       [sg.Input(key='gen', size=(50, 1), default_text=book[3])],
       [sg.Text('Indioma do Livro:')],
       [sg.Input(key='linguage', size=(50, 1), default_text=book[4])],
       [sg.Button('Editar'), sg.Button('Cancelar')]
    ]
    janela_editar = sg.Window('Editar Livro', layout_editar)
    while True:
       event, values = janela_editar.read()
       if event == sg.WINDOW_CLOSED or event == 'Cancelar':
           janela_editar.close()
           tela_principal()
           break
       elif event == 'Editar':
           # Capturar valores dos campos de entrada
           code = book[0]
           title = values['title']
           author = values['author']
           gen = values['gen']
           linguage = values['linguage']
           book_list = [title, author, gen, linguage]
           updade_book(books, code, book_list)
         #   updade_book(table_values, code, book_list)
           # Atualizar tabela com a nova lista de books
           janela_editar.close()
           tela_principal()
           table.update(values=books)
           # Fechar a janela de cadastro
   
tela_principal()
       

