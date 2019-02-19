# Header Metadata Routing

This example demonstrates how to pick a subset of endpoints by matching the endpoint
metadata against a request header.

This example launches 5 nodes:
- front proxy running envoy
- 1 backend instance with owner=kramer
- 1 backend instance with owner=newman
- 2 backend instance with owner=PUBLIC

# Commands

```
$ docker-compose up --build -d

$ docker-compose ps

$ docker-compose down
```

# Sending Traffic

```
Route to any endpoint with owner=PUBLIC in dora cluster:
$ curl -sv localhost:8000/service/dora

Route to an endpoint in dora cluster with metadata owner=kramer:
$ curl -sv localhost:8000/service/dora -H 'namespace: kramer'

Route to an endpoint in dora cluster with metadata owner=newman:
$ curl -sv localhost:8000/service/dora -H 'namespace: newman'

These route based on hardcoded metadata_match within the routes:
$ curl -sv localhost:8000/service/dora/kramer
$ curl -sv localhost:8000/service/dora/newman
```
