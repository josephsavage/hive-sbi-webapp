from django.shortcuts import render
from .utils.metabase import signed_dashboard_url

def rich_list(request):
    iframe_url = signed_dashboard_url(5)  # replace 5 with your dashboard ID
    return render(request, "rich_list.html", {"iframe_url": iframe_url})
