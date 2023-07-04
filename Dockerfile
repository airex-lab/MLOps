FROM python:3.9

WORKDIR /code

RUN pip install fastapi "uvicorn[standard]"
COPY ./main.py /code/main.py

EXPOSE 8000
CMD ["uvicorn",  "main:app", "--host", "0.0.0.0", "--port", "8000"]
