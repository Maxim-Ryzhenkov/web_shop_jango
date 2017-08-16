from django.shortcuts import render
from django.http import HttpResponse, Http404
from page.models import Category, Good


# Create your views here.

def index(request, category_id):
    if category_id is None:
        try:
            cat = Category.objects.first()
        except Category.DoesNotExist:
            raise Http404
    else:
        try:
            cat = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise Http404

    goods = Good.objects.filter(category=cat).order_by('name')
    s = "Категория: {}<br><br>".format(cat.name)
    for good in goods:
        s += '({}) {} <br>'.format(str(good.pk), good.name)
    return HttpResponse(s)


def good(request, good_id):
    try:
        good = Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404

    s = '{}<br><br>{}<br><br>{}'.format(good.name, good.category.name, good.description)
    if not good.in_stock:
        s += '<br><br>Нет в наличии!'
    return HttpResponse(s)
