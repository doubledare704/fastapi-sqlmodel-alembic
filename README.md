# FastAPI + SQLModel + Alembic

Sample FastAPI project that uses async SQLAlchemy, SQLModel, Postgres, Alembic, and Docker.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/fastapi-sqlmodel/).

## Want to use this project?

```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```

Sanity check: [http://localhost:8004/ping](http://localhost:8004/ping)

Add a hero:

```sh
$ curl -d '{"name":"Midnight Fit", "secret_name":"Mogwai", "age":"30"}' -H "Content-Type: application/json" -X POST http://localhost:8004/heroes
```

Get all songs: [http://localhost:8004/heroes](http://localhost:8004/heroes)

Changelog for my fork of original FastAPI + SQLModel + Alembic boilerplate:
* Used test model from sqlmodel example
* Updated packages
* Updated codebase to use new Model, stop using deprecated code (async engine in sqlmodel is not available now, used alchemy instead)
* Updated postgresql image version
* Renamed source folder to backend (for cases if someone uses monorepo for front-end and backend)

Plan to update this repo from time to time.

Features to implement:
* Separate DB queries from routers methods (start using db repository classes)
* add testing folder and settings
* add visual docs folder with auto-generation of uml class models