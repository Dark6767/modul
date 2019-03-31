urls=[['','']]
def input_url(name_url,srt_url):
    urls.append([name_url,srt_url])
def search_url(shrt_url):
    for i in urls:
        if i[1]==shrt_url:
            print('Полная ссылка>>'+i[0])