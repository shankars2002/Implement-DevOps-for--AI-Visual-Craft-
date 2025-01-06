# Implement-DevOps-for-AI-Visual-Craft-
Here's a consolidated guide covering the deployment and monitoring of the AI Artistic Style Service, using Docker, Docker Compose, Prometheus, Grafana, and Jenkins for CI/CD.

---

### **Steps to Deploy AI Artistic Style Service**
1. **Pull the Docker Image**  
   ```bash
   docker pull urmsandeep/ai-artistic-style-service
   ```

2. **Run the Docker Container**  
   ```bash
   docker run -d -p 5001:5001 urmsandeep/ai-artistic-style-service
   ```

3. **Verify the Container**  
   ```bash
   docker ps | grep ai-artistic-style-service
   ```

4. **Invoke the Service**  
   Use `curl` to make a POST request:  
   ```bash
   curl -X POST http://127.0.0.1:5001/styleTransfer -F "image=@input.jpg" --output output.jpg
   ```

---

### **Docker Compose for Simplified Management**
Create a `docker-compose.yml` file:
```yaml
version: '3.8'
services:
  ai-artistic-style-service:
    image: urmsandeep/ai-artistic-style-service:latest
    container_name: ai-artistic-style
    ports:
      - "5001:5001"
    restart: always

  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    restart: always

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    depends_on:
      - prometheus
    restart: always
```

---

### **Prometheus Configuration**
Create `prometheus.yml` for metrics scraping:
```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'ai-artistic-style-service'
    static_configs:
      - targets: ['ai-artistic-style-service:5001']
```

---

### **Run the Setup**
Start all services:  
```bash
docker-compose up -d
```

Verify running services:  
```bash
docker ps
```

---

### **Grafana Setup**
1. Visit Grafana at [http://localhost:3000](http://localhost:3000).
2. Login:  
   - Username: `admin`  
   - Password: `admin` (or the password set in Docker Compose).  
3. Add Prometheus as a Data Source:  
   - Go to **Configuration > Data Sources > Add Data Source**.  
   - Select Prometheus and set URL to `http://prometheus:9090`.  
   - Save & Test.  
4. Create dashboards to visualize metrics.

---

### **Integrating Jenkins for CI/CD**
Here’s a sample `Jenkinsfile` pipeline:

```groovy
pipeline {
    agent any

    stages {
        stage('Pull Docker Image') {
            steps {
                script {
                    sh 'docker pull urmsandeep/ai-artistic-style-service:latest'
                }
            }
        }

        stage('Deploy Service') {
            steps {
                script {
                    sh 'docker-compose down'
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'curl -X POST http://127.0.0.1:5001/styleTransfer -F "image=@test.jpg" --output styled_test.jpg'
                }
            }
        }

        stage('Monitor') {
            steps {
                echo 'Integrating Prometheus & Grafana for monitoring...'
            }
        }
    }
}
```

---

### **Prometheus & Grafana Monitoring**
1. Access Prometheus at [http://localhost:9090](http://localhost:9090).  
   - Query service metrics like `up` or custom metrics exposed by the AI service.  
2. Access Grafana at [http://localhost:3000](http://localhost:3000).  
   - View real-time data visualizations and dashboards.

---

### **Key Commands**
- **Start services**: `docker-compose up -d`  
- **Stop services**: `docker-compose down`  
- **View logs**:  
   ```bash
   docker-compose logs <service_name>
   ```


![image](https://github.com/user-attachments/assets/956ef0e7-76a5-451e-9670-895d2ff685a6)

![image](https://github.com/user-attachments/assets/a321cf2d-0c5b-43b3-8690-576a9d86dffe)

![image](https://github.com/user-attachments/assets/15a6fa49-d1e6-4cac-ab0e-7fddc71f5899)


![image](https://github.com/user-attachments/assets/6092c454-221a-4693-823a-e6fa625dd517)



![Screenshot 2024-12-24 192131](https://github.com/user-attachments/assets/d6e48457-2449-4c1f-9835-39deaae9088a)


![Screenshot 2025-01-06 124851](https://github.com/user-attachments/assets/5cd725bf-fa56-4709-9260-32cefbeab25a)

