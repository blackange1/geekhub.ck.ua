from libs.stories import Stories


def main():
    menu = (
        'askstories',
        'showstories',
        'newstories',
        'jobstories'
    )
    for i in range(len(menu)):
        print(f'{i} - парсити {menu[i]}')

    try:
        n = input('Введіть номер команди\n')
        n = 2 if n == '' else n
        type_stories = menu[int(n)]
        print(f'Ви обрали {type_stories}'.upper())
        stories = Stories(type_stories)
        stories.run_parsing()
    except:
        print('помилка введення команди')


if __name__ == '__main__':
    main()

