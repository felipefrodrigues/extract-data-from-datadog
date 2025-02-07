from dashboard_data import get_dashboard_data
from widget_data import get_widget_data


def get_metric():
  from_ts = 1738749600000
  to_ts = 1738753200000
  widget_id = YOUR_WIDGET_ID
  api_key = YOUR_API_KEY
  app_key = YOUR_APP_KEY

  dashboard_json = get_dashboard_data(api_key, app_key)
  widget_data = get_widget_data(
    dashboard_json,
    widget_id,
    from_ts,
    to_ts,
    api_key,
    app_key
  )

  if widget_data:
      return widget_data
  return {}


