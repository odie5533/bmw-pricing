FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
RUN pip install .
RUN bmw_backend create-db
RUN bmw_backend populate-db
RUN bmw_backend add-user -u admin -p admin
EXPOSE 5000
CMD ["bmw_backend", "run", "-h", "0.0.0.0"]
