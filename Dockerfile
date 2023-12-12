FROM python:3.8-slim-buster
LABEL maintainer="Objective Bank"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -U -r /tmp/requirements.txt

COPY . /webhook
WORKDIR /webhook

EXPOSE 5000
CMD ["flask","run","-h","0.0.0.0","-p","5000"]


# Run Container:
# docker build -t obj.bank_service:0.1 .
# docker run --name obj.bank_service --add-host=host.docker.internal:172.17.0.1 -p 5000:5000 -d obj.bank_service:0.1