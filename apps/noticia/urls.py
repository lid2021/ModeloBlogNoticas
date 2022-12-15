from django.urls import path
from .views import NoticiaListview

urlpatterns = [
    path("noticiamas", NoticiaListview.as_view())
]
