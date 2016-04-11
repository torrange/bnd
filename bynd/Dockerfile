FROM phusion/baseimage
MAINTAINER Tobias Jone <tobiasjone@gmail.com> 

CMD ["python", "manage.py", "runserver"]

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y python \
	python-pip \
	python-lxml \
	python-defusedxml \
    && pip install django==1.9.5 \
	django-tastypie==0.13.3


COPY hashtag_battles /hashtag_battles 


WORKDIR /hashtag_battles
