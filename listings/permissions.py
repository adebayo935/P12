from rest_framework.permissions import BasePermission
from .models import *
 
class IsManagerAuthenticated(BasePermission):
 
    def has_permission(self, request, view):
    
        if request.method == "GET":
            return bool(request.user and request.user.is_authenticated)
        else:
            if request.user.team == "Management":
                return True
            else: 
                return False

    def has_object_permission(self, request, view, obj):

        if request.user.team == "Management":
            return True
        else: 
            return False

class IsSalesAuthenticated(BasePermission):
 
    def has_permission(self, request, view):
    
        if request.method == "GET":
            return bool(request.user and request.user.is_authenticated )
        elif request.user.team == "Management":
                return True
        elif request.user.team == "Sales": 
            client = Client.objects.filter(id=obj.id)
            if client[0].sales_contact == request.user:
                return True
        else: 
            return False

    def has_object_permission(self, request, view, obj):

        if request.user.team == "Management":
            return True
        elif request.user.team == "Sales": 
            client = Client.objects.filter(id=obj.id)
            if client[0].sales_contact == request.user:
                return True
        else: 
            return False


class IsSupportAuthenticated(BasePermission):
 
    def has_permission(self, request, view):
    
        contract = Contract.objects.filter(id=request.data['contract'])
        if contract[0].status == "signed":
            if request.method == "GET":
                return bool(request.user and request.user.is_authenticated )
            elif request.user.team == "Management":
                return True
            elif request.user.team == "Sales":
                client = Client.objects.filter(id=event.client)
                if request.user == client.sales_contact:
                    return True
            else:
                return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
  
        if request.user.team == "Management":
            return True
        elif request.user.team == "Sales":
            client = Client.objects.filter(id=event.client)
            if request.user == client.sales_contact:
                return True
        elif event[0].support_contact == request.user:
                return True
        else: 
            return False