import requests
def generate_answ():
    URL = 'https://old.myshows.me/mt/episodes/76691/add'
    action = 'add'
    token = 'a71a69b2974e1'
    selectedTab = '0'
    title = 'test'
    seasonNumber = '2023'
    episodeNumber = '0'
    airDate = '26.01.2023'
    sequenceNumber = '0'
    runtime = '12'
    statusId = '1'

    form_data = {
        'action': action,
        '__token': token,
        'selectedTab': selectedTab,
        'episode[title]': title,
        'episode[seasonNumber]': seasonNumber,
        'episode[episodeNumber]': episodeNumber,
        'episode[airDate]': airDate,
        'image': '',
        'episode[sequenceNumber]': sequenceNumber,
        'episode[productionNumber]': '',
        'episode[runtime]': runtime,
        'episode[statusId]': statusId,
        'episode[externalIds][tvrage]': '',
        'episode[externalIds][tvmaze]': '',
        'episode[externalIds][thetvdb]': '',
        'episode[externalIds][imdb]': '',
        'episode[externalIds][kinopoisk]': '',
        'episode[externalIds][rt]': '',
        'episode[externalIds][amediateka]': '',
        'episode[externalIds][youtube]': '',
        'episode[externalIds][showjet]': '',
        'episode[externalIds][ivi]': '',
        'episode[externalIds][okko]': '',
        'episode[externalIds][kion]': '',
        'episode[externalIds][wink]': '',
        'episode[externalIds][justwatch]': '',
        'ohCreatedAt': ''
    }
    print(form_data)
    #Сборка ответа и загрузка в форму
    ##HEADER##
    header = {
        'authority': 'old.myshows.me',
        'method': 'POST',
        'path': '/mt/episodes/76691/add',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru,en;q=0.9,es;q=0.8',
        'cache-control': 'max-age=0',
        'content-length': '3017',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarychsDC9egBzqzscWn',
        'cookie': 'msid=X9WZImNrnUo8Yiahin3cAg==; adtech_uid=5842b8e5-fde9-4743-92d1-f61b00cf4ef4%3Amyshows.me; top100_id=t1.1923755.1959652481.1667997013516; SiteUser[login]=sad_smiley; SiteUser[password]=aa8a2038791565d5537eeb8ed2a2796b; _ym_uid=16692244681045413878; _ym_d=1669224468; __gads=ID=b1ab31a7719618a3-22b952355fda00a1:T=1671809156:RT=1671809156:S=ALNI_Maa-2-8EtDCojuJeVzy_0aqsHNfdA; tmr_lvid=a750b5a7c31b1a40ac613c9f0c278e83; tmr_lvidTS=1671809156343; last_visit=1672463490692%3A%3A1672492290692; t3_sid_1923755=s1.39338767.1672492290688.1672492294455.5.3; __gpi=UID=00000b973b787f89:T=1671809156:RT=1673177349:S=ALNI_MbMlc51qbJoRxvuyx8kjI4VCXPu5w; msAuthToken=888a410d645fb366a73e571cb4774572ee1a85ea; msRefreshToken=96b3efe71fccbe940bb8ade1c0908b14c9fd3033aa573bec18af596d84ce3b0ad8a0efee2980118aac5b5adc752259e9e755691052f03eb0; _ga=GA1.2.160649657.1669224467; _ga_QES40KQ53S=GS1.1.1674420966.46.0.1674420966.0.0.0; PHPSESSID=948ee209cd380acb5810d451e1778476',
        'origin': 'https://old.myshows.me',
        'referer': 'https://old.myshows.me/mt/episodes/76691/add',
        'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36'
    }
    user_agent = {'Referer': URL,'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36"}
    req = requests.post(URL, data=form_data, headers=header).status_code
    print(req)

def main():
    generate_answ()


if __name__ == '__main__':
    main()