FROM python:3.11

WORKDIR /ChatBot

COPY ./requirements.txt /ChatBot/requirements.txt

RUN pip install --no-cache-dir --upgrade -r/ChatBot/requirements.txt

RUN useradd user
USER user

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR  $HOME/app

COPY --chown=user . $HOME/app


CMD [ "gunicorn","app:app","--host","0.0.0.0","--port","7860" ]

