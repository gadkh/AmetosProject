
---

## Ametos Alerting System

### Project Overview
This project simulates a system that ingests IoT events, processes them, and generates 
alerts based on predefined criteria.

### System Components
The system consists of two primary services:
1. #### ingestion Service:
   - Responsible for receiving sensor events, validating them, and storing them in the database.
   - Sends the processed events to a message queue for further processing.
   ##### Valid sensors
| device_id | device_type       |
|--------|-------------------|
| AA:BB:CC:DD:EE:FF   | access_controller |
| 11:22:33:44:55:66    | radar             |
| 77:88:99:AA:BB:CC    | security_camera             |

 
2. #### Alerting Service:
   - Listens to the message queue.
   - Generates alerts when certain conditions are met.
   ##### Valid users

| user_id           |
|-------------------|
| user123 | 
| user456 |
| user789 |
| admin001 |


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


1. Start the services using Docker Compose:
    ```bash
    docker-compose build --no-cache
    ```
   ```bash
    docker-compose up
    ```

2. Access the services via the following URLs:
    - **Ingestion Service API:** [http://localhost:8000/docs](http://localhost:8000/docs)
    - **Alerting Service API:** [http://localhost:8001/docs](http://localhost:8001/docs)

---

## API Endpoints

### Ingestion Service
| Method | Endpoint       | Description                |
|--------|---------------|----------------------------|
| POST   | `/v1/events/`  | Receive and validate events |
| GET    | `/v1/events/`  | Retrieve stored events      |

### Alerting Service
| Method | Endpoint      | Description                |
|--------|---------------|----------------------------|
| GET    | `/v1/alerts/` | Retrieve stored alerts      |


