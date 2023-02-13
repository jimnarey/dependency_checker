#!/usr/env python3

import json
import requests

CABINET_OFFICE_ORG_URL = 'https://api.github.com/orgs/cabinetoffice/repos'

def get_repos(url):
    return requests.get(url).json()




