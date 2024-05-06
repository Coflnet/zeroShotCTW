FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/files

# Set the directory as the working directory
WORKDIR /usr/files

RUN pip install transformers

RUN pip install Pillow

RUN pip install open_clip_torch

RUN pip install fastapi

RUN pip install uvicorn

RUN pip install pydantic

RUN pip install torch


EXPOSE 42069

COPY . .

# Command to run the application
CMD ["uvicorn", "index:app", "--reload", "--host", "0.0.0.0", "--port", "42069"]
