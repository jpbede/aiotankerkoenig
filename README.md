# aiotankerkoenig

[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE.md)

[![Build Status][build-shield]][build]
[![Code Coverage][codecov-shield]][codecov]

Asynchronous Python client for tankerkoenig.de.

## About

This package allows you to fetch data from tankerkoenig.de.

## Installation

```bash
pip install aiotankerkoenig
```

## Changelog & Releases

This repository keeps a change log using [GitHub's releases][releases]
functionality. The format of the log is based on
[Keep a Changelog][keepchangelog].

Releases are based on [Semantic Versioning][semver], and use the format
of ``MAJOR.MINOR.PATCH``. In a nutshell, the version will be incremented
based on the following:

- ``MAJOR``: Incompatible or major changes.
- ``MINOR``: Backwards-compatible new features and enhancements.
- ``PATCH``: Backwards-compatible bugfixes and package updates.

## Contributing

This is an active open-source project. I am always open to people who want to
use the code or contribute to it.

Thank you for being involved! :heart_eyes:

## Setting up development environment

This Python project is fully managed using the [Poetry][poetry] dependency manager. But also relies on the use of NodeJS for certain checks during development.

You need at least:

- Python 3.11+
- [Poetry][poetry-install]

To install all packages, including all development requirements:

```bash
poetry install
```

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

## Authors & contributors

The content is by [Jan-Philipp Benecke][jpbede].

For a full list of all authors and contributors,
check [the contributor's page][contributors].

## License

MIT License

Copyright (c) 2024 Jan-Philipp Benecke

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[build-shield]: https://github.com/jpbede/aiotankerkoenig/actions/workflows/release.yml/badge.svg
[build]: https://github.com/jpbede/aiotankerkoenig/actions
[codecov-shield]: https://codecov.io/gh/jpbede/aiotankerkoenig/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/jpbede/aiotankerkoenig
[commits-shield]: https://img.shields.io/github/commit-activity/y/jpbede/aiotankerkoenig.svg
[commits]: https://github.com/jpbede/aiotankerkoenig/commits/main
[contributors]: https://github.com/jpbede/aiotankerkoenig/graphs/contributors
[jpbede]: https://github.com/jpbede
[keepchangelog]: http://keepachangelog.com/en/1.0.0/
[license-shield]: https://img.shields.io/github/license/jpbede/aiotankerkoenig.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com/
[project-stage-shield]: https://img.shields.io/badge/project%20stage-stable-green.svg
[python-versions-shield]: https://img.shields.io/pypi/pyversions/aiotankerkoenig
[releases-shield]: https://img.shields.io/github/release/jpbede/aiotankerkoenig.svg
[releases]: https://github.com/jpbede/aiotankerkoenig/releases
[semver]: http://semver.org/spec/v2.0.0.html
[pypi]: https://pypi.org/project/aiotankerkoenig/
