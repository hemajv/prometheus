from prometheus_client import Summary, start_http_server, Counter, Gauge, Histogram
import time
import random

start_http_server(8000)
#Counter
c = Counter('my_failures_total', 'Total failures')
c.inc()

#Gauge
g = Gauge('my_inprogress_requests', 'Progress requests')
g.inc()
g.dec(5)
g.set(4.1)
g.set_to_current_time()

#Summary
s = Summary('request_latency_seconds', 'Latency seconds')
s.observe(4.5)

#Histogram
#h = Histogram('request_latency_seconds', 'Description of histogram')
#h.observe(4.5)


