# 🍽️ Recipe API (Django + MySQL + Bootstrap)

A full-stack API development project built for the Securin assessment task.

---

## 🛠️ Tech Stack

- Django + Django REST Framework
- MySQL (with PyMySQL connector)
- Bootstrap 5 (for simple frontend UI)
- Python 3.14

---

## 📦 Features

- Parse & load large JSON recipe data
- CRUD API with Django REST
- Responsive frontend (add + list recipes)
- MySQL database integration
- Clean UI with Bootstrap
- Optional deployment ready

---

## 📑 API Endpoints

| Method | Endpoint               | Description          |
|--------|------------------------|----------------------|
| GET    | `/api/recipes/`        | List all recipes     |
| POST   | `/api/recipes/`        | Add new recipe       |
| GET    | `/api/recipes/<id>/`   | View one recipe      |
| PUT    | `/api/recipes/<id>/`   | Update recipe        |
| DELETE | `/api/recipes/<id>/`   | Delete recipe        |

Frontend:
- `/api/web/` — View recipes
- `/api/web/add/` — Add a new recipe

---

## 📁 Project Setup

```bash
git clone https://github.com/yourusername/recipe-api-project.git
cd recipe-api-project
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
