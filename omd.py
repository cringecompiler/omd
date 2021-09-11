def step5_no_date():
    print('Ну ничего, в следующий раз точно познакомится.'
          'В скором времени утка-маляр 🦆 пришла домой и легла спать.\n'
          'Какой приятный вечер!')


def step5_date():
    print('Резким движением лапок, утка-маляр 🦆 потяпала к соседнему столику. '
          'К сожалению, гравитация сыграла не в нашу пользу, и утка-маляр 🦆 упала прямо перед своей целью.\n'
          'С позором и чувством собственной никчемности, она была вынуждена пойти домой.')


def step4_tipsy():
    print('Утка-маляр 🦆  решила, что ей достаточно. '
          'Однако сейчас hot-girl summer, и неплохо было бы закончить вечер новым знакомством.\n'
          'Стоит ли ей подкатить к утке-пожарному 🦆 за соседним столиком?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step5_date()
    return step5_no_date()


def step4_drunk():
    print('Наревное йе хввтит. Укта-малр🦆 решлила поеххать домой на ткси.\n'
          'Послле недогой позедки она прихала дмой. Слдкий снов, уттка=мляр🦆 !')


def step3_tequila(count_shots=0):
    if count_shots >= 3:
        return step4_drunk()
    print('Ого, да ей нравится! Берем еще?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        count_shots += 1
        return step3_tequila(count_shots)
    return step4_tipsy()


def step3_cider():
    print('Какой приятный вечер! '
          'Освежающий напиток отлично дополнил его.\n'
          'Утка-маляр 🦆 спокойно вышла из бара и добралась до дома. '
          'Как хорошо, что история на этом закончилась!')


def step2_umbrella():
    print('Утка-маляр 🦆 берет в лапки зонтик и идет в бар.\n'
          'Ей стоит взять шот текилы или 0.5 сидра?'
          )
    option = ''
    options = {'текила': True, 'сидр': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_tequila()
    return step3_cider()


def step2_no_umbrella():
    print('О нет, на улице дождь! Благо главный герой - утка-маляр 🦆, которая умеет плавать.\n'
          'Что же стоит взять в баре?'
          )
    option = ''
    options = {'текила': True, 'сидр': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_tequila()
    return step3_cider()


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
