# syntax=docker/dockerfile:1

FROM node:latest as node_builder

WORKDIR /app

COPY frontend/package*.json ./

RUN npm ci --only=production

COPY frontend/public ./public
COPY frontend/src ./src
COPY frontend/tailwind.config.js ./
COPY frontend/tsconfig.json ./

RUN npm run build

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install --upgrade pip

COPY --from=node_builder /app/build ./static

COPY backend/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

COPY backend/ancient.py .
COPY backend/users.xml .
RUN echo 'ictf{fake_flag_for_testing}' > flag.txt

CMD ["python3", "-m", "gunicorn.app.wsgiapp", "ancient:app", "--bind=0.0.0.0:4000", "--timeout", "10", "-k", "gevent", "--workers=4"]
