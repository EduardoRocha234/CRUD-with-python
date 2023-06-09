# funções 

# books => é a matriz de livros
# new_book => a lista com os novos livrso
def add_book(books, new_book):
    books.append(new_book)

# books => é a matriz de livros
# search => é a pesquisa feita pelo usuario no campo de pesquisa
def find_book(books, search):
        if len(search) >= 1:   
          for position, book in enumerate(books):
              code, name = book[0], book[1]
              name = book[1]
              if(search == code or search in name):
                # retorna uma lista coma a lista do livro encontrado e a posição dele na matriz
                  return [book, position] 
        else:
            print('Parametro de pesquisa Invalido, use o codigo ou o nome no livro para pesquisar')

# books => é a matriz de livros
# code => é o código do livro
# update_book_list => é a lista dos dados novos do livro
def updade_book(books, code, update_book_list):
    position = find_book(books, code)[1]
    print(position)

    books[position][1] = update_book_list[0]
    books[position][2] = update_book_list[1]
    books[position][3] = update_book_list[2]
    books[position][4] = update_book_list[3]

# books => é a matriz de livros
# book => é a lista do livro que vai ser removido
def delete_book(books, book):
  books.remove(book)
