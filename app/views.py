import argparse
from app import app
from flask import render_template

import requests
import json

# set all available config arguments
parser = argparse.ArgumentParser()
parser.add_argument("--plex_address", "-a", help="set address of plexinstance", default="127.0.0.1")
parser.add_argument("--plex_port", "-p", help="set port of plexinstance", default="32400")
args = vars(parser.parse_args())

# the URL for the Plex Media Server
BASEURL = 'http://%(address)s:%(port)s' % {"address": args.get('plex_address'), "port": args.get('plex_port')}

def get(path):
    """
    Collect data from the Plex Media Server given a path of the API and return
    it as dictionary.
    """
    url = BASEURL + path
    r = requests.get(url, headers={"Accept": "application/json"})

    # fix JSON object - result can actually be broken
    data = json.loads(r.text.replace("}{", "},{"))

    return data


@app.route('/sections')
def sections():
    data = get('/library/sections')
    return render_template("sections.html", data=data)

@app.route('/sections/<section_id>')
def section(section_id):
    data = get('/library/sections/' + section_id + '/all')
    return render_template("section.html", data=data)

@app.route('/entries/<entry_id>')
def entry(entry_id):
    data = get('/library/metadata/' + entry_id + '/children')
    full_data = get('/library/metadata/' + entry_id)['_children'][0]
    return render_template("entry.html", data=data, full_data=full_data, nice_data=json.dumps(full_data, indent=2))

@app.route('/file/<entry_id>/<int:file_id>')
def file(entry_id, file_id):
    full_data = get('/library/metadata/' + entry_id)['_children'][0]
    filename = full_data['_children'][0]['_children'][file_id]['file']

    # FIXME: works only for unix-systems AND when script runs on same machine
    # serve file as static (strip trailing slash - it is added by the static
    # folder which is '/')
    return app.send_static_file(filename[1:])
