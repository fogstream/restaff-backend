from django.urls import path

from restaff.api.expert import views

urlpatterns = [
    path('padawans', views.Padawans.as_view()),
    path('padawans/<int:padawan_id>', views.PadawansOne.as_view()),
    path('padawans/<int:padawan_id>/todo_list', views.PadawanTodoListOne.as_view()),
    path('staff_orders', views.StaffOrdersView.as_view()),
    path('staff_orders/<int:staff_order_id>', views.StaffOrdersOneView.as_view())
]