import streamlit as st
import pandas as pd
from geopy.distance import geodesic

st.set_page_config(page_title="Task Recommendation System", layout="wide")

st.title("🎯 Real-Time Skill-Based Task Recommendation System")

# -------------------------
# Sample Tasks Dataset
# -------------------------
tasks = pd.DataFrame([
    {"task_id": 1, "task_type": "Website Development", "required_skill": "Python", "mode": "Remote",
     "location": None, "urgency": "High", "reward": 500},
    {"task_id": 2, "task_type": "Math Tutoring", "required_skill": "Tutoring", "mode": "In-Person",
     "location": (13.0350, 77.5970), "urgency": "Medium", "reward": 300},
    {"task_id": 3, "task_type": "Data Entry", "required_skill": "Excel", "mode": "Remote",
     "location": None, "urgency": "Low", "reward": 200},
])

# -------------------------
# Urgency Scores
# -------------------------
urgency_scores = {"High": 1, "Medium": 0.6, "Low": 0.3}

# -------------------------
# Sidebar - User Input
# -------------------------
st.sidebar.header("👤 Freelancer Info")

user_name = st.sidebar.text_input("Enter your name:", "New User")

skills_options = ["Python", "Data Entry", "Excel", "Delivery", "Tutoring", "Website Design"]
user_skills = st.sidebar.multiselect("Select your skills:", skills_options, default=["Python"])

user_rating = st.sidebar.slider("Your rating (0-5):", 0.0, 5.0, 4.5, 0.1)

user_mode = st.sidebar.radio("Are you available for In-Person tasks?", ("Yes", "No"))

if user_mode == "Yes":
    user_lat = st.sidebar.number_input("Your latitude:", 12.9716)
    user_lon = st.sidebar.number_input("Your longitude:", 77.5946)
    user_location = (user_lat, user_lon)
else:
    user_location = None

st.sidebar.markdown("---")

# -------------------------
# Sidebar - Add New Task
# -------------------------
st.sidebar.header("➕ Add New Task")
new_task_type = st.sidebar.text_input("Task Type")
new_task_skill = st.sidebar.selectbox("Required Skill", skills_options)
new_task_mode = st.sidebar.radio("Mode", ("Remote", "In-Person"), key="mode")
new_task_urgency = st.sidebar.selectbox("Urgency", ["High", "Medium", "Low"])
new_task_reward = st.sidebar.number_input("Reward", 0, 10000, 100)

if new_task_mode == "In-Person":
    new_task_lat = st.sidebar.number_input("Task Latitude", 12.9716)
    new_task_lon = st.sidebar.number_input("Task Longitude", 77.5946)
    new_task_location = (new_task_lat, new_task_lon)
else:
    new_task_location = None

if st.sidebar.button("Add Task"):
    task_id = tasks['task_id'].max() + 1
    tasks = pd.concat([tasks, pd.DataFrame([{
        "task_id": task_id,
        "task_type": new_task_type,
        "required_skill": new_task_skill,
        "mode": new_task_mode,
        "location": new_task_location,
        "urgency": new_task_urgency,
        "reward": new_task_reward
    }])], ignore_index=True)
    st.sidebar.success(f"Task '{new_task_type}' added successfully!")

# -------------------------
# Function to Calculate Score
# -------------------------
def calculate_score(task, user_skills, user_location, user_rating):
    # Skill Match
    skill_match = 1 if task['required_skill'] in user_skills else 0
    
    # Distance Score
    if task['mode'] == "Remote":
        distance_score = 1
    elif task['location'] and user_location:
        distance_km = geodesic(user_location, task['location']).km
        distance_score = 1 / (distance_km + 1)  # avoid division by zero
    else:
        distance_score = 0  # if location not provided
    
    urgency_score = urgency_scores.get(task['urgency'], 0)
    
    score = 0.4 * skill_match + 0.3 * distance_score + 0.2 * urgency_score + 0.1 * (user_rating / 5)
    return round(score, 2)

# -------------------------
# Calculate Scores for All Tasks
# -------------------------
tasks['score'] = tasks.apply(lambda row: calculate_score(row, user_skills, user_location, user_rating), axis=1)
tasks_sorted = tasks.sort_values(by='score', ascending=False).reset_index(drop=True)

# -------------------------
# Display
# -------------------------
st.subheader(f"🔹 Task Recommendations for {user_name}")
st.dataframe(tasks_sorted[['task_type', 'required_skill', 'mode', 'urgency', 'reward', 'score']])

# Optional: Show Map for In-Person Tasks
in_person_tasks = tasks_sorted[tasks_sorted['mode'] == "In-Person"].dropna(subset=['location'])
if not in_person_tasks.empty and user_location:
    st.subheader("📍 In-Person Task Locations")
    map_data = pd.DataFrame([{"lat": loc[0], "lon": loc[1]} for loc in in_person_tasks['location']])
    st.map(map_data)
