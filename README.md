````markdown
# 🩸 Blood Donate & Request System

A Django-based web application that connects blood donors with people who need blood. Users can register, create donor profiles, search for suitable donors, create blood requests, and manage their own requests.

The main goal of this project is to provide a simple and user-friendly platform for managing blood donation and blood request information.

---

## 📌 Project Overview

The **Blood Donate & Request System** is developed using Python and Django.

The system allows users to:

- Create an account and log in
- Create and manage donor profiles
- Search donors by blood group and location
- Check donor availability
- Create blood requests
- View blood requests
- Filter blood requests
- Edit and delete their own blood requests
- Manage their donor profile
- View dashboard statistics

This project demonstrates practical implementation of Django Models, Views, Templates, Forms, ORM, Authentication, CRUD operations, Validation, Search and Filtering.

---

## ✨ Features

### 👤 User Authentication

- User Registration
- User Login
- User Logout
- Django built-in authentication
- Authenticated user dashboard
- Protected pages using `login_required`

### 🩸 Donor Management

- Create donor profile
- View donor profile
- Update donor profile
- Delete donor profile
- Blood group selection
- Donor location
- Phone number
- Last donation date
- Donation availability
- Optional profile picture
- Donor description

### 🔎 Donor Search & Filtering

Users can find donors using:

- Blood Group
- Location
- Availability

Supported blood groups:

- A+
- A-
- B+
- B-
- AB+
- AB-
- O+
- O-

### 🏥 Blood Request Management

Users can create blood requests containing:

- Patient Name
- Required Blood Group
- Hospital Name
- Hospital Location
- Required Date
- Number of Blood Bags
- Contact Number
- Description / Reason
- Request Status

Request statuses:

- Pending
- Fulfilled
- Cancelled

### 🔍 Blood Request Search & Filtering

Blood requests can be filtered by:

- Blood Group
- Hospital Location
- Request Status

### 📊 Dashboard

The dashboard displays useful statistics such as:

- Total Donors
- Total Blood Requests
- My Requests
- Available Donors
- Pending Requests
- Fulfilled Requests
- Recent Blood Requests

### 🛡️ Security & Access Control

- Django authentication system
- Login required for protected pages
- Users can edit only their own donor profile
- Users can delete only their own donor profile
- Users can edit only their own blood requests
- Users can delete only their own blood requests
- CSRF protection for forms

### ✅ Form Validation

The application validates:

- Required fields
- Phone numbers
- Blood bag quantity
- Required date
- Last donation date
- Blood group choices
- Request status choices

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Django | Web Framework |
| SQLite | Database |
| HTML5 | Page Structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive UI |
| Bootstrap Icons | Icons |
| JavaScript | Frontend Interaction |
| Pillow | Image Upload Support |

---

## 📂 Project Structure

```text
blood_donation_system/
│
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── blood/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── dashboard.html
│   │
│   ├── registration/
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── donors/
│   │   ├── donor_list.html
│   │   ├── donor_form.html
│   │   ├── donor_confirm_delete.html
│   │   └── donor_profile.html
│   │
│   └── requests/
│       ├── request_list.html
│       ├── request_form.html
│       ├── request_confirm_delete.html
│       └── request_detail.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│
├── media/
│
├── requirements.txt
├── README.md
└── .gitignore
````

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shuvoroydipon/Blood-Donate-Request-System.git
```

### 2. Go to the Project Directory

```bash
cd Blood-Donate-Request-System
```

### 3. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

If PowerShell blocks script execution, use:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Admin User

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

Django admin panel:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser account created with:

```bash
python manage.py createsuperuser
```

From the admin panel, administrators can manage:

* Donor Profiles
* Blood Requests
* Users

---

## 🌐 Main URLs

| URL                      | Description           |
| ------------------------ | --------------------- |
| `/`                      | Home Page             |
| `/register/`             | User Registration     |
| `/login/`                | User Login            |
| `/logout/`               | User Logout           |
| `/dashboard/`            | Dashboard             |
| `/profile/`              | My Donor Profile      |
| `/donors/`               | Find Donors           |
| `/donors/create/`        | Create Donor Profile  |
| `/donors/edit/`          | Edit Donor Profile    |
| `/donors/delete/`        | Delete Donor Profile  |
| `/requests/`             | Blood Requests        |
| `/requests/create/`      | Create Blood Request  |
| `/requests/<id>/`        | Blood Request Details |
| `/requests/<id>/edit/`   | Edit Blood Request    |
| `/requests/<id>/delete/` | Delete Blood Request  |
| `/admin/`                | Admin Panel           |

---

## 🗃️ Database Models

### DonorProfile

The `DonorProfile` model stores donor information.

Main fields:

* User
* Full Name
* Blood Group
* Phone
* Location
* Last Donation Date
* Availability
* Description
* Profile Picture
* Created At
* Updated At

### BloodRequest

The `BloodRequest` model stores blood requirement information.

Main fields:

* Requester
* Patient Name
* Blood Group
* Hospital Name
* Hospital Location
* Required Date
* Bags Required
* Contact Number
* Description
* Status
* Created At
* Updated At

---

## 🔄 CRUD Operations

The project implements CRUD functionality for the main application data.

### Donor Profile

* Create
* Read
* Update
* Delete

### Blood Request

* Create
* Read
* Update
* Delete

Users are restricted from modifying or deleting records belonging to other users.

---

## 🔎 Search & Filtering

### Donor Search

Donors can be filtered using:

```text
Blood Group
Location
Availability
```

### Blood Request Search

Requests can be filtered using:

```text
Blood Group
Hospital Location
Status
```

---

## 📱 Responsive Design

The project uses **Bootstrap 5** to provide a responsive interface that works across:

* Desktop
* Laptop
* Tablet
* Mobile devices

The interface includes:

* Responsive navigation bar
* Bootstrap cards
* Responsive forms
* Responsive tables
* Responsive dashboard
* Mobile-friendly layouts

---

## 🖼️ Media Upload

Donors can optionally upload a profile picture.

Uploaded images are stored under:

```text
media/donor_profiles/
```

Pillow is used to support image uploads.

---

## 🧪 Testing

Before running the project, check the Django configuration:

```bash
python manage.py check
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

---

## 🚀 Future Improvements

Possible future features include:

* Donor and blood request matching system
* Blood compatibility checking
* Pagination
* Email notifications
* Donor/request messaging
* AJAX-based search
* User profile management
* Blood donation history
* Emergency blood request priority
* Location-based donor matching
* REST API integration
* Advanced dashboard analytics

---

## 🎯 Learning Objectives

This project was developed to practice:

* Django Project Structure
* Django Apps
* Django Models
* Django ORM
* Model Relationships
* Django Forms
* ModelForms
* CRUD Operations
* User Authentication
* Login & Logout
* Access Control
* Template Inheritance
* Bootstrap Integration
* Search & Filtering
* Form Validation
* Static Files
* Media Files
* Django Admin
* SQLite Database

---

## 📄 License

This project is created for educational and learning purposes.

---

## 👨‍💻 Author

**Shuvoroy Dipon**

GitHub:

https://github.com/shuvoroydipon

---

## ❤️ Project Purpose

> **Find a donor. Save a life.**

The purpose of this project is to demonstrate how a Django web application can be used to organize blood donor and blood request information in one place and make it easier for users to find suitable blood donors.

````



