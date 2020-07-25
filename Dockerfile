FROM python:3.6
ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt