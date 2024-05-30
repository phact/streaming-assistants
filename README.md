# streaming_assistants

This library has been deprecated in favor of [astra-assistants](https://pypi.org/project/astra-assistants/) the repo has been moved in tree with the server code [here](https://github.com/datastax/astra-assistants-api/tree/main/client).

The latest version of streaming-assistants (v0.19.0) now pull in astra-assistants as a dependency and leverages that code. To upgrade simply switch from using streaming_assistants to astra_assistants.

> from streaming_assistants import patch

to

> from astra_assistants import patch

# Server

The astra-assistants server code is now open source (Apache2)! Check it out here https://github.com/datastax/astra-assistants-api
