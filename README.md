
# 💰 Personal Finance Tracker

A full-stack web application that helps users **track income, expenses, manage budgets**, and **visualize spending habits** with rich analytics over time.

---

## 🔧 Features

### ✅ Authentication
- **JWT-based authentication** powered by Django REST Framework.
- **React** handles protected routes and securely stores the token.

### ✅ Core Functionality
- Add, edit, and delete **income or expense transactions**.
- Categorize transactions (e.g., Food, Rent, Salary).
- Monthly and category-wise **summaries** of financial activity.

### ✅ Analytics Dashboard
- 📈 **Line Chart** showing monthly income vs expenses.
- 🥧 **Pie Chart** showing spending distribution by category.
- 🧾 List of recent transactions for quick access.

### ✅ Budget Planning
- Set **monthly budgets** per category.
- Get **notified** when budget limits are exceeded.

---

## 🗃 Backend – Django REST Framework

### 🔩 Models
- `User` – Custom user model (with JWT auth).
- `Transaction` – Stores income/expense entries.
- `Category` – Categories for classifying transactions.
- `Budget` – User-defined category-wise monthly budgets.

### 🔐 Permissions
- Users can only access **their own** data.

### 📡 API Endpoints
| Endpoint        | Description                        |
|-----------------|------------------------------------|
| `/transactions/`| CRUD operations for transactions   |
| `/categories/`  | CRUD operations for categories     |
| `/budgets/`     | Set and manage category budgets    |
| `/summary/`     | Returns analytics & dashboard data |

> 🛎️ Optional: Django **signals** can be used to trigger budget limit notifications.

---

## 🌐 Frontend – React

### 📄 Pages & Components
- **Login/Register**: Secure user auth forms.
- **Dashboard**: Visual charts and key summaries.
- **Transactions**: Full CRUD for transactions.
- **Budget Planner**: UI for setting and editing budgets.

### 🧰 Tools & Libraries
- `Axios`: API communication & JWT handling.
- `Chart.js` or `Recharts`: For rich data visualizations.
- React Router: Routing and protected routes.

---

## 🚀 Getting Started

### Backend (Django)
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Frontend (React)
```bash
Copy
Edit
cd frontend
npm install
npm start

📦 Folder Structure
finance-tracker/
├── backend/
│   ├── manage.py
│   └── finance_app/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── urls.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/ (Axios setup)
│   │   └── App.js

✨ Future Improvements
User-defined recurring transactions
Export data (CSV, PDF)
Dark mode
Multi-currency support