from django.urls import path
from apps.accounts import views

urlpatterns = [
    path("users/create/",views.CreateUserView.as_view()),
    path("users/<int:pk>/update/",views.UpdateUserView.as_view()),
    path("users/<int:pk>/newses/",views.user_newses),
]