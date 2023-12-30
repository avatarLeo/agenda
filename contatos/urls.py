from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'contato'

urlpatterns = [
    path('contact/<int:contact_id>/detail/',views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)