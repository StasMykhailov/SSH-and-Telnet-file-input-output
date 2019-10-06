FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ENV PYTHONPATH /app:$PYTHONPATH
COPY requirements/base.txt /app/
RUN pip install -r base.txt
COPY . /app/
CMD tail -f /dev/null