from django.urls import path, include

#from authentication.views import RegisterView
from authentication.views import LoginView, UserListView, UserDeleteView, user_form


urlpatterns = [
    path('users/create', user_form, name='user-create'),
    path("users/<int:pk>/update", user_form, name="user-update"),
    path("users/<int:pk>/delete", UserDeleteView.as_view(), name="user-delete"),
    path('users', UserListView.as_view(), name='user-list'),
    #path("users/<int:pk>/update", UserUpdateView.as_view(), name="user-update"),
    #path('register', RegisterView.as_view(), name='register'),
    #path('', LoginView.as_view(), name='login'),
]