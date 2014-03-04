#!/usr/bin/env python

import config
from app import app

app.run(host=config.APP_HOST, port=config.APP_PORT)
