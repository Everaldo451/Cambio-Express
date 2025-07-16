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

COPY --from=build /app/.next ./.next
COPY --from=build /app/public ./public

CMD ["npm", "run", "start"]