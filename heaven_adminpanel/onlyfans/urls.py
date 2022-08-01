
from django.urls import path, include

from onlyfans.views import OnlyFansWorkpage, CreateNewTable

urlpatterns = [
    path('', OnlyFansWorkpage.as_view(), name='onlyfans_workpage'),
    path('create_table/', CreateNewTable.as_view(), name='onlyfans_new_table'),
]