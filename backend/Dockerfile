FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
# This command starts the Flask application server and makes it accessible on all network interfaces (0.0.0.0).
# The "--host=0.0.0.0" option ensures that the server is accessible externally, not just from localhost.
CMD ["flask", "run", "--host=0.0.0.0"]