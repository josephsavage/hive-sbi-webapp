import time, jwt
from django.conf import settings
from django.http import HttpResponse

def signed_dashboard_url(dashboard_id, params=None):
    payload = {
        "resource": {"dashboard": dashboard_id},
        "params": params or {},
        "exp": round(time.time()) + (60 * 10)  # expires in 10 minutes
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    return f"{METABASE_SITE_URL}/embed/dashboard/{token}#bordered=true&titled=true"

def dashboard_view(request):
    # Example: lock the filter to the logged-in user’s account
    url = signed_dashboard_url(2, {"account": request.user.username})
    iframe = f'<iframe src="{url}" width="100%" height="800" frameborder="0"></iframe>'
    return HttpResponse(iframe)
