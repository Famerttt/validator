FROM centos:centos7

RUN yum -y update
RUN yum -y install python36
RUN yum -y install python36-pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "./init_tornado.py"]
