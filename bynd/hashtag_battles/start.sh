#!/bin/sh
python manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 & \
python manage.py shell < twitter_queue.py 
