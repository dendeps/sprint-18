from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView

from authentication.forms import CustomUserForm
from authentication.models import CustomUser


class UserListView(ListView):
        model = CustomUser
        template_name = 'user/user_list.html'
        context_object_name = 'items'


class UserDetailsView(View):
    def get(self, request, pk, *args, **kwargs):
        user = CustomUser.objects.get(pk=pk)
        context = {
            'item': user
        }
        return render(request, 'user/user_details.html', context)


def user_form(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = CustomUserForm()
        else:
            user = CustomUser.objects.get(pk=pk)
            form = CustomUserForm(instance=user)
        return render(request, 'user/customuser_form.html', {'form': form})
    else:
        if pk == 0:
            form = CustomUserForm(request.POST)
        else:
            user = CustomUser.objects.get(pk=pk)
            form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/users')


class UserDeleteView(DeleteView):
    model = CustomUser
    success_url = "/users"
    template_name = "user/delete_user.html"




class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/login.html')

    '''def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            context = {
                'message': f'User with email: {email} logged in!'
            }
            return render(request, 'user/success.html', context)
        else:
            context = {
                'message': f'Invalid credentials!'
            }
            return render(request, 'user/error.html', context)'''