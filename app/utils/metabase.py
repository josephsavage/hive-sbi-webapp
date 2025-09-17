import time, jwt, os

METABASE_SITE_URL = os.environ.get("METABASE_SITE_URL")
METABASE_SECRET_KEY = os.environ.get("METABASE_SECRET_KEY")

def signed_dashboard_url(dashboard_id, params=None):
    payload = {
        "resource": {"dashboard": 2},
        "params": params or {},
        "exp": round(time.time()) + (60 * 10)
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    return f"{METABASE_SITE_URL}/embed/dashboard/{token}#bordered=true&titled=true"
