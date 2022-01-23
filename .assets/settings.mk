
ENV_DOCKER_OPTIONAL := $(if $(findstring Y,${DOCKER_OPTIONAL}),-f ./docker-compose.optional.yaml,)
ENV_DOCKER_NO_CACHE := $(if $(findstring Y,${DOCKER_NO_CACHE}),--no-cache,)
ENV_DOCKER_DETACHED := $(if $(findstring Y,${DOCKER_DETACHED}),-d,)

#
# Not working as expected? See 0x022 specification on https://compilou.com wiki.
#
ifneq ($(ONLY),)
ENV_DOCKER_OPTIONAL :=
endif

DOCKER_FILEYML := ./docker-compose.${APP_ENV}.yaml
DOCKER_COMPOSE := docker-compose -f $(DOCKER_FILEYML) $(ENV_DOCKER_OPTIONAL)



ifneq ($(APP_ENV),production)
ifneq ($(APP_ENV),homolog)
NODE_NPM_DEV := --include=dev
COMPOSER_DEV := --dev
endif
endif



ifeq ($(OS),Windows_NT)
BORING_MODE := Y
endif



ifeq ($(BORING_MODE),)
 BOLD = \033[1m
/BOLD = \033[0m
Style = | sed -E 's/!([A-Z]+)/\\033[0;2;3m\1\\033[0m/g;s/(`[0-9a-zA-Z …\.\-]*`|\$$\(.*\))/\\033[33m\1\\033[0m/g;s/(DEPRECATED)/\\033[0;31m\1\\033[0m/'
endif
