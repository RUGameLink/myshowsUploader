from data_loader import Data_Loader
from youtube_parser import YouTube_Parser


def parsing_menu(list_channel):
    i = 0
    print('100 -- Exit')
    for channel in list_channel:
        print(f'{i} -- {channel[0]}')
        i += 1
    option = int(input('Выберите канал: '))
    if option == 100:
        return
    elif option <= len(list_channel):
        parser = YouTube_Parser()
        channel = list_channel[option]
        parser.start_parsing(channel[0], channel[1])


def write_channel():
    title = input('Введите название канала ')
    url = input('Вставьте ссылку на канал ')
    myshows_block = input('Вставьте XPATH строки на myshows ')

    my_file = open('channel_list.txt', 'a', encoding="utf-8")
    my_file.write(f'{title}, {url}, {myshows_block}\n')
    my_file.close()
    print('Сохранено!')


def read_channel():
    video_info = []
    data_channel = open("channel_list.txt", "r", encoding='utf-8')
    for video in data_channel:
        data = video.split(',')
        video_info.append(data)
    return video_info


def upload_menu(list_channel):
    i = 0
    print('100 -- Exit')
    for channel in list_channel:
        print(f'{i} -- {channel[0]}')
        i += 1
    option = int(input('Выберите канал: '))
    if option == 100:
        return
    elif option <= len(list_channel):
        loader = Data_Loader()
        channel = list_channel[option]
        max_ep = int(input('Введите максимальное количество эпизодов в сезоне: '))
        loader.upload_to_myshows(channel[0], channel[2], max_ep)


def print_menu():
    menu_options = {
        1: 'Парсинг данных',
        2: 'Загрузка в myshows',
        3: 'Добавление канала',
        4: 'Exit',
    }

    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def main():
    print_menu()

    while True:
        try:
            option = int(input('Введите число для работы: '))
            if option == 1:
                print('Загружаю список каналов...')
                list = read_channel()
                parsing_menu(list)
                print_menu()
            elif option == 2:
                print('загружаю список каналов для загрузки в myshows')
                list = read_channel()
                upload_menu(list)
                print_menu()
            elif option == 3:
                print('Подготовка к записи...')
                write_channel()
                print_menu()
            elif option == 4:
                print('До скорой встречи!')
                exit()
            else:
                print('Команда не распознана!')
                print_menu()
        except Exception as e:
            print(e)
            print('Команда не распознана!')
            print_menu()



if __name__ == '__main__':
    main()
