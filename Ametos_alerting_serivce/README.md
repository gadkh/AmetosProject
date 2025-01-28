
---

## Ingestion service

### Overview
This service get an events from RMQ, save in DB and alert if needed

   
### System Components
- Backend Framework: FastAPI (Python)
- Task Queue Management: Celery
- Message Broker: RabbitMQ
- Database: PostgreSQL
- Caching: Redis
- Containerization: Docker, Docker-Compose
- Dependency Management: Python Virtual Environments (venv), pip

### Prerequisites
Make sure you have the following installed:
- Redis
- PostgreSQL
- RabbitMQ
- Docker

### Steps to Run
1. move to /Ametos_alerting_service
    ```bash
    docker cd /Ametos_alerting_service
    ```
2. check if have shared_network on the Docker:
   ```bash
    docker network ls
    ```
   if not exist create one:
    ```bash
    docker network create shared_network
    ```

3. Start the services using Docker Compose:
    ```bash
    docker-compose build --no-cache
    ```
   ```bash
    docker-compose up
    ```

4. Access the services via the following URLs:
    - **Alerting Service API:** [http://localhost:8001/docs](http://localhost:8001/docs)

---

## API Endpoints

| Method | Endpoint      | Description                |
|--------|---------------|----------------------------|
| GET    | `/v1/alerts/` | Retrieve stored alerts      |

## Valid users

| user_id           |
|-------------------|
| user123 | 
| user456 |
| user789 |
| admin001 |
