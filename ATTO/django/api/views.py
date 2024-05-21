from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializers, TarifSerializers, User, Tarif


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializers
    lookup_field = 'telegram_id'

    def get_queryset(self):
        telegram_id = self.kwargs['telegram_id']
        return User.objects.filter(telegram_id=telegram_id)


class TarifCreateView(generics.ListCreateAPIView):
    queryset = Tarif.objects.all()
    serializer_class = TarifSerializers


class TarifDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarif.objects.all()
    serializer_class = TarifSerializers
