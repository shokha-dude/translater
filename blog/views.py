from django.db.models.expressions import result
from django.http import HttpResponse
from django.shortcuts import render
from .models import Dictionary

def index(request):
    word = request.GET.get('q', '')
    if word and word != '':
        result = Dictionary.objects.filter(russian__icontains=word).all()[:3]
    else:
        result = None
    return render(request, 'blog/index.html', {'q':word, 'result': result})

def about(request):
    return HttpResponse('About')
