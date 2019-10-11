FROM python:3.7

COPY . .
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
CMD ["python", "manage.py","runserver"]