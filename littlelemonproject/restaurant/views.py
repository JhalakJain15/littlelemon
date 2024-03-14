from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem, Booking
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer,BookingSerializer,UserSerializer
from rest_framework import generics,viewsets,permissions
# def sayHello(request):
#     return HttpResponse('Hello World!')
def index(request):
    return render(request,'index.html',{})
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all() 
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]