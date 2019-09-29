from django.urls import path

from restaff.api.employee import views

urlpatterns = [
    path('profile/', views.ProfileView().as_view()),
    path('skills/', views.SkillsView().as_view()),
    path('skills/<int:skill_id>/', views.SkillView().as_view()),
    path('offers/', views.OffersView().as_view()),
    path('offers/<int:offer_id>/', views.OffersOneView().as_view()),
    path('offers/<int:offer_id>/propose/', views.OfferProposeView().as_view()),
    path('position/<int:position_id>/propose/', views.PositionProposeView().as_view()),
    path('positions/', views.PositionsView().as_view()),
    path('positions/<int:position_id>/', views.PositionsOneView().as_view()),
    path('positions/<int:position_id>/subscribe', views.SubscribePositionView().as_view()),
]