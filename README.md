# Real-Time Skill-Based Task Recommendation System

This is a **Python + Streamlit web application** that dynamically recommends micro-tasks to freelancers in real-time based on their skills, location, and task urgency.  
The system supports **online (remote)** and **in-person tasks**, simulating a mini gig-economy platform.

---

## Project Description

The **Real-Time Skill-Based Task Recommendation System** intelligently matches tasks to freelancers using a **priority score**:

Score = 0.4 * SkillMatch + 0.3 * (1 / Distance OR 1 for Remote) + 0.2 * UrgencyScore + 0.1 * FreelancerRating

Freelancers can interactively view, accept, or reject tasks, while recommendations update dynamically as new tasks are added or locations change.  

This project demonstrates **real-time task recommendations, dynamic data handling, and interactive web-based interfaces** using Python.

---

## Features

### Freelancer Features
- Enter personal details: name, skills, rating, location
- View real-time task recommendations
- Accept or reject tasks
- Dynamic recommendations update as tasks change or freelancer moves

### Admin / Task Management Features
- Add new tasks with required skill, mode (Remote/In-Person), location, urgency, reward
- Calculate task score automatically
- Task list updates in real-time

---

## Screenshots

### 1. Freelancer Input / Dashboard

- <img width="393" height="660" alt="image" src="https://github.com/user-attachments/assets/dc93b135-ff32-4f67-9498-57567c49eb88" />


### 2. Task Recommendations

- <img width="398" height="585" alt="image" src="https://github.com/user-attachments/assets/c3bd9909-0424-4640-b2d5-4a499f2e8ffd" />


### 3. Tasks

- <img width="1166" height="318" alt="image" src="https://github.com/user-attachments/assets/ad872733-c6d9-4921-99fc-a62c52e593a5" />

- <img width="1454" height="613" alt="image" src="https://github.com/user-attachments/assets/8f457c57-6cd9-4af8-b4ee-184b3736dd02" />

### 4. entire page

<img width="1871" height="927" alt="image" src="https://github.com/user-attachments/assets/211f5792-d605-4c58-b385-165d77bb6017" />

---

## Folder Structure
- task_recommendation/
- ├── app.py
- └── README.md

  
---

## Installation & Run
Clone the repository:

> git clone https://github.com/tharz-06/freelancing_task_recommendation.git
> 
> cd freelancing_task_recommendation

Install dependencies:

> pip install -r requirements.txt

Run the Streamlit app:

> python -m streamlit run app.py

----

## Technologies Used

- Python 3.10+
- Pandas & NumPy (data handling)
- Geopy (distance calculation)
- Streamlit (interactive web interface)
