# Residential Mortgage Securities (RMBS) Credit Rating

This project consists of a **backend (Django REST Framework)** and a **frontend (React.js)** to calculate and display mortgage credit ratings.

---

## 🚀 Getting Started

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/subhash-goswami/rmbs.git
cd rmbs
```

---

## 🖥️ Backend (Django REST Framework)

### **🔹 Setup & Run the Backend**

#### **1️⃣ Navigate to Backend Directory**

```bash
cd backend
```

#### **2️⃣ Create and Activate Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

#### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

#### **4️⃣ Apply Migrations & Setup Database**

```bash
python manage.py migrate
```

#### **5️⃣ Create a Superuser (Optional, for Django Admin)**

```bash
python manage.py createsuperuser
```

#### **6️⃣ Run the Backend Server**

```bash
python manage.py runserver
```

- The API will be available at: **`http://127.0.0.1:8000/api/`**

#### **7️⃣ Run Unit Tests (Optional)**

```bash
python manage.py test
```

---

## 🌐 Frontend (React.js)

### **🔹 Setup & Run the Frontend**

#### **1️⃣ Navigate to Frontend Directory**

```bash
cd frontend
```

#### **2️⃣ Install Dependencies**

```bash
npm install  # or yarn install
```

#### **3️⃣ Start the React Development Server**

```bash
npm start  # or yarn start
```

- The frontend will be available at: **`http://localhost:3000/`**

---

## 🔗 API Endpoints

| Method   | Endpoint               | Description                |
| -------- | ---------------------- | -------------------------- |
| `POST`   | `/api/mortgages/`      | Submit a new mortgage      |
| `GET`    | `/api/mortgages/`      | Retrieve all mortgages     |
| `GET`    | `/api/mortgages/{id}/` | Retrieve a single mortgage |
| `PUT`    | `/api/mortgages/{id}/` | Update a mortgage          |
| `DELETE` | `/api/mortgages/{id}/` | Delete a mortgage          |

---

## 📌 Features

✅ Input multiple mortgages with attributes like credit score, loan amount, property type, etc.\
✅ Backend logic to calculate credit rating (AAA, BBB, or C)\
✅ React frontend for submitting and viewing mortgages\
✅ Unit tests for API validation\
✅ Django Admin for managing data (optional)

---

## 📜 License

This project is licensed under the **GNU GENERAL PUBLIC LICENSE**.

---
