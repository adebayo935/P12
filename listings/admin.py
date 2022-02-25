from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'team','is_active','is_staff')
    list_filter = ('username', 'team','is_active','is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'team',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'team','is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

class CustomClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('id','first_name','last_name','email','mobile','phone','company_name','sales_contact')
    list_filter = ('id','first_name','last_name','email','mobile','phone','company_name','sales_contact')

class CustomEventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('id','name','client','support_contact','status','attendees','date_event','notes','created_time','updated_time')
    list_filter = ('id','name','client','support_contact','status','attendees','date_event','notes','created_time','updated_time')

class CustomContractAdmin(admin.ModelAdmin):
    model = Contract
    list_display = ('id','client','amount','sales_contact','status','created_time','updated_time')
    list_filter = ('id','client','amount','sales_contact','status','created_time','updated_time')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Client, CustomClientAdmin)
admin.site.register(Event, CustomEventAdmin)
admin.site.register(Contract, CustomContractAdmin)