# doppler-env (experimental)

Automatically inject Doppler secrets as environment variables for use during local development if the `DOPPLER_ENV` environment variable is set.

Forked from and inspired by [patch-env](https://github.com/caricalabs/patch-env).

> NOTE: This package is experimental shoudl be used during local development only. It is not suitable, recommended, or supported for production usage.

## Use case

Debugging in IDE's such as Python and Visual Studio Code do not allow the Doppler CLI to be used as the process runner for Python.

This package proposes a solution in the form of a [site hook that is run for every Python startup](https://docs.python.org/3/library/site.html) and will inject secrets using a local installation of the Doppler CLI if the `DOPPLER_ENV` environment variable is set.

## Getting started

> NOTE: This presumes you've already [installed the Doppler CLI](https://docs.doppler.com/docs/enclave-installation) and have [created a project in Doppler](https://docs.doppler.com/docs/enclave-project-setup).

1. Ensure you've configured the Doppler CLI to select the project and config:

```sh
doppler setup
```

2. Install in `doppler-env` in your local development environment:

```sh
pip install git+https://github.com/dopplerhq/python-doppler-env.git#egg=doppler_env
```

3. On the command line or in your editor, set the environment variable `DOPPLER_ENV` to trigger injecting secrets as environment variables:


```sh
export DOPPLER_ENV=1
```

4. Run your application as per normal:

```sh
python src/app.py
```
