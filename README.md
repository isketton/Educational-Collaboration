# Educational-Collaboration

Full-stack web application facilitating communication between teachers, parents, students, and clubs, providing real-time access to grades, announcements, and events using Django Knox to serve a REST API.


## Features

- Frontend: Interactive React dashboard for grades, messaging, etc.
- Backend: Python (Django) serving user information via REST API
- Docker: Features containerization to orchestrate nginx, Redis, Daphne(WSGI), Gunicorn(ASGI), and postgreSQL and pgadmin for the database, across multiple services
- Database: Stores user messages, grades, classes, etc. using PostgreSQL via Django's ORM


## Setup
```bash
git clone https://github.com/isketton/Educational-Collaboration.git

docker compose up -d


