from django.urls import path

from restaff.api.hr import views

urlpatterns = [
    path('stuff_orders', views.StaffOrdersView),
    path('stuff_orders/<int:staff_order_id>', views.StaffOrdersOne),
    path('stuff_orders/<int:staff_order_id>', views.StaffOrdersOne),
    path('stuff_orders/<int:staff_order_id>/make_demand', views.StaffOrderMakeDemand),
    path('stuff_orders/<int:staff_order_id>/archive', views.StaffOrdersArchiveOne),

    path('widget_stuff_orders', views.WidgetStaffOrders),
    path('widget_vacancy/', views.WidgetVacancyView),

    path('employees/', views.EmployeesView),
    path('employees/<int:employee_id>/profile', views.EmployeesProfileView),
    path('employees/<int:employee_id>/todo_list', views.EmployeesTodoListView),

    path('positions/', views.PositionsView),
    path('positions/<int:position_id>', views.PositionsOneView),
    path('positions/<int:position_id>/staff_orders', views.PositionStaffOrdersView),
    path('positions/<int:position_id>/proposes', views.PositionPadawanProgress),
    path('positions/<int:position_id>/padawan_progress', views.PositionPadawanProgress),

    path('experts', views.ExpertsView),
    path('experts/<int:expert_id>', views.ExpertsOneView),
    path('experts/<int:expert_id>/padawan_progress', views.ExpertsOnePadawanProgressView),
]