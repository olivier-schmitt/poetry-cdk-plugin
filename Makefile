ifndef PIP_CMD
$(error PIP_CMD is not set)
endif

build:
	poetry build

publish: build
	poetry publish

install: build
	${PIP_CMD} uninstall poetry-cdk-plugin
	${PIP_CMD} install ./dist/poetry_cdk_plugin-*-py3-none-any.whl
