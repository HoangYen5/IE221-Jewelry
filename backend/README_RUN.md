# Backend local run helper

The backend is configured to run easily using Docker and Docker Compose.

## 1. Using Docker Compose (Recommended)

From the `backend` folder, run:

```bash
docker compose up -d
```

This will build the backend image and start the container. The backend will be available at `http://localhost:8080`.
To stop the backend, run: `docker compose down`

## 2. Using Docker (Manual)

If you prefer to run the Docker container manually from the backend folder:

```bash
cd backend
docker build -t jewelry_backend .
docker run -d -p 8080:8080 --env-file .env --name jewelry_backend jewelry_backend
```

### Notes:
- Edit `.env` in the `backend` folder to set your DB credentials and `JWT_SECRET`.
- The `uploads` directory is mapped as a volume in docker-compose so uploaded files persist on your host machine.
