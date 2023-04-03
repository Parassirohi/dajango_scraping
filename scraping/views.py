import dateparser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from django.http import HttpResponse

from .serializer import ArticleSerializer
from .models import Article

from bs4 import BeautifulSoup
import requests


def index(request):
    data()
    return HttpResponse("Success")


# class ArticleViewSet(ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


def data():
    link = "https://www.theverge.com"

    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')

    def latest():
        articles = soup.find_all("div",
                                 class_="relative border-b border-gray-31 pb-20 md:pl-80 lg:border-none lg:pl-[165px] "
                                        "-mt-20 sm:-mt-40")

        for article in articles:
            headline = article.find(class_="group-hover:shadow-highlight-blurple").text
            complete_link = article.find("a", class_="group-hover:shadow-highlight-blurple")["href"]
            url = link + complete_link
            author = article.find("a", class_="text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8").text
            date = article.find("span", class_="text-gray-63 dark:text-gray-94").text

            if not Article.objects.filter(headline=headline).exists():
                article = Article()
                article.headline = headline
                article.url = url
                article.author = author
                article.date = dateparser.parse(date)
                article.save()

    def topstory():
        topstoryarticles = soup.find_all("div", class_="max-w-content-block-standard md:w-content-block-compact "
                            "md:max-w-content-block-compact lg:w-[240px] lg:max-w-[240px] lg:pr-10")

        for story in topstoryarticles:
            headline = story.find(class_="group-hover:shadow-underline-franklin").text
            complete_link = story.find("a", class_="group-hover:shadow-underline-franklin")["href"]
            url = link + complete_link
            author = story.find("a", class_="text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8").text
            date = story.find("span", class_="text-gray-63 dark:text-gray-94").text

            if not Article.objects.filter(headline=headline).exists():

                article = Article()
                article.headline = headline
                article.url = url
                article.author = author
                article.date = dateparser.parse(date)
                print(date)
                article.save()
    latest()
    topstory()
    return Response({'message': 'Article saved successfully.'})

