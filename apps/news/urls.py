from django.urls import path
from apps.news import views

urlpatterns = [
    path('',views.ListNewsAPIView.as_view(),name='news_list'),
    path('categories/',views.news_categories,name='news_category'),
    path('create/',views.CreateNewsAPIView.as_view()),
    path('<int:pk>/',views.SingleNewsAPIView.as_view(),name='detail_news'),
    path('<int:pk>/update/',views.UpdateNewsAPIView.as_view()),
    path('<int:pk>/delete/',views.DeleteNewsAPIView.as_view()),
    path('<int:pk>/comment/',views.CommentCreateAPIView.as_view()),
]
