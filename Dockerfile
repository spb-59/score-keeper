
FROM python:3.9-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# Set the command to run when the container starts
CMD [ "python", "main.py" ]