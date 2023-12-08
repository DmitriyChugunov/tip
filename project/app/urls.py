from django.urls import path

from .views import shop, myForm, NewsView, ProductView

urlpatterns = [
    path('', shop),
    path('form', myForm),
    path('news', NewsView),
    path('dilivery', ProductView),
]