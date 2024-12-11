from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name='homepage'),
      path('login/', login_view, name='login'), 
        path('register/', register, name='register'), 
        path('contact/', contact, name='contact'), 
           
    path('dashboard/vendor/', dashboard_ven, name='dashboard_ven'),
    path('dashboard/businessman/', dashboard_bus, name='dashboard_bus'),
    path('dashboard/person/', dashboard_pers, name='dashboard_pers'),
          # This should route to your homepage view
]
