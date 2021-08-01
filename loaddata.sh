#!/bin/bash

echo
echo 'Load users...'
./manage.py loaddata users/fixtures.json
