import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import time
import os
from plotly.subplots import make_subplots
import numpy as np

# ===== USER TRACKING LOGGING =====
def log_user_access():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("usage_log.txt", "a") as f:
        f.write(f"{now} - Dashboard accessed\n")
log_user_access()

# Configure page
st.set_page_config(
    page_title="AI Trainer Management Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to create dummy data (for demonstration)
def create_dummy_data():
    dummy_data = [
        {
            'Name': 'John Smith',
            'Status Date': '2024-07-01',
            'Task Allocated': 'Training Delivery',
            'Client Name': 'TechCorp',
            'Batch Name': 'Batch-A1',
            'Training Hours': 25.5,
            'Topic Covered': 'Python Programming, Data Structures',
            'Challenges': 'Network connectivity issues during virtual sessions',
            'Learner Queries': 'Questions about advanced Python concepts',
            'Suggestions': 'More hands-on practice sessions needed',
            'Asset Development Hours': 12.0,
            'Content Decks Developed': 5,
            'Content Videos Developed': 3,
            'Simulations Developed': 2,
            'Assessment Questions (MCQ) Developed': 25,
            'Lab Questions Developed': 15,
            'Projects, Case Studies and POCs': 'E-commerce website project, Banking system case study'
        },
        {
            'Name': 'Sarah Johnson',
            'Status Date': '2024-07-02',
            'Task Allocated': 'Asset Development',
            'Client Name': 'FinanceInc',
            'Batch Name': 'Batch-B2',
            'Training Hours': 18.0,
            'Topic Covered': 'Machine Learning, Data Analytics',
            'Challenges': 'Complex ML algorithms difficult to explain',
            'Learner Queries': 'Practical applications of ML in finance',
            'Suggestions': 'More real-world examples needed',
            'Asset Development Hours': 28.5,
            'Content Decks Developed': 8,
            'Content Videos Developed': 6,
            'Simulations Developed': 4,
            'Assessment Questions (MCQ) Developed': 40,
            'Lab Questions Developed': 20,
            'Projects, Case Studies and POCs': 'Stock prediction model, Risk assessment system'
        },
        {
            'Name': 'Mike Chen',
            'Status Date': '2024-07-03',
            'Task Allocated': 'Training Delivery',
            'Client Name': 'HealthTech',
            'Batch Name': 'Batch-C3',
            'Training Hours': 32.0,
            'Topic Covered': 'Cloud Computing, AWS Services',
            'Challenges': 'AWS account setup issues for participants',
            'Learner Queries': 'Cost optimization in cloud deployments',
            'Suggestions': 'Dedicated AWS sandbox environment',
            'Asset Development Hours': 15.5,
            'Content Decks Developed': 6,
            'Content Videos Developed': 4,
            'Simulations Developed': 3,
            'Assessment Questions (MCQ) Developed': 30,
            'Lab Questions Developed': 18,
            'Projects, Case Studies and POCs': 'Hospital management system, Telemedicine platform'
        },
        {
            'Name': 'Emily Davis',
            'Status Date': '2024-07-04',
            'Task Allocated': 'Asset Development',
            'Client Name': 'RetailCorp',
            'Batch Name': 'Batch-D4',
            'Training Hours': 22.5,
            'Topic Covered': 'React Development, Frontend Technologies',
            'Challenges': 'Version compatibility issues with React libraries',
            'Learner Queries': 'Best practices for component optimization',
            'Suggestions': 'Updated curriculum with latest React version',
            'Asset Development Hours': 35.0,
            'Content Decks Developed': 10,
            'Content Videos Developed': 8,
            'Simulations Developed': 5,
            'Assessment Questions (MCQ) Developed': 45,
            'Lab Questions Developed': 25,
            'Projects, Case Studies and POCs': 'E-commerce frontend, Inventory management UI'
        },
        {
            'Name': 'David Wilson',
            'Status Date': '2024-07-05',
            'Task Allocated': 'Training Delivery',
            'Client Name': 'TechCorp',
            'Batch Name': 'Batch-E5',
            'Training Hours': 28.0,
            'Topic Covered': 'DevOps, CI/CD Pipeline',
            'Challenges': 'Docker containerization complexity',
            'Learner Queries': 'Kubernetes deployment strategies',
            'Suggestions': 'Step-by-step Docker tutorials',
            'Asset Development Hours': 20.0,
            'Content Decks Developed': 7,
            'Content Videos Developed': 5,
            'Simulations Developed': 3,
            'Assessment Questions (MCQ) Developed': 35,
            'Lab Questions Developed': 22,
            'Projects, Case Studies and POCs': 'CI/CD pipeline setup, Microservices architecture'
        },
        {
            'Name': 'Lisa Rodriguez',
            'Status Date': '2024-07-06',
            'Task Allocated': 'Asset Development',
            'Client Name': 'EduTech',
            'Batch Name': 'Batch-F6',
            'Training Hours': 19.5,
            'Topic Covered': 'Data Science, Statistical Analysis',
            'Challenges': 'Statistical concepts difficult for beginners',
            'Learner Queries': 'Real-world data science applications',
            'Suggestions': 'More visualization examples needed',
            'Asset Development Hours': 42.0,
            'Content Decks Developed': 12,
            'Content Videos Developed': 9,
            'Simulations Developed': 6,
            'Assessment Questions (MCQ) Developed': 50,
            'Lab Questions Developed': 30,
            'Projects, Case Studies and POCs': 'Student performance analysis, Learning analytics dashboard'
        }
    ]
    return pd.DataFrame(dummy_data)

# The rest of the script continues as before...
