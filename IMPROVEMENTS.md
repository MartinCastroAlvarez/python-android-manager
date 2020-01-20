# Improvements
This section contains the answers to the extra questions in the technical challenge.

##### The application can be improved with features which, most of them, are implemented [here](https://github.com/MartinCastroAlvarez/iguazu) in one of my other repositories. It includes:

- Higher test coverage using [Unit Tests](https://en.wikipedia.org/wiki/Unit_testing) and [Integration Tests](https://en.wikipedia.org/wiki/Functional_testing).
- [Docker](https://www.docker.com/). It can be used to virtualize the application environment. In the application mentioned, it uses [docker-compose](https://docs.docker.com/compose/) to setup the required dependencies.
- [Celery](http://www.celeryproject.org/) worker to run tasks in the background.
- A [notification system](https://en.wikipedia.org/wiki/Push_technology) that can be used to check the status of the tests.
- [Redis](https://redis.io/). It can be used, together with [this](https://github.com/gabfl/redis-priority-queue) repository to provide a [Priority Queue](https://en.wikipedia.org/wiki/Priority_queue). Then, it can be used to, given a set of scarce resources, decide which test to run next.
- [Authentication](https://flask-login.readthedocs.io/en/latest/). [Google OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2) can be used to access Google APIs.

##### In order to ship to production, the following services can be used:

- [AWS S3](https://aws.amazon.com/s3/) can be used to upload and store the APKs, partitioned by owner, application and version.
- [AWS ECS](https://aws.amazon.com/ecs/) can be used to ship and scale multiple instances of the web server.
- [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) is required to overcome the [issue](https://wiki.python.org/moin/GlobalInterpreterLock) with multi-threading in Python.
- Detect currently opened app using [these](https://stackoverflow.com/questions/16691487/how-to-detect-running-app-using-adb-command) instructions.
- Accessing USB device over the network using [this](http://www.usb-over-network.com/) tool.
