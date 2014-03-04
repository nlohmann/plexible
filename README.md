# Plexible

Plexible is a tool to make your [Plex](https://plex.tv) media library browsable for remote users.


## Bootstrapping

### Prerequisites

To get Plexible running, you need the following software:

- Python
- virtualenv

With Homebrew running on OS X, installing these prerequisites is simple:

    brew install python
    pip install virtualenv

On Debian or Ubuntu Linux, the same can be achieved with

    sudo apt-get install python
    sudo apt-get install python-virtualenv

### Install

The code can be set up by:

    make install

Which sets up a virtual environment and installs further Python packages.

### Configuration

Before you run Plexible the first time, please review the file `config.py`. It contains several standard settings and should be OK for most cases. In particular, check the following settings:

- `SERVER_NAME` determines where Plexible should be reachable.
- `PLEX_SERVER_NAME` is the location of your Plex Media Server.

## Run Plexible

You can start a server by running

    make start

Plexible should then be reachable at the server and port configured as `SERVER_NAME` in file `config.py`. In the default setting, you can point your browser to http://localhost:1337/sections to browse your Plex sections.
