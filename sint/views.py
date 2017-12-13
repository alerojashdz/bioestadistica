from django.shortcuts import render
from sint.models import Category, Sujeto

def base(request):
    return render(request, 'base.html')

def contenido(request):
    return render(request, 'contenido.html')

def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request, 'sint/category.html', context)

def category_detail(request, category_id):

    category = Category.objects.get(id=category_id)
    context = {'object': category}
    return render(request, 'sint/category_detail.html', context)

def sujeto(request):
    sujeto_list = Sujeto.objects.all()
    context = {'sujeto_list': sujeto_list}
    return render(request, 'sint/sujeto.html', context)

def sujeto_detail(request, sujeto_id):
    sujeto = Sujeto.objects.get(id=sujeto_id)
    context = {'sujeto': sujeto}
    return render(request, 'sint/sujeto_detail.html', context)









# Create your views here.
