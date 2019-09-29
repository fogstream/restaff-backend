from django.urls import path

from restaff.api.hr import views

urlpatterns = [
    path('stuff_orders/', views.StaffOrdersView.as_view()),
    path('stuff_orders/<int:staff_order_id>/', views.StaffOrdersOne.as_view()),
    path('stuff_orders/<int:staff_order_id>/make_demand/', views.StaffOrderMakeDemand.as_view()),
    path('stuff_orders/<int:staff_order_id>/archive/', views.StaffOrdersArchiveOne.as_view()),

    path('widget_stuff_orders/', views.WidgetStaffOrders.as_view()),
    path('widget_vacancy/', views.WidgetVacancyView.as_view()),

    path('employees/', views.EmployeesView.as_view()),
    path('employees/<int:employee_id>/profile', views.EmployeesProfileView.as_view()),
    path('employees/<int:employee_id>/todo_list', views.EmployeesTodoListView.as_view()),

    path('positions/', views.PositionsView.as_view()),
    path('positions/<int:position_id>/', views.PositionsOneView.as_view()),
    path('positions/<int:position_id>/staff_orders', views.PositionStaffOrdersView.as_view()),
    path('positions/<int:position_id>/proposes', views.PositionProposesView.as_view()),
    path('positions/<int:position_id>/padawan_progress', views.PositionPadawanProgress.as_view()),
    path('proposes/<int:propose_id>/accept', views.PositionPadawanProgress.as_view()),

    path('experts', views.ExpertsView.as_view()),
    path('experts/<int:expert_id>/', views.ExpertsOneView.as_view()),
    path('experts/<int:expert_id>/padawan_progress/', views.ExpertsOnePadawanProgressView.as_view()),
]