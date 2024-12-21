import pandas as pd

music = [
    ['Король и Шут', 'Лесник'],
    ['Anacondaz', 'Мама, я люблю'],
    ['Nautilus Pompilius','Во время дождя'],
    ['Агата Кристи','Чёрная луна'],
    ['Комбинация','Хватит, довольно']
]
entries = ['artist', 'track']
table = pd.DataFrame(data = music, columns = entries)
print(table)