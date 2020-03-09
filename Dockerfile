FROM python:3.6-stretch

RUN useradd search
RUN mkdir /home/search
RUN chown search:search /home/search

USER search

# For Windows only
# COPY --chown=search:search ./app /home/search/app

WORKDIR /home/search
COPY --chown=search:search requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

# USER root
# WORKDIR /home/search/app
# RUN apt-get install nodejs

# USER search
# RUN npm install
# RUN npm run build

WORKDIR /home/search
COPY --chown=search:search search.py search.py
ENV FLASK_APP search.py
EXPOSE 5000
COPY --chown=search:search boot.sh boot.sh
RUN chmod +x boot.sh
ENTRYPOINT ["./boot.sh"]
