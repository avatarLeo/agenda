from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'contato'

urlpatterns = [
    path('contact/<int:contact_id>/detail/',views.contact, name='contact'),
    path('contact/<int:contact_id>/update/',views.update, name='update'),
    path('contact/<int:contact_id>/delete/',views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    #user
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),


    
    
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)