from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.template.loader import render_to_string
from .models import Book
from .forms import BookForm

def book_list(request):
    all_info = Book.objects.all()
    context = {
        'all_info': all_info}
    return render(request, 'book/book_list.html', context=context)

def add_book(request,id=0):
    if request.method=='GET':
        if id==0:
            form=BookForm()
        else:
            book=Book.objects.get(pk=id)
            form=BookForm(instance=book)
        return render(request,'book/add_book.html',{'form':form})
    else:
        if id==0:
            form=BookForm(request.POST)
        else:
            book=Book.objects.get(pk=id)
            form=BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/book/list/')





