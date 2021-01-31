#Задание 4
#Создайте датафрейм authors_stat на основе информации из authors_price.
# В датафрейме authors_stat должны быть четыре столбца: author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора,минимальная, максимальная и средняя цена на книги этого автора.

import pandas as pd
authors = pd.DataFrame({'author_id':[1, 2, 3], 'author_name':['Тургенев', 'Чехов', 'Островский']})
books = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                    'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо',
                                  'Толстый и тонкий', 'Дата с собачкой', 'Гроза', 'Таланты и поклонники'],
                    'price':[450, 300, 350, 500, 450, 370, 290]})

authors_price = pd.merge(authors, books, on = 'author_id', how = 'inner')
top5 = authors_price.nlargest(5, 'price')

min_prices = authors_price.groupby('author_name').agg({'price': 'min'}).rename(columns = {'price': 'min_price'})
max_prices = authors_price.groupby('author_name').agg({'price': 'max'}).rename(columns = {'price': 'max_price'})
mean_prices = authors_price.groupby('author_name').agg({'price': 'mean'}).rename(columns = {'price': 'mean_price'})
result = pd.concat([min_prices, max_prices, mean_prices], axis=1, ignore_index=False)
print(result)