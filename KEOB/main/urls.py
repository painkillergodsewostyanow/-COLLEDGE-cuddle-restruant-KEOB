from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('menu', menu, name='menu'),
    path('reg', reg.as_view(), name='reg'),
    path('log', log_in.as_view(), name='log')
]


