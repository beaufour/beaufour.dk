#!/usr/bin/env python
#
# Silly little script to download the list of my repos and print the
# html. Need to be integrated into the build process of Cactus.
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import sys

import requests


def main():
    repos = requests.get('https://api.github.com/users/beaufour/repos')

    data = repos.json()
    out = []
    for entry in data:
        if entry['private']:
            continue

        out.append('  <dt><a href="{0}">{1}</a></dt>'.format(entry['html_url'], entry['name']))
        out.append('  <dd>{0}{1}</dd>'.format(entry['description'], " <i>(fork)</i>" if entry['fork'] else ""))
        out.append('')
    print('\n'.join(out))

if __name__ == '__main__':
    sys.exit(main())
