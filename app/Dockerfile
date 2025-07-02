ARG IMAGE_TAG=3.13.5-slim-bookworm

FROM python:${IMAGE_TAG}

ENV DB_HOST=db \
    DB_PORT=3306

WORKDIR /src

COPY requirements.txt .

RUN useradd --home-dir /src --uid 1000 app \
    && pip install --no-cache-dir -r requirements.txt \
    && chown -R app:app /src

USER app

COPY ./src/ ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

