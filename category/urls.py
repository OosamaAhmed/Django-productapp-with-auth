

from django.urls import path
from category.views import *


urlpatterns = [
    path('show/<int:pk>', CategoryDetailedView.as_view(), name='category.show'),
    path('listall/', CategoryListView.as_view(), name='category.listall'),
    path('delete/<int:pk>', CategoryDeleteView.as_view(), name='category.delete'),
    path('create/', CategoryCreateView.as_view(), name='category.create'),
    path('edit/<int:pk>', CategoryUpdateView.as_view(), name='category.edit')
]
