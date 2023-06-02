# funções
books = [
     ['1111', 'ALice no Pais das maravilhas', 'não sei', 'fantasia', 'Portugues'],
     ['1112', 'A Sutil Arte de ligar o Foda-se', 'Mark Mason', 'n sei', 'portugues']
    ]


def add_book(code, title, author, generated, linguage):
    books.append([code, title, author, generated, linguage])

def find_book(search):
        if len(search) > 1:   
          for position, book in enumerate(books):
              code = book[0]
              name = book[1]
              if(search == code or search == name):
                  return position

def updade_book(code, update_book_list):
    position = find_book(code)[0]

    books[position][1] = update_book_list[0]
    books[position][2] = update_book_list[1]
    books[position][3] = update_book_list[2]
    books[position][4] = update_book_list[3]
    
     

# add_book(1111, 'ALice no Pais das maravilhas', 'não sei', 'fantasia', 'Portugues')
# add_book(1112, 'A Sutil Arte de ligar o Foda-se', 'Mark Mason', 'n sei', 'portugues')
# print(books)

# updade_book(1112, ['A Sutil Arte de ligar o Foda-se', 'Mark Mason', 'mente', 'portugues'])
# print(books)

