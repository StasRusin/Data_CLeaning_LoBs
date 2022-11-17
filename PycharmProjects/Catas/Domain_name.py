def domain_name(url):
    #beg_wor = {'www.': 4,  'https://www.':12, 'https://': 8, 'http://': 7}
    beg_wor = {'www.': 4, 'https://': 8, 'http://': 7}
    beg_url=0
    for i in beg_wor:
        if url.find(i) !=-1:
            beg_url=beg_wor[i]+beg_url
            #print("found " + str(beg_url))
    end_url=url.find('.', beg_url)
            #print("end_url = " + str(end_url))
            #print(url[beg_url:end_url])
    return url[beg_url:end_url]

if __name__== '__main__' :
    #url="www.xakep.ru"
    #url="www.youtube.com"
    url= input("Введите адрес строки ")
    #"http://google.com"
    print(domain_name(url))
