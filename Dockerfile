FROM python:3.9.6

ENV PYTHONUNBUFFERED 1

RUN useradd wagtail

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends apt-utils \
    mc \
    htop \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    postgresql-client \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN python -m pip install pip==21.2.2

COPY requirements.txt /
RUN pip install --no-cache-dir -Ur requirements.txt

ADD . /app

WORKDIR /app
RUN chown wagtail:wagtail /app

#ARG MEDIA_ROOT
#RUN echo $MEDIA_ROOT
#RUN mkdir $MEDIA_ROOT
#RUN chown wagtail:wagtail $MEDIA_ROOT
#VOLUME $MEDIA_ROOT

USER wagtail

#RUN python manage.py collectstatic --noinput --clear

CMD ./manage.py migrate --noinput \
 && uwsgi --ini /app/uwsgi.ini
