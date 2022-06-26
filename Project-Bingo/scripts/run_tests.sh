#!/bin/sh

coverage run --source=. -m unittest discover -v -s tests/ -p "*_test.py"
coverage report -m --omit=tests/*,*__init__.py