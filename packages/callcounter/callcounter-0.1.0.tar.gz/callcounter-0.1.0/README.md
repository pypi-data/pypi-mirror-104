# Callcounter Python integration pip package

This package can be used to gather API request & response data from Rack based applications and send it to Callcounter.

Callcounter is an API analytics platform that collect information about requests (calls) to your API using so-called
integrations. Integrations come in the form of a Ruby gem, a Nuget package, a Pip module, etcetera. The integrations
can send the data to Callcounter using an API, which is described at: https://callcounter.eu/pages/api

After collection data, the web interface can then be used to view all kinds of metrics, giving you insight in the
(mis)usage of your API.

## Install

Install the package with pip: `pip install callcounter`.

## Configure what to capture

In you django `settings.py` add the following lines:

```python
import callcounter

callcounter.project_token = '' # TODO: fill with your unique project token
```

And add the middleware to the `MIDDLEWARE` array in the same settings.py:

```python
MIDDLEWARE = [
    # other middleware kept here
    'callcounter.middleware.Capturer',
]
```

This will capture any requests to the `api` subdomain and any request that has a path which starts with `/api`.
After deploying you should start seeing data in Callcounter. Note that this might take some time because this gems
only sends data every few requests or every few minutes.

If you API doesn't match with the default matching rules, you can add a lambda that will be called for every request
to determine whether it was a request to your API. For example, you can customize the default lambda shown below:

```python
callcounter.track = lambda request: request.get_host().startswith('api.') or request.path.startswith('/api')
```

## Bug reporting

Bugs can be reported through the Sourcehut todo lists found at: https://todo.sr.ht/~webindie/callcounter-pip
If you don't want to sign up for an account, you can also contact us through https://callcounter.eu/contact

## Releasing

- Verify tests pass.
- Increment version number in: `callcounter/__init__.py`
- Commit all changes.
- Create a git tag for the release.
- Push the git tag.
- Build the package: `python3 -m build`
- Push the package to pypi.org: `python3 -m twine upload dist/*`

## About Callcounter

[Callcounter](https://callcounter.eu) is a service built by [Webindie](https://webindie.nl) that
helps API providers with debugging and optimising the usage of their APIs.
