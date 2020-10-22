FROM centos:centos7

RUN yum -y update
RUN yum -y install python3.6
RUN yum -y install python3.6-pip
RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install wheel
RUN python3.6 -m pip install tornado==6.0.3
RUN python3.6 -m pip install numpy==1.19.2
RUN python3.6 -m pip install pandas
RUN python3.6 -m pip install Flask==1.1.1
RUN python3.6 -m pipi nstall werkzeug


COPY . .
CMD ["python", "./init_tornado.py"]
EXPOSE 8081

