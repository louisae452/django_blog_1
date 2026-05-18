from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the About page
    """
    toshow = About.objects.order_by("updated_on").first()
    return render(
        request,
        "about/about.html",
        {"about": toshow},
    )
    



# Create your views here.
