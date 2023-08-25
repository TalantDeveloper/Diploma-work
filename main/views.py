from django.shortcuts import render
from .models import Category, Language, Short, Word, NotWord
from django.core.paginator import Paginator


def home(request):
    if request.method == 'POST':
        words = Word.objects.filter(short__name__icontains=request.POST.get('search'))
    else:
        words = Word.objects.all()
    categories = Category.objects.all()
    languages = Language.objects.all()
    shorts = Short.objects.filter(is_active=True)
    p = Paginator(words, 5)
    page = request.GET.get('page') or 1
    word_list = p.get_page(page)
    context = {
        'categories': categories,
        'languages': languages,
        'shorts': shorts,
        'words': words,
        'word_list': word_list,
    }
    return render(request, 'main/index.html', context)


def short_view(request, name):
    short = Short.objects.filter(name__contains=name.upper()) or None
    words = Word.objects.all().order_by('?')[:3]
    shorts = Short.objects.filter(is_active=True)
    if short:
        word = short[0].word.all()
        context = {
            'words': word,
            'languages': Language.objects.all(),
            'categories': Category.objects.all(),
            'word_list': words,
            'shorts': shorts
        }
        return render(request, 'main/short.html', context)
    return render(request, 'main/short.html')


def language_view(request, pk):
    categories = Category.objects.all()
    languages = Language.objects.all()
    shorts = Short.objects.filter(is_active=True)
    words = Word.objects.filter(language_id=pk)
    language = Language.objects.get(id=pk)
    p = Paginator(words, 5)
    page = request.GET.get('page') or 1
    word_list = p.get_page(page)
    context = {
        'categories': categories,
        'languages': languages,
        'shorts': shorts,
        'word_list': word_list,
        'language': language
    }
    return render(request, 'main/index.html', context)

def category_view(request, pk):
    category = Category.objects.get(id=pk)
    categories = Category.objects.all()
    languages = Language.objects.all()
    shorts = Short.objects.filter(is_active=True)
    words = Word.objects.all()
    word_list = []
    for word in words:
        for i in word.categories.all():
            if i == category:
                word_list.append(word)
    p = Paginator(word_list, 5)
    page = request.GET.get('page') or 1
    word_list = p.get_page(page)
    context = {
        'category': category,
        'categories': categories,
        'languages': languages,
        'shorts': shorts,
        'words': words,
        'word_list': word_list
    }
    return render(request, 'main/category.html', context)


