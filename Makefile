# 🜏 ~ John Murowaniecki Sant`Anna

-include .env
-include .assets/settings.mk

### COMMON COMMANDS

help: ## Show this help.
	@echo "$$(fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep \
	| sed -E 's/\\$$//;s/[#]{3} (.*$$)/\n\n\1\:\n/;s/(.*):.*#''# (.*)/\1:\2/g' \
	| awk -F':' '{ printf(($$1""$$2 != "" ? "$(BOLD)%-20s\1$(/BOLD)%s\n" :"\n"), $$1, $$2); }' )"

: ## \

start: ## Shortcut to `docker start …`.
	$(DOCKER_COMPOSE) up ${ENV_DOCKER_DETACHED} --remove-orphans $(ONLY)

stop: ## Shortcut to `docker stop …`.
	$(DOCKER_COMPOSE) stop $(ONLY)

restart: ## Shortcut to `docker restart …`.
	$(DOCKER_COMPOSE) restart $(ONLY)

down: ## Shortcut to `docker down …`
	$(DOCKER_COMPOSE) down $(ONLY)

: ## \

install: build ## Alias to build containers and other possible automatization…
build: ## Build containers - alias to `docker build …`.
	$(DOCKER_COMPOSE) build $(ENV_DOCKER_NO_CACHE) $(ONLY)

stats: ## Show container status - alias to `docker ps …`.
	$(DOCKER_COMPOSE) ps

clean: ## Remove containers, images and volumes - alias to `docker down …` with increments.
	$(DOCKER_COMPOSE) down --remove-orphans --rmi all --volumes

deploy: ## Uploads container to Docker Hub
	@docker build -t lambdadeveloper/tech2heal . -f Dockerfile
	@docker push lambdadeveloper/tech2heal

: ## \

ssh-%: ## Run SSH into desired service container.
	$(DOCKER_COMPOSE) run --entrypoint sh $*
: ## \
: ## Available containers are `application`, `mongo`, …
: ## For example use `make ssh-application` to access application console.

killsig:
	@kill -9 $$(ps aux | grep make | awk '{print($$2);}') > /dev/null
