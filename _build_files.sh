#!/bin/bash
source .venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
