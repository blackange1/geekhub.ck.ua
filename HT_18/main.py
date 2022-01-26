import argparse
from libs.stories import Stories


def main(type_stories='newstories'):
    check = (
        'askstories',
        'showstories',
        'newstories',
        'jobstories'
    )
    if type_stories in check:
        print(f'Ви обрали {type_stories}'.upper())
        # stories = Stories(type_stories)
        # stories.run_parsing()
    else:
        print('помилка введення команди')


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("type",
                            type=str,
                            help="type of stories",
                            default="newstories")
        args = parser.parse_args()
        main(args.type)
    except:
        main()
