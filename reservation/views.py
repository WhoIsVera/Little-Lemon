from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Menu, Booking
from rest_framework import generics, viewsets, permissions
from .serializers import BookingSerializer, MenuSerializer, UserSerializers

# Create your views here La vista recibe el objeto de solicitud HTTP.
def index(request):
    return render(request, 'index.html', {})

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]


