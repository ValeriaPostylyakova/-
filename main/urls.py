from django.urls import path

from .views import anime_store, company_dashboard, home, ip_accounting

urlpatterns = [
    path("", home, name="home"),
    path("company-dashboard/", company_dashboard, name="company_dashboard"),
    path("ip-accounting/", ip_accounting, name="ip_accounting"),
    path("anime-store/", anime_store, name="anime_store"),
]
