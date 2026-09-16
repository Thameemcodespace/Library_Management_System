from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library import views
from library.api_views import BookViewSet


router = DefaultRouter()
router.register('books', BookViewSet)


urlpatterns = [
    path('', views.home, name='home'),

    path('add/', views.add_book, name='add_book'),

    path('view/<int:id>/', views.view_book, name='view_book'),

    path('edit/<int:id>/', views.edit_book, name='edit_book'),

    path('delete/<int:id>/', views.delete_book, name='delete_book'),

    path('api/', include(router.urls)),

    path('admin/', admin.site.urls),
]