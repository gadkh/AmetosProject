
---

## Ingestion service

### Overview
This service get an events from sensors, save them in the DB and send them to RMQ

   
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
1. move to /Ametos_ingestion_service
    ```bash
    docker cd /Ametos_ingestion_service
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
    - **Ingestion Service API:** [http://localhost:8000/docs](http://localhost:8000/docs)
---

## API Endpoints

| Method | Endpoint       | Description                |
|--------|---------------|----------------------------|
| POST   | `/v1/events/`  | Receive and validate events |
| GET    | `/v1/events/`  | Retrieve stored events      |

## Valid sensors
| device_id | device_type       |
|--------|-------------------|
| AA:BB:CC:DD:EE:FF   | access_controller |
| 11:22:33:44:55:66    | radar             |
| 77:88:99:AA:BB:CC    | security_camera             |



