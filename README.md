### Requirements
1. Install python prometheus_client
```
     pip install prometheus_client
```
2. Install the push gateway from https://prometheus.io/download/#pushgateway

### How to run the push gateway:
1. Change to the directory where your pushgateway is installed
```
   	cd pushgateway-0.5.1.linux-amd64/
```
2. Start the pushgateway
```
   	./pushgateway
```
3. Check if the port is activated via your browser. The default port for the push gateway is 9091.
```
     https://localhost:9091
```
