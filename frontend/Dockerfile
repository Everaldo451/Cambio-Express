FROM node:latest AS build

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build

FROM node:latest

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --production

COPY next.config.ts ./
COPY --from=build /app/public ./public
COPY --from=build /app/build ./build

ENV HOST=0.0.0.0
ENV PORT=3000

EXPOSE 3000

CMD ["npm", "run", "start"]