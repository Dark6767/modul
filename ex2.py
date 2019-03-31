urls=[['','']]
def input_url():
    name_url = input('Введите полную ссылку>')
    srt_url = input('Введите сокращенную ссылку>')
    urls.append([name_url,srt_url])
def search_url(shrt_url):
    for i in urls:
        if i[1]==shrt_url:
            print('Полная ссылка>>'+i[0])
def main():
    input_url()
    input_url()
    search_url(input('Введите сокращенную ссылку для получения полной>'))
if __name__ == '__main__':
    main()