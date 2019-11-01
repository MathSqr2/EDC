from django.shortcuts import render
from datetime import datetime
from lxml import etree
import feedparser

# Create your views here.

def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)


def contact(request):
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)

def news(request):
    rss = feedparser.parse('https://www.cinemablend.com/rss_news_movies.xml')
    tparams = {
        'title': 'News',
        'rss': rss,
    }
    return render(request, 'news.html', tparams)

def category(request, category):
    tparams = {
        'title': 'News',
        'category': category
    }
    return render(request, 'category.html', tparams)