# Use an official Python runtime as a parent image
FROM python:3.12.5


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "KingSalmanAcademy.wsgi:application"]
