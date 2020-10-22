FROM centos:centos7

RUN yum -y update
RUN yum -y install python36
RUN yum -y install python36-pip
RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install tornado==6.0.3\
    && pip install numpy==1.18.1 \
    && pip install pandas==1.0.1 \
    && pip install Flask==1.1.1 \
    && pip install werkzeug


COPY . .
CMD ["python", "./init_tornado.py"]
EXPOSE 8081

