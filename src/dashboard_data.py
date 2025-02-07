from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

def get_dashboard_data(api_key, app_key):
  configuration = Configuration()
  configuration.api_key["apiKeyAuth"] = api_key
  configuration.api_key["appKeyAuth"] = app_key


  with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    try:
      api_response = api_instance.get_dashboard("ni9-xjr-kx2")
      dashboard_json = api_response.to_dict()
      return dashboard_json
    except Exception as e:
      print(f"Error getting dashboard: {e}")
      return None

   
