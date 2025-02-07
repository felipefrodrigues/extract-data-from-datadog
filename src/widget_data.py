from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.query_formula import QueryFormula
from datadog_api_client.v2.model.scalar_formula_query_request import ScalarFormulaQueryRequest
from datadog_api_client.v2.model.scalar_formula_request import ScalarFormulaRequest
from datadog_api_client.v2.model.scalar_formula_request_attributes import ScalarFormulaRequestAttributes
from datadog_api_client.v2.model.scalar_formula_request_queries import ScalarFormulaRequestQueries
from datadog_api_client.v2.model.scalar_formula_request_type import ScalarFormulaRequestType
from datadog_api_client.v2.model.events_compute import EventsCompute
from datadog_api_client.v2.model.events_scalar_query import EventsScalarQuery
import json

def get_widget_data(dashboard_json, widget_id, from_ts, to_ts, api_key, app_key):
  widget = next((w for w in dashboard_json.get("widgets", []) if w.get("id") == widget_id), None)
  configuration = Configuration()
  configuration.api_key["apiKeyAuth"] = api_key
  configuration.api_key["appKeyAuth"] = app_key

  queries_data = widget['definition']['requests'][0]['queries']
  formulas_data = widget['definition']['requests'][0]['formulas']
  formulas = []
  queries = []

  for q in queries_data:
    query_object = EventsScalarQuery(
      compute=EventsCompute(
        aggregation=q["compute"]["aggregation"],
        metric=q["compute"]["metric"]
      ),
      data_source=q["data_source"],
      name=q["name"],
      search= {
        "query": q["search"]["query"]
      },
      group_by=q["group_by"]
    )
    queries.append(query_object)


  for f in formulas_data:
    formula_object = QueryFormula(
      formula=f["formula"]
    )
    formulas.append(formula_object)
  
  with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    body = ScalarFormulaQueryRequest(
      data=ScalarFormulaRequest(
        attributes=ScalarFormulaRequestAttributes(
          formulas=formulas,
          _from=from_ts,
          queries=ScalarFormulaRequestQueries(queries),
          to=to_ts,
        ),
      type=ScalarFormulaRequestType.SCALAR_REQUEST
    ))
    response = api_instance.query_scalar_data(body=body)
  
  if response and response.data and response.data.attributes:
    results = {}
    attributes = response.data.attributes

    if attributes.columns:
      for column in attributes.columns:
        results[column.name] = column.values
    return json.dumps(results)

  return json.dumps({})
    




  
