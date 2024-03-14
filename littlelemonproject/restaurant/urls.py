from django.contrib import admin 
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

from. import views 
# from .views import sayHello 
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('',views.index,name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

]
