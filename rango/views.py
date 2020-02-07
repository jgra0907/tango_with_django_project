from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dic = {}
    context_dic['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dic['categories'] = category_list
    context_dic['pages'] = page_list

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dic)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method=='POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            return redirect('/rango/')
        else:
            #The supplied form contained errors. Print them
            print(form.errors)
    #Handle bad form, new form, or no form supplied cases.
    return render(request, 'rango/add_category.html', {'form': form})
