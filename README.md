# Cambio

<p>__DEV__ is a full-stack project that represents a course platform and allows teachers
to create courses and students to register for them.</p>

![Status: Development](https://img.shields.io/badge/Status-Development-yellow)

## ⚙️ Tech Stack:

- 🐍 Django + DRF (Python REST API and JWT Auth)
- ⚛️ Next.JS (frontend framework)
- 🐳 Docker & Docker Compose
- 🧰 Nginx (reverse proxy to Django API and Next.JS app)
- 🐬 MySQL (Database)

## 📁 Project Structure

- `/frontend`: Next.JS app
- `/backend*`: Django REST API with MySQL and Redis integration
- `/nginx`: Nginx config files
- `/docker-compose.yaml`
- `/.env.example`: Environment variables example

## 🧪 Setup and Running

1. **Clone the repository**

```bash
git clone https://github.com/Everaldo451/Cambio-Express
```

2. Create a `.env` file in the root folder of the project with the variables present in `.env.example`.

3. **Build and run the containers**

```bash
$ docker-compose up -d --build
```

4. **Access the app**

- 🌐 Frontend (Next.JS app proxied internally): http://localhost
- 🔙 Backend (Django API proxied internally): http://localhost/api

## Authors

- Everaldo Veloso Cavalcanti Junior