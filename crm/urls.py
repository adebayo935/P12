from django.contrib import admin
from django.urls import path, include
from listings.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('clients', ClientViewset, basename='clients')
router.register('users', UserViewset, basename='users')
router.register('register', SignUpView, basename="signup")

domains_router = routers.NestedSimpleRouter(router,'clients', lookup="client")
domains_router.register('contracts',ContractViewset, basename='client-contracts')

second_router = routers.NestedSimpleRouter(domains_router,'contracts', lookup="contract")
second_router.register('events',EventViewset, basename='contract-events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/', include(domains_router.urls)),
    path('api/', include(second_router.urls)),
]
