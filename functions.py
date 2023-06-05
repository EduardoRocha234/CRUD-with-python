# funções

def add_book(books, new_book):
    books.append(new_book)

def find_book(books, search):
        if len(search) > 1:   
          for position, book in enumerate(books):
              code = book[0]
              name = book[1]
              if(search == code or search in name):
                  return position
        else:
            print('Parametro de pesquisa Invalido, use o codigo ou o nome no livro para pesquisar')

def updade_book(books, code, update_book_list):
    position = find_book(books, code)
    print(position)

    books[position][1] = update_book_list[0]
    books[position][2] = update_book_list[1]
    books[position][3] = update_book_list[2]
    books[position][4] = update_book_list[3]

# updade_book(books, '1112', ['A Sutil Arte de ligar o Foda-se', 'Mark Mason', 'mente', 'portugues'] )



    
     

# add_book(1111, 'ALice no Pais das maravilhas', 'não sei', 'fantasia', 'Portugues')
# add_book(1112, 'A Sutil Arte de ligar o Foda-se', 'Mark Mason', 'n sei', 'portugues')
# print(books)

# updade_book(1112, ['A Sutil Arte de ligar o Foda-se', 'Mark Mason', 'mente', 'portugues'])
# print(books)

