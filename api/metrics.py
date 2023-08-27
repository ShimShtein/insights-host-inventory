from prometheus_client import Counter
from prometheus_client import Histogram
from prometheus_client import Summary
from prometheus_client import Gauge

api_request_time = Summary("inventory_request_processing_seconds", "Time spent processing request")
schema_validation_time = Summary("inventory_schema_validation_seconds", "Time spent validating System Profile schemas")
api_request_count = Counter("inventory_request_count", "The total amount of API requests")
login_failure_count = Counter("inventory_login_failure_count", "The total amount of failed login attempts")
outbound_http_response_time = Histogram(
    "inventory_outbound_http_response_time_seconds",
    "Time spent waiting for an external service to respond",
    ["dependency"],
)
host_cpu_count = Gauge('cpu_count', 'CPU count for hosts', ['subscription_manager_id'])