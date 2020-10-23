FROM centos:centos7

RUN yum -y update
RUN yum -y install python36
RUN yum -y install python36-pip
RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install wheel
RUN python3.6 -m pip install tornado==6.0.3
RUN python3.6 -m pip install numpy
RUN python3.6 -m pip install pandas
RUN python3.6 -m pip install Flask
RUN python3.6 -m pip install werkzeug



CMD ["python", "init_tornado.py"]
EXPOSE 8081

