# Azure ML with Python - Sample

This sample uses [pyenv](https://github.com/pyenv/pyenv) and [pipenv](https://github.com/pypa/pipenv) to setup a sound python dev environment.

## Running the Sample

Create a `.env` file with the following contents:

```sh
# Get this from the Azure portal
SUBSCRIPTION_ID="<YOUR SUBSCRIPTION ID>"

# Get this from the Azure portal
RESOURCE_GROUP_NAME="test-rg"

# Name of your choice - if it doesn't exist, it will be created
WORKSPACE_NAME="test-ws"

# Or a region of your choice
REGION="northeurope"
```

Setup a >=3.7 python environment, e.g. via `pyenv`: `pyenv install 3.7.2`.

Finally, run the following commands:

```sh
pipenv install
python mlservice.py
```
