FROM python:3.6.6
EXPOSE 5000
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "./init_tornado.py"]
K