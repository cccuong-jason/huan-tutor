from . import views
from django.urls import path

urlpatterns = [
	path('list_product',views.get_product, name='list'),
	path('post_create',views.create, name='create'),
	path('post_update/<str:slug>',views.update, name='update'),
	path('post_delete/<str:slug>',views.delete, name='delete'),
]
