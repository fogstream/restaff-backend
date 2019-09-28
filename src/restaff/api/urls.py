from django.urls import path, include

from restaff.api.employee import urls as employee_urls
from restaff.api.hr import urls as hr_urls
from restaff.api.expert import urls as expert_urls

urlpatterns = [
    path('employees/', include('restaff.api.employee.urls')),
    path('hr/', include('restaff.api.hr.urls')),
    path('expert/', include('restaff.api.expert.urls')),
]