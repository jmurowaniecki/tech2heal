# Testing FastAPI

![Python Alpine](https://img.shields.io/badge/Python-3.10.2-646464?style=for-the-badge&logo=python&labelColor=306998&logoColor=FFD43B)
![FastAPI](https://img.shields.io/badge/FastAPI-v7-306998?style=for-the-badge&logo=fastapi&labelColor=646464&logoColor=FFD43B)


# Getting started

Copy `example.env` to `.env` and configure it.

Execute `make install start` to build and launch application. After installation use `start`, `stop` and another `make` listed commands to handle your environment.

> **Tip:** if you're using Windows, first install Makefile support running `choco install make --source=cygwin` on your favorite command interpreter.



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
