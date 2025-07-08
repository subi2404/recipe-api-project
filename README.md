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

## ✅ Challenges Faced
JSON was double-wrapped in a dictionary format ({"0": {...}, "1": {...}})

Fixed decoding by parsing key-value pairs instead of assuming a list

mysqlclient failed on Windows, used PyMySQL as drop-in replacement

Cleaned up recipes missing titles with a safe validation step

## 📬 Submission
All source code, JSON loader, frontend, and documentation included in this repo.


---

## ✅ 5. Add `requirements.txt` (Optional but great!)

Run:

```bash
pip freeze > requirements.txt
✅ This helps reviewers set up the environment fast.


