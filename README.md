# Django + Stripe API

___

### Description

This project includes developed little API for interaction with Stripe platform manager,where:

___

### Requirements

This project requires Python, SQLite, Docker
___

### Deployment

1) You need to have installed Docker, Docker-compose .
2) Clone Git repo:

> $ git clone https://github.com/MikitaYeudakimau/rishan_test.git .

3) Build the images and run containers (in my case only web container, because SQLite db is just a file):

> $ docker-compose up -d --build

4) Use admin rights to fill database (login:passowrd | admin:admin).
5) Test it out at http://localhost:8000.
---
Bonus tasks implemented:

1) Docker
2) .env (this file is not ignored for git, if you want to start it local)
3) models in admin panel
4) server deployment

You can check this API at https://nikevdokimov.pythonanywhere.com/

