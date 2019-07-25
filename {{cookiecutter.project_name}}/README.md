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

Project dependencies shoud always be specified in `setup.py` using the
[compatible release](https://www.python.org/dev/peps/pep-0440/#compatible-release)
notation.


### Updating dependencies in virtualenv

Run the following after updating `setup.py`

```sh
make update-deps
```


### Installing development dependencies

Replace `<PACKAGE>` with the actual name, and `<VERSION>` with the MAJOR.MINOR
(or MAJOR.MINOR.PATCH for versions below 1.0.0) version of the package.
[Read more on compatible releases](https://www.python.org/dev/peps/pep-0440/#compatible-release).

```sh
pipenv install --dev <PACKAGE>~=<VERSION>
```


### Running unit-tests

```sh
make test
```


### Starting a release

Variables:

- `RELEASE_REMOTE` set to the name of the Git remote. Set to empty to disable pushes to
remote. Default value: `origin`
- `RELEASE_VERSION` override the release version, or leave empty to release the current
snapshot (`-SNAPSHOT` will be stripped off). Empty by default

```sh
make release-start
```


### Finishing a release

Variables:

- `RELEASE_REMOTE` set to the name of the Git remote. Set to empty to disable pushes to
remote. Default value: `origin`
- `RELEASE_PUBLISH` set to `1` to enable publishing of the sdist tarball after the release`

```sh
make release-finish
```

`release-finish` will leave the release Git tag checked out on completion.


### Building and publishing the source distribution:

```sh
make publish
```
