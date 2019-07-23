PROJECT := {{ cookiecutter.project_name }}
VERSION = $(shell cat VERSION)
SDIST_TARBALL = dist/$(PROJECT)-$(VERSION).tar.gz

.PHONY: all clean develop shell lint test update-deps release-start release-finish sdist publish

all:

clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	pipenv --rm || true

develop:
	pipenv install --dev

shell:
	pipenv shell

lint:
	pipenv run flake8 --max-line-length=119 --exclude=.git,__pycache__,.tox,.eggs,*.egg

test: lint
	pipenv run pytest --verbose

update-deps:
	pipenv update

release-start: test
	pipenv run lase --remote origin start $${RELEASE_VERSION:+--version "$${RELEASE_VERSION}"}

release-finish:
	pipenv run lase --remote origin finish

sdist: assets $(SDIST_TARBALL)

$(SDIST_TARBALL):
	python3 setup.py sdist

publish: test $(SDIST_TARBALL)
	pipenv run twine upload $(SDIST_TARBALL)

