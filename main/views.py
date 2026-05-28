from django.shortcuts import redirect, render

from .forms import ContactRequestForm
from .models import (
    FAQ,
    Benefit,
    CalculatorSettings,
    FooterLink,
    NavItem,
    PricingPlan,
    Service,
    ServiceCompany,
    SiteSettings,
)


def home(request):
    return render(
        request,
        "home.html",
        {
            "nav_items": NavItem.objects.all(),
            "services": Service.objects.all(),
            "benefits": Benefit.objects.all(),
            "plans": PricingPlan.objects.all(),
            "footer_links": FooterLink.objects.all(),
        },
    )


def company_dashboard(request):
    settings = SiteSettings.objects.first()

    services = ServiceCompany.objects.all()

    faqs = FAQ.objects.all()

    calculator = CalculatorSettings.objects.first()

    if request.method == "POST":
        form = ContactRequestForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/")

    else:
        form = ContactRequestForm()

    context = {
        "settings": settings,
        "services": services,
        "faqs": faqs,
        "calculator": calculator,
        "form": form,
    }

    return render(request, "company_dashboard.html", context)


def ip_accounting(request):
    return render(
        request,
        "ip_accounting.html",
    )


def anime_store(request):
    return render(
        request,
        "anime_store.html",
    )
