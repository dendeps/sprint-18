from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.template.loader import render_to_string
from .models import Author
from .forms import AuthorForm

def author_list(request):
    all_info = Author.objects.all()
    context = {
        'all_info': all_info}
    return render(request, 'author/author_list.html', context=context)

def add_author(request,id=0):
    if request.method=='GET':
        if id==0:
            form=AuthorForm()
        else:
            author=Author.objects.get(pk=id)
            form=AuthorForm(instance=author)
        return render(request,'author/add_author.html',{'form':form})
    else:
        if id==0:
            form=AuthorForm(request.POST)
        else:
            author=Author.objects.get(pk=id)
            form=AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/author/list/')





