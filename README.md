# ml-system-study
Learning how to build and deploy ML systems

Run *n* instances of the app with load balancing by

`docker-compose up --scale app=n`

Connect to load balancer on localhost:80, powered by nginx

Query prediction for ticker id by GET on /predict/<ticker_id>

Example:
`GET localhost/predict/msft`

Query server logs by GET on /log/

`GET localhost/log/`