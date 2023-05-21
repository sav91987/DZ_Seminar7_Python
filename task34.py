poem = 'пара-ра-рам рам-пАм-папам па-ра-па-дам'

poem = poem.lower().split()
res = set(map(lambda elem: elem.count('а'), poem))
if len(res) <= 1: print('Парам пам-пам')
else: print('Пам парам')