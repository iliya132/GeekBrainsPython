#Задание 2
#Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

import pandas as pd
authors = pd.DataFrame({'author_id':[1, 2, 3], 'author_name':['Тургенев', 'Чехов', 'Островский']})
books = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                    'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо',
                                  'Толстый и тонкий', 'Дата с собачкой', 'Гроза', 'Таланты и поклонники'],
                    'price':[450, 300, 350, 500, 450, 370, 290]})

authors_price = pd.merge(authors, books, on = 'author_id', how = 'inner')
print(authors_price)