# CreatorLens 📊

A Scalable Backend Analytics Platform for Content Creators

---

## 🚀 Overview

CreatorLens is a backend analytics system built with Django REST Framework that enables creators to publish posts, track real-time engagement, and generate automated performance reports.

The system is designed with scalability in mind using:

* Redis for real-time view tracking and caching
* Celery for background processing
* Celery Beat for scheduled analytics jobs
* PostgreSQL as the primary database

---

## 🧠 Key Features

* User authentication (JWT-based)
* Post creation, update, delete, and listing
* Real-time post view tracking using Redis
* Analytics dashboard (total views, top posts, engagement stats)
* Automated daily/weekly reports
* Background task processing with Celery
* Scheduled jobs using Celery Beat
* Seed data generation for testing (100+ fake records)

---

## 🏗️ System Architecture

Client Request
↓
Django REST API
↓
Redis (cache + real-time counters)
↓
Celery Workers (background processing)
↓
PostgreSQL (persistent storage)

Celery Beat
↓
Scheduled tasks (reports + sync jobs)

---

## 📁 Project Structure

```
CreatorLens/
│
├── config/                 # Project configuration
│   └── redis/              # Redis setup/config
│
├── apps/
│   ├── account/            # User authentication & profile management
│   ├── analytics/          # Dashboard + analytics logic
│   ├── posts/              # Posts + Redis view tracking + Celery tasks
│   ├── reports/            # Scheduled report generation tasks
│
├── dockerfile              # Container setup
├── requirements.txt        # Project dependencies
├── manage.py               # Django entry point
├── .github/                # CI/CD workflows (if used)
```

---

## ⚙️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Cache:** Redis
* **Async Tasks:** Celery
* **Scheduler:** Celery Beat
* **Media Storage:** Cloudinary
* **Auth:** JWT Authentication
* **Deployment Ready:** Docker

---

## ⚡ Core System Design

### 1. Post View Flow

* User opens a post
* Redis increments view count instantly
* API responds immediately
* Celery syncs Redis → PostgreSQL every 60 seconds

---

### 2. Analytics Flow

* Dashboard request received
* System checks Redis cache
* If cache exists → return instantly
* Else → compute from PostgreSQL → cache result

---

### 3. Report Generation

* Celery Beat triggers scheduled task
* Celery worker aggregates user analytics
* Stores results in `AnalyticsReport` table

---

## 🧪 Seed Data

To simulate real-world usage, the system includes a custom Django management command:

```bash
python manage.py seed_data
```

### This generates:

* ~100 posts
* Sample users
* Randomized view counts

Purpose:

* Test analytics accuracy
* Validate performance at scale
* Simulate real production-like usage

---

## 🔁 Background Jobs

### Celery Tasks

* Sync Redis views → PostgreSQL
* Generate analytics reports
* Aggregate user engagement metrics

### Celery Beat Schedule

* Every 60 seconds → Sync post views
* Weekly → Generate analytics reports

---

## 📊 Example API Features

* `POST /posts/` → Create post
* `GET /posts/` → List posts
* `GET /posts/<id>/` → Post details (increments views)
* `GET /analytics/dashboard/` → User analytics
* `GET /reports/` → Generated reports

---

## 🐳 Docker Support

Project includes Docker setup for containerized deployment.

```bash
docker build -t creatorlens .
docker run creatorlens
```

---

## 📌 Key Design Decisions

* Redis used to avoid heavy DB writes on every view
* Celery used to move expensive tasks off request cycle
* PostgreSQL used as single source of truth
* Cloudinary used to simplify media handling
* Seed data added for realistic testing environment

---

## 📈 Future Improvements

* WebSocket real-time analytics dashboard
* Rate limiting per user
* Kafka-based event streaming
* Advanced engagement metrics (CTR, retention)
* PDF export for reports
* Kubernetes deployment
* Multi-tenant architecture

---

## 👨‍💻 Author

Built as a backend engineering portfolio project demonstrating:

* Scalable API design
* Caching strategies
* Background processing
* Analytics systems architecture
* Production-ready Django patterns
