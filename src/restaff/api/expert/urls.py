from django.urls import path

from restaff.api.expert import views

urlpatterns = [
    path('padawans', views.Padawans),
    path('padawans/<int:padawan_id>', views.PadawansOne),
    path('padawans/<int:padawan_id>/todo_list', views.PadawanTodoListOne),
    path('staff_orders', views.StaffOrdersView),
    path('staff_orders/<int:staff_order_id>', views.StaffOrdersOneView)
]