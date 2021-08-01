#!/bin/bash

./manage.py dumpdata --natural-primary --natural-foreign --indent=2 users > users/fixtures.json
