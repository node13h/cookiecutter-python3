# {{ cookiecutter.project_name }}


## Installing

```sh
pip install {{ cookiecutter.project_name }}
```


## Developing

Prerequisites:

- Python 3
- [pipenv](https://docs.pipenv.org/en/latest/#install-pipenv-today)

Initialize a virtualenv with dev dependencies installed:

```sh
make develop
```

### Project dependencies

Project dependencies shoud always be specified in `setup.py` using the [compatible release](https://www.python.org/dev/peps/pep-0440/#compatible-release) notation.


### Updating dependencies in virtualenv

Run the following after updating `setup.py`

```sh
make update-deps
```


### Installing development dependencies

Replace `<PACKAGE>` with the actual name, and `<VERSION>` with the MAJOR.MINOR (or MAJOR.MINOR.PATCH for versions below 1.0.0) version of the package. [Read more on compatible releases](https://www.python.org/dev/peps/pep-0440/#compatible-release).

```sh
pipenv install --dev <PACKAGE>~=<VERSION>
```


### Running unit-tests

```sh
make test
```


### Starting a release

```sh
make release-start
```


### Finishing a release

```sh
make release-finish
```


### Building and publishing the source distribution for the version X.Y.Z:

```sh
git checkout X.Y.Z
make publish
```
