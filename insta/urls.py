from django.urls import path
from insta import views

urlpatterns = [
    path('', views.list),
    path('upload', views.PhotoUpload.as_view(), name='upload'),
    path('detail/<int:pk>', views.PhotoDetail.as_view(), name='detail'),
]
