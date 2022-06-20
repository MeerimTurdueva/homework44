from django.urls import path

from webapp.views import game_calculation

urlpatterns = [
    path('', game_calculation)
]
