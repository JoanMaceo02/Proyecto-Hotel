FROM python:3.8
RUN mkdir app
WORKDIR /app
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]