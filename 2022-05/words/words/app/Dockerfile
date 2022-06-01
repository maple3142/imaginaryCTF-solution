# syntax=docker/dockerfile:1

FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY index.js ./index.js
COPY public public/
EXPOSE 3000

ENTRYPOINT ["node", "./index.js"]
