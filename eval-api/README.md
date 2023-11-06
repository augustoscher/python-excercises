# Python-API

Creating an rest api with python an poetry

## Running

First we need to configure virtual env and install dependencies:

```
make setup
```

Now, we're able to run api. Type:

```
poetry run uvicorn api.main:app --reload
```

or

```
make run-api
```

## Running unit tests

To run unit tests, type:

```
poetry run pytest
```

or

```
make test
```


## Docs

See the docs here: https://realpython.com/dependency-management-python-poetry/


#### Set python version to be used in virtual env

```
poetry env use python3
```

#### Check all virtual environments:

```
poetry env list
```
