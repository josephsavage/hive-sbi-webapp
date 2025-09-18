from django.shortcuts import render
from .utils.metabase import signed_dashboard_url

def richlist_view(request):
    iframe_url = "https://www.hivesbi.com/richlist/"
    return render(request, "richlist.html", {"iframe_url": iframe_url})
