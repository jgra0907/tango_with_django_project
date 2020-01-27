from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    context_dic = {}
    context_dic['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dic['categories'] = category_list

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dic)

def about(request):
    return render(request, 'rango/about.html')
