from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.viewsets import ModelViewSet

class SignUpView(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    model = User


class UserViewset(ModelViewSet):

    permission_classes = [IsManagerAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):

        queryset = User.objects.all()

        id = self.request.GET.get('id')
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset

class ClientViewset(ModelViewSet):

    permission_classes = [IsSalesAuthenticated]
    serializer_class = ClientSerializer

    def get_queryset(self):

        queryset = Client.objects.all()

        id = self.request.GET.get('id')
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


class EventViewset(ModelViewSet):

    permission_classes = [IsSupportAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self, *args, **kwargs):

        queryset = Event.objects.all()
        contract_id = self.kwargs.get("contract_pk")
        try:
            contract = Contract.objects.get(id=contract_id)
        except Contract.DoesNotExist:
            raise NotFound('A Contract with this id does not exist')
        return queryset.filter(contract=contract)


class ContractViewset(ModelViewSet):

    permission_classes = [IsSalesAuthenticated]
    serializer_class = ContractSerializer

    def get_queryset(self, *args, **kwargs):

        queryset = Contract.objects.all()
        client_id = self.kwargs.get("client_pk")
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            raise NotFound('A Client with this id does not exist')
        return queryset.filter(client=client)