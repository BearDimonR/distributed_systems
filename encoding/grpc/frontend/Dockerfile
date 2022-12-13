FROM node:14-alpine

RUN apk add python3 make gcc g++

WORKDIR /app

COPY package.json .
RUN npm install --legacy-peer-deps

COPY . .
COPY .env .env

EXPOSE 3000

CMD [ "npm", "start" ]