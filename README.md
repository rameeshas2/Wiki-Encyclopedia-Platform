# 📚 Wiki Encyclopedia Platform

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.4-purple?style=for-the-badge&logo=bootstrap)
![Markdown](https://img.shields.io/badge/Markdown-Content-black?style=for-the-badge&logo=markdown)

A Wikipedia-inspired web application built using **Django** as part of **CS50's Web Programming with Python and JavaScript (Project 1: Wiki)**. The platform allows users to browse, search, create, edit, and randomly discover encyclopedia entries written in Markdown and rendered dynamically as HTML.

---

# 📌 Project Overview

This project implements a server-rendered encyclopedia platform where each article is stored as a Markdown (`.md`) file. Users can manage encyclopedia content through a clean web interface while the Django backend handles routing, content retrieval, Markdown conversion, and template rendering.

The application demonstrates Django fundamentals including URL routing, views, templates, forms, and dynamic content generation.

---

# 🎯 Project Objectives

- Build a dynamic web application using Django
- Store encyclopedia entries as Markdown files
- Convert Markdown into HTML
- Implement full CRUD functionality for encyclopedia entries
- Practice Django routing, templates, and forms
- Develop a responsive user interface

---

# ✨ Features

## 📖 Encyclopedia Entries

- View encyclopedia articles
- Render Markdown as HTML
- Responsive article pages

---

## 🔍 Search

- Search encyclopedia entries
- Exact match redirects directly to the article
- Partial matches display a list of related entries

---

## ➕ Create New Entry

Users can create new encyclopedia pages by providing:

- Entry title
- Markdown content

The application prevents duplicate page titles.

---

## ✏️ Edit Entries

- Edit existing encyclopedia pages
- Pre-populated Markdown editor
- Save updates instantly

---

## 🎲 Random Page

- Navigate to a randomly selected encyclopedia article

---

## 📱 Responsive Design

- Bootstrap layout
- Responsive navigation
- Mobile-friendly pages

---

# 🛠️ Technologies Used

- Python 3
- Django
- HTML5
- CSS3
- Bootstrap 4
- Markdown
- Font Awesome

---

# 📂 Project Structure

```text
Wiki-Encyclopedia-Platform/
│
├── encyclopedia/
│   ├── templates/
│   │   └── encyclopedia/
│   │       ├── layout.html
│   │       ├── index.html
│   │       ├── entry.html
│   │       ├── search.html
│   │       ├── new.html
│   │       ├── edit.html
│   │       └── error.html
│   │
│   ├── entries/
│   │   ├── Python.md
│   │   ├── Django.md
│   │   └── ...
│   │
│   ├── urls.py
│   ├── views.py
│   └── util.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Application Workflow

```text
User Request
      │
      ▼
URL Routing (urls.py)
      │
      ▼
View Function (views.py)
      │
      ▼
Read Markdown File
      │
      ▼
Convert Markdown to HTML
      │
      ▼
Render Django Template
      │
      ▼
Display Encyclopedia Page
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/your-username/Wiki-Encyclopedia-Platform.git
```

## Navigate to the Project

```bash
cd Wiki-Encyclopedia-Platform
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install django markdown2
```

## Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

# 📄 Pages

## 🏠 Home

Displays all available encyclopedia entries.

<img width="1800" height="932" alt="image" src="https://github.com/user-attachments/assets/c38799d5-fc9b-4f89-b069-16c74e86c597" />

---

## 📖 Entry Page

Shows a selected encyclopedia article with Markdown rendered into HTML.

<img width="1811" height="942" alt="image" src="https://github.com/user-attachments/assets/d9a55454-d492-478f-8065-1c7fcd62b8d7" />

---

## 🔍 Search

Supports:

- Exact title matches
- Partial keyword matches

<img width="1778" height="926" alt="image" src="https://github.com/user-attachments/assets/f824b8a2-d8b0-4e74-a1df-871c0b6499f7" />

---

## ➕ New Entry

Allows users to create a new encyclopedia article.

<img width="1910" height="939" alt="image" src="https://github.com/user-attachments/assets/6922eb72-b527-43eb-ac5c-59ef044dafec" />

---

## ✏️ Edit Entry

Modify existing articles using a Markdown editor.

<img width="1794" height="924" alt="image" src="https://github.com/user-attachments/assets/af448869-295a-42cc-94b5-e8479b891516" />

---

## 🎲 Random Entry

Redirects users to a randomly selected encyclopedia page.

<img width="1797" height="926" alt="image" src="https://github.com/user-attachments/assets/93cdc711-93a4-4e13-9b7a-e047b067ca1c" />

---

# 📚 Markdown Support

Articles are written in Markdown and converted to HTML before rendering.

Example:

```markdown
# Python

Python is a programming language.

## Features

- Easy to learn
- Powerful
- Open Source
```

Rendered as:

- Heading
- Paragraphs
- Lists
- Bold text
- Italics
- Links
- Code blocks

---

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

- Django Framework
- URL Routing
- Django Views
- HTML Templates
- Template Inheritance
- Forms & CSRF Protection
- Markdown Rendering
- Dynamic Content Management
- CRUD Operations
- Responsive Web Design

---

# 🎓 Course Information

**Course:** CS50's Web Programming with Python and JavaScript

**Project:** Project 1 – Wiki

---

# 🙏 Acknowledgements

This project was developed as part of **CS50's Web Programming with Python and JavaScript** offered by Harvard University.

---

# 👩‍💻 Author

**Rameesha Shahid**

Software Engineering Student

Interested in Artificial Intelligence, Machine Learning, Full-Stack Web Development, UI/UX Design, and Cybersecurity.

---

# 📄 License

This project was created for educational purposes as part of the CS50 Web Programming course.
