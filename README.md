# issue-drf-stubs-response

## Setup 

`poetry install`

## Run mypy to reproduce the issue

`poetry run mypy .`

## Issue in question

https://github.com/typeddjango/djangorestframework-stubs/issues/204

## I don't want to use poetry.

That's fine.
There's a requirements.txt and for all commands remove the `poetry run` prefix.


## I don't want to install anything to reproduce the error.

That's fine.
There's a github action that reproduces it. Check the actions tab.
