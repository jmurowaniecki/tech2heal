# FastAPI Testing

![Python Alpine](https://img.shields.io/badge/Python-3.9.10-646464?style=for-the-badge&logo=python&labelColor=306998&logoColor=FFD43B)
![FastAPI](https://img.shields.io/badge/FastAPI-uvicorn-306998?style=for-the-badge&logo=fastapi&labelColor=646464&logoColor=FFD43B)


# Getting started

Copy `example.env` to `.env` and configure it.

Execute `make install start` to build and launch application. After installation use `start`, `stop` and another `make` listed commands to handle your environment. You can also see it working on the fly on [Heroku](https://tech2heal.herokuapp.com/).

> **Tip:** if you're using Windows, first install Makefile support running `choco install make --source=cygwin` on your favorite command interpreter.

## Installing on Linux environment

Using Makefile, the example above shows the execution of `make build start` command:

[![asciicast](https://asciinema.org/a/2NnMG5CGHSCyJielWr8aT4Qgy.svg)](https://asciinema.org/a/2NnMG5CGHSCyJielWr8aT4Qgy)

# First steps

Once your system is running you can access the address set (generally `http://localhost`) and it will present you with a JSON containing the environment in which the application is running and the configured collections.

To navigate between the endpoints of your application, use Swagger, via the url `http://localhost/docs` or Redocly via `http://localhost/redoc`.

![Swagger or Redoc](.assets/swagger-redoc.png)

Try it online by going to [Swagger](https://tech2heal.herokuapp.com/docs) or [Redocly](https://tech2heal.herokuapp.com/redoc) via the online platform via Heroku.

# Environment configuration

Setup environment variables above in your `.env` file:

```apache
DOCKER_NO_CACHE=N
# …To provide cache for build processes.
# Set `Y` to force build processes without cache.

DOCKER_DETACHED=Y
# …To execute start/up/launch commands silently… Or not.

DOCKER_OPTIONAL=Y
# …To append database to the project infraestructure.
```

> **Tip:**  Makefile `build` and `restart` commands allows to define targeted containers according to the following to build/rebuild only application container:
> ```sh
> ONLY=application make build
> ```

---

See more on

[![Github](https://img.shields.io/badge/Github-jmurowaniecki/Tech2heal-306998?style=for-the-badge&logo=github&labelColor=646464&logoColor=FFD43B)](https://github.com/jmurowaniecki/tech2heal)
[![Heroku](https://img.shields.io/badge/Heroku-Tech2heal.herokuapp-306998?style=for-the-badge&logo=Heroku&labelColor=646464&logoColor=FFD43B)](https://tech2heal.herokuapp.com/)
[![Docker Hub](https://img.shields.io/badge/Docker_Hub-lambdadeveloper/Tech2heal-306998?style=for-the-badge&logo=Docker&labelColor=646464&logoColor=FFD43B)](https://tech2heal.Dockerapp.com/)


