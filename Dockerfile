FROM python:2.7.13
MAINTAINER Ritu Singh "ritu.ocs10@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

