# -*- coding: utf-8 -*-
# В строке заменить все тире (-) знаком процента (%). 
# Подсчитать количество замен.
text = '''Пожилая пара, троллейбус, зима. 

Она – болтает со своячницей. 

Он – задремал в тепле у окна. Снится ему, что он молодой двадцатилетний парнище, косая сажень в плечах. И идут они с дружками на первомайскую демонстрацию, кепки заломили, штиблетами поскрипывают, да на девчонок заглядываются...

{И не слушает он, о чем трещит, как сломанный пропеллер, его жена. Пятьдесят лет ведь трещит уже…

- …А как там Лена-то? Племянница? Лена… Как же ее фамилия-то? Тьфу, забыла! Вань! Ваня? Спишь? Как ленина фамилия?

Ответ приходит мгновенно, еще даже до того, как первомайский сон закончился.

- Ульянов!

- Никогда не ходи в этот магазин, Сань. Никогда!} Были там с Машкой на распродаже шуб. Распродажа! Ха! Ты видел те цены?! Машка и присмотрела дорогущую. Пошли еще глянем, говорю, а продавец такая – ой, у нас их мгновенно раскупают, можете и не успеть! Вот! – думаю, - мой шанс!

Кое-как увел, три часа ходили, пришлось купить перчатки и сумочку, лишь бы отвлечь. Вернулись – хренак! нет шубы на витрине. Ура! – думаю. - Пронесло! И прикинь! Тут выходит эта змея, продавец. Ой, вы знаете, у нас все так расхватывают, а вы такая милая девушка, отложила я вашу шубку, чтоб вас не расстраивать. Змея и есть!'''

print('Количество замен "-" на "%": ', text.count('-'))
newText = text.replace('-', '%')