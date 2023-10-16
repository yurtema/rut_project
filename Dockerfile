FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
CMD ["python", "DailyGreat/manage.py", "runserver", "0.0.0.0:8000"]
