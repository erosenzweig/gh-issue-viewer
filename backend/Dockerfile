FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy django files
COPY backend .
COPY asgi.py .
COPY main.py .
COPY manage.py .
COPY settings.py .
COPY urls.py .
COPY wsgi.py .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# To use this image in a production environment, this command would be swapped out
# with a command to start an application server like gunicorn or uwsgi. For this app,
# we'll opt to run the django development server keeping in mind the notes on productionizing for future reference.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
