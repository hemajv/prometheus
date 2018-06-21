#Test code for exporting metrics to localhost push gateway
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, Summary, Histogram, Counter, start_http_server
import os


registry = CollectorRegistry()
_PACKAGES_NEW = Gauge('packages_added','Packages newly added', registry=registry)

#Implement a logic for checking condition to increase gauge count
for i in range(10):
	#some logic for checking if any new packages have been added
	packages_added = True
	if packages_added==True:
		_PACKAGES_NEW.inc()

push_gateway = os.getenv('PROMETHEUS_PUSH_GATEWAY', '10.195.149.58:9091')
if push_gateway:
	try:
		push_to_gateway(push_gateway, job='package-releases', registry=registry)
	except Exception as e:
		print('An error occurred pushing the metrics: {}'.format(str(e)))
