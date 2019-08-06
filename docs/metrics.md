# Exporting Metrics

Metrics are very important to keep track of how your software is working. This will help you in keeping check on any unwanted things that went to production and impacted it.
One of the most important tools for metrics is prometheus that is very widely used by companies. We will try expose metrics for prometheus using python prometheus client. 

### Installation
pip install prometheus_client

### Code

<pre>
from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9000)
    # Generate some requests.
    while True:
        process_request(random.random())
</pre>

This will run a server on port 9000 and export metrics that prometheus will be able to consume. 

### Prometheus exporter with flask. 

You can do the same with you application written in flask using different client present for flask. https://pypi.org/project/prometheus-flask-exporter/ 

Read about it create an application with metrics. Ping me if you are stuck.