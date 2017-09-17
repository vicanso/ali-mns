FROM python:2-alpine

EXPOSE 5000

ADD ./ /app

RUN pip install Flask

CMD ["python", "/app/server.py"]
