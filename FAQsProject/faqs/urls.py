from django.urls import path
from .views import add_faq, faq_list
from django.urls import include

urlpatterns = [
    path('add/', add_faq, name='add_faq'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('', faq_list, name='faq_list'),
]