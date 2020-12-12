# Pull prom this python image
FROM python:3.7.2-stretch

# Set our working directory
WORKDIR /app

# Copy all files to /app
ADD . /app

# Update and install wkhtmltopdf for use with pdfkit
RUN apt-get update
RUN apt-get install -y wkhtmltopdf xvfb

# Install all requirements
RUN pip install -U pip
RUN pip install -r requirements.txt

# Start our wsgi server
CMD ["uwsgi", "app.ini"]

