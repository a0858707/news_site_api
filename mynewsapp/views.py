# импорт новостей
from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient

# Создание функции представления
def index(request):

    newsapi = NewsApiClient(api_key ='de80688d074e476f96628db2ffe0f3ff')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    dsc =[]
    nws =[]
    im =[]

    for i in range(len(l)):
      f = l[i]
      nws.append(f['title'])
      dsc.append(f['description'])
      im.append(f['urlToImage'])
      mylist = zip(nws, dsc, im)

    return render(request, 'index.html', context ={"mylist":mylist})