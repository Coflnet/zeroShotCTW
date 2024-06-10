FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-devel

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the directory as the working directory
WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 42069

COPY . .

# Command to run the application
CMD ["uvicorn", "index:app", "--reload", "--host", "0.0.0.0", "--port", "42069"]
