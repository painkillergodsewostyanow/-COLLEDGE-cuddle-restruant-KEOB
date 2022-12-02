from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('menu', menu, name='menu'),
    path('reg', reg.as_view(), name='reg'),
    path('log', log_in.as_view(), name='log'),
    path('com', comment, name='com'),
    path('logout', logout_user, name='logout'),
    path('addcomment', add_page, name='addpage'),
    path('delivery', delivery, name='delivery'),
    path('book', do_book, name='book')
]


