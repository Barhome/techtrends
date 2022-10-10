## Packaging Docker Application

- Change your directory to /techtrends where the Dockerfile is located

- run the command `docker build -t techtrends .` to spin up a docker container

- to run docker container in a detached mode and on port 7111 on your host run the command `docker run -d -p 7111:3111 techtrends`

- Test that the app is running on your host by hitting `http://localhost:7111/` in your browser

## Here is a screenshot of the app running locally:

![](screenshots/docker-run-local.png)

## The docker logs command After adding logging functionalities metrics endpoint as a best practice in the development process we should check on that by doing the following:

- get the container ID by running the command `docker ps`

- retrieve the docker logs using container id c8633365188e by running the command `docker logs c8633365188e`

- You will get the following logs:

Serving Flask app "app" (lazy loading)
Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
Debug mode: off
Monday, 10/Oct/2022 at, 18:31:49 PM \* Running on http://0.0.0.0:3111/ (Press CTRL+C to quit)
Monday, 10/Oct/2022 at, 18:32:01 PM 172.17.0.1 - - [10/Oct/2022 18:32:01] "GET / HTTP/1.1" 200 -
Monday, 10/Oct/2022 at, 18:32:01 PM 172.17.0.1 - - [10/Oct/2022 18:32:01] "GET /static/css/main.css HTTP/1.1" 200 -
Monday, 10/Oct/2022 at, 18:32:01 PM 172.17.0.1 - - [10/Oct/2022 18:32:01] "GET /favicon.ico HTTP/1.1" 404 -
Monday, 10/Oct/2022 at, 18:32:35 PM 172.17.0.1 - - [10/Oct/2022 18:32:35] "GET / HTTP/1.1" 200 -
Monday, 10/Oct/2022 at, 18:36:43 PM The "About Us" page is retrieved
Monday, 10/Oct/2022 at, 18:36:43 PM 172.17.0.1 - - [10/Oct/2022 18:36:43] "GET /about HTTP/1.1" 200 -
Monday, 10/Oct/2022 at, 18:37:28 PM The "About Us" page is retrieved
Monday, 10/Oct/2022 at, 18:37:28 PM 172.17.0.1 - - [10/Oct/2022 18:37:28] "GET /about HTTP/1.1" 200 -
Monday, 10/Oct/2022 at, 18:38:57 PM 172.17.0.1 - - [10/Oct/2022 18:38:57] "GET /healthz HTTP/1.1" 200 -
Monday, 10/Oct/2022 at, 18:45:16 PM 172.17.0.1 - - [10/Oct/2022 18:45:16] "GET /healthz HTTP/1.1" 200 -
Monday, 10/Oct/2022 at, 18:45:19 PM 172.17.0.1 - - [10/Oct/2022 18:45:19] "GET /healthz HTTP/1.1" 200 -

## Continuous Integration With Github actions

- Create a configration file named techtrends-dockerhub.yaml in .github/workflows/ directory as in the project
- Create dockerhub token and github encrypted secrets that will be used inside of the configration file
- upon pushing new commits to github the configration file will the dockerhub token and github secrets to log in dockerhub and push new images.

## Here are screenshots of successful github action and new image on dockerhub

![](screenshots/ci-github-actions.png)
![](screenshots/ci-dockerhub.png)

## Kubernetes Declarative Manifests

- run `vagrant up` in the directory that contains the vagrant file , The vagrant file has a command for automatically bootstrapping the kubernetes cluster using k3s
- run `vagrant ssh` and use `sudo su` to become root and use kubectl commands
- verify if th the kubernetes cluster is operational by evaluating the node status in the cluster to be up and running

## Here is a screenshot of k8s node :

![](screenshots/k8s-nodes.png)
