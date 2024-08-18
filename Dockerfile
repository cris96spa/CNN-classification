FROM python:3.12

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

WORKDIR /code

COPY ./requirements.txt ./code/requirements.txt

RUN pip install --no-cache-dir -r ./code/requirements.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]