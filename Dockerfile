FROM python:2.7.13
MAINTAINER Ritu Singh "ritu.ocs10@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN git clone -b docker https://github.com/RituSinghme/cmpe273-assignment1/assignment1-flask-app.git /assignment1-flask-app/
ENTRYPOINT ["python"]
CMD ["app.py"]

