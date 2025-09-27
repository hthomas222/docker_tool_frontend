FROM python:3.12-slim
WORKDIR /app
RUN pip install flask
RUN apt-get update && apt-get install -y docker.io
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
