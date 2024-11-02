from django.shortcuts import render
from .models import Menu, Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .serializers import BookingSerializer, MenuSerializer

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


