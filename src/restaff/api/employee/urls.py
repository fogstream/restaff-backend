from django.urls import path

from restaff.api.employee import views

urlpatterns = [
    path('profile', views.ProfileView),
    path('skills', views.SkillsView),
    path('skills/<int:skill_id>/', views.SkillView),
    path('offers/', views.OffersView),
    path('offers/<int:offer_id>', views.OffersOneView),
    path('offers/<int:offer_id>/propose', views.OfferProposeView),
    path('position/<int:position_id>/propose/', views.PositionProposeView),
    path('positions/', views.PositionsView),
    path('positions/<int:position_id>', views.PositionsOneView),
    path('positions/<int:position_id>/subscribe', views.SubscribePositionView),
]