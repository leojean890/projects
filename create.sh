curl -i \
-H "Accept: application/json" \
-H "Content-Type:application/json" \
-X POST --data '{"name": "john", "status": "ACTIVE", "id":9}' "http://localhost:8080/insurances/"
