# ml-system-study
Learning how to build and deploy ML based systems. 
The system is intended to serve predictions of stock prices based on Yahoo finance data.
User queries the ticker id, e.g. MSFT and receives the predicted future value, generated with an underline machine learning model.
Predictions are cached to reduce the number of calls to an exernal Yahoo finance API.

API is powered by Flask, caching and logging are implemented using Redis. 
There is load balancing with nginx as a balancer. Docker-compose is used as a container orchestration tool
to coordinate Redis, nginx and several app containers. 

Several models imlpementing the same abstract class are available for user.

Basic CI / CD workflow is implemented with GitHub actions. build_test.yml runs unit tests,
publish.yml builds Docker image out of application code and pushes it to the registry.
After that the application is automatically deployed on Google Cloud Platform. 

Run the app with *n* servers in rotation by
`docker-compose up --scale app=n`

Query prediction for ticker id by GET on /predict/<ticker_id>

Example:
`GET localhost/predict/msft`

Query server logs by GET on /log/, query parameter _count_ limits the output size

`GET localhost/log/?count=20`