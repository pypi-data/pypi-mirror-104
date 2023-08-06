# Callcounter Python integration pip package

This package can be used to gather API request & response data from Rack based applications and send it to Callcounter.

Callcounter is an API analytics platform that collect information about requests (calls) to your API using so-called
integrations. Integrations come in the form of a Ruby gem, a Nuget package, a Pip module, etcetera. The integrations
can send the data to Callcounter using an API, which is described at: https://callcounter.eu/pages/api

After collection data, the web interface can then be used to view all kinds of metrics, giving you insight in the
(mis)usage of your API.

## Bug reporting

Bugs can be reported through the Sourcehut todo lists found at: https://todo.sr.ht/~webindie/callcounter-pip
If you don't want to sign up for an account, you can also contact us through https://callcounter.eu/contact

## Releasing

- Verify tests pass.
- Increment version number in: `setup.cfg`
- Commit all changes.
- Create a git tag for the release.
- Push the git tag.
- Build the package: `python3 -m build`
- Push the package to pypi.org: `python3 -m twine upload dist/*`

## About Callcounter

[Callcounter](https://callcounter.eu) is a service built by [Webindie](https://webindie.nl) that
helps API providers with debugging and optimising the usage of their APIs.
