FROM python:3.9
WORKDIR /get_current_usd
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["python", "manage.py", "runserver", "0:8000"]