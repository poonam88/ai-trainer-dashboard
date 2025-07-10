import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import time
import os
from plotly.subplots import make_subplots
import numpy as np

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

# Function to load Excel data
def load_excel_data(file_path):
    try:
        if os.path.exists(file_path):
            return pd.read_excel(file_path)
        else:
            # Return dummy data if file doesn't exist
            return create_dummy_data()
    except Exception as e:
        st.error(f"Error loading Excel file: {str(e)}")
        return create_dummy_data()

# Function to get file modification time
def get_file_mtime(file_path):
    try:
        return os.path.getmtime(file_path) if os.path.exists(file_path) else 0
    except:
        return 0

# Initialize session state
if 'last_file_time' not in st.session_state:
    st.session_state.last_file_time = 0
if 'df' not in st.session_state:
    st.session_state.df = None

# File uploader and path settings
st.sidebar.header("📁 Data Source")
excel_file = st.sidebar.file_uploader("Upload Excel File", type=['xlsx', 'xls'])

# If no file uploaded, use dummy data
if excel_file is not None:
    # Load uploaded file
    df = pd.read_excel(excel_file)
    st.session_state.df = df
    st.sidebar.success("✅ Excel file loaded successfully!")
else:
    # Use dummy data
    df = create_dummy_data()
    st.session_state.df = df
    st.sidebar.info("📊 Using dummy data for demonstration")

# Auto-refresh settings
st.sidebar.header("🔄 Auto-Refresh")
auto_refresh = st.sidebar.checkbox("Enable Auto-Refresh", value=True)
if auto_refresh:
    refresh_interval = st.sidebar.slider("Refresh Interval (seconds)", 5, 60, 10)
    
    # Auto-refresh logic
    if excel_file is None:  # Only for demo with dummy data
        time.sleep(refresh_interval)
        st.rerun()

# Main Dashboard
st.title("🤖 AI Trainer Management Dashboard")
st.markdown("---")

# Convert Status Date to datetime
if 'Status Date' in df.columns:
    df['Status Date'] = pd.to_datetime(df['Status Date'])

# Sidebar Filters
st.sidebar.header("🔍 Filters")

# Trainer filter
all_trainers = df['Name'].unique()
selected_trainers = st.sidebar.multiselect(
    "Select Trainers", 
    options=all_trainers, 
    default=all_trainers
)

# Task filter
all_tasks = df['Task Allocated'].unique()
selected_tasks = st.sidebar.multiselect(
    "Select Tasks", 
    options=all_tasks, 
    default=all_tasks
)

# Client filter
all_clients = df['Client Name'].unique()
selected_clients = st.sidebar.multiselect(
    "Select Clients", 
    options=all_clients, 
    default=all_clients
)

# Date filter
if 'Status Date' in df.columns:
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['Status Date'].min().date(), df['Status Date'].max().date()),
        min_value=df['Status Date'].min().date(),
        max_value=df['Status Date'].max().date()
    )

# Apply filters
filtered_df = df[
    (df['Name'].isin(selected_trainers)) &
    (df['Task Allocated'].isin(selected_tasks)) &
    (df['Client Name'].isin(selected_clients))
]

# Apply date filter if available
if 'Status Date' in df.columns and len(date_range) == 2:
    filtered_df = filtered_df[
        (filtered_df['Status Date'].dt.date >= date_range[0]) &
        (filtered_df['Status Date'].dt.date <= date_range[1])
    ]

# Key Performance Metrics
st.subheader("📈 Key Performance Metrics")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("👥 Total Trainers", len(filtered_df['Name'].unique()))

with col2:
    total_training_hours = filtered_df['Training Hours'].sum()
    st.metric("⏱️ Training Hours", f"{total_training_hours:.1f}")

with col3:
    total_asset_hours = filtered_df['Asset Development Hours'].sum()
    st.metric("🔧 Asset Dev Hours", f"{total_asset_hours:.1f}")

with col4:
    st.metric("📊 Total Submissions", len(filtered_df))

with col5:
    st.metric("🏢 Active Clients", len(filtered_df['Client Name'].unique()))

st.markdown("---")

# Charts Section
st.subheader("📊 Training Analytics")

# Training Hours by Trainer
trainer_hours = filtered_df.groupby('Name')['Training Hours'].sum().sort_values(ascending=False)
if not trainer_hours.empty:
    fig_hours = px.bar(
        x=trainer_hours.index, 
        y=trainer_hours.values,
        title='🏆 Training Hours by Trainer',
        labels={'x': 'Trainer', 'y': 'Hours'},
        color=trainer_hours.values,
        color_continuous_scale='Blues'
    )
    fig_hours.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig_hours, use_container_width=True)

# Two column layout for pie charts
col1, col2 = st.columns(2)

with col1:
    # Task Distribution
    task_dist = filtered_df['Task Allocated'].value_counts()
    if not task_dist.empty:
        fig_task = px.pie(
            values=task_dist.values,
            names=task_dist.index,
            title='📋 Task Distribution',
            color_discrete_sequence=['#667eea', '#764ba2']
        )
        st.plotly_chart(fig_task, use_container_width=True)

with col2:
    # Client Distribution
    client_dist = filtered_df['Client Name'].value_counts()
    if not client_dist.empty:
        fig_client = px.pie(
            values=client_dist.values,
            names=client_dist.index,
            title='🏢 Client Distribution',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig_client, use_container_width=True)

# Asset Development Analysis
st.subheader("🔧 Asset Development Analytics")

# Asset metrics by trainer
asset_columns = ['Content Decks Developed', 'Content Videos Developed', 'Simulations Developed', 
                'Assessment Questions (MCQ) Developed', 'Lab Questions Developed']

asset_metrics = filtered_df.groupby('Name')[asset_columns].sum().reset_index()

if not asset_metrics.empty:
    # Melt the data for grouped bar chart
    asset_melted = asset_metrics.melt(
        id_vars='Name', 
        value_vars=asset_columns,
        var_name='Asset Type', 
        value_name='Count'
    )
    
    fig_assets = px.bar(
        asset_melted,
        x='Name',
        y='Count',
        color='Asset Type',
        title='📊 Asset Development by Trainer',
        barmode='group',
        height=500
    )
    st.plotly_chart(fig_assets, use_container_width=True)

# Performance Score Analysis
st.subheader("🏆 Trainer Performance Analysis")

# Calculate performance score
performance_df = filtered_df.groupby('Name').agg({
    'Training Hours': 'sum',
    'Asset Development Hours': 'sum',
    'Content Decks Developed': 'sum',
    'Content Videos Developed': 'sum',
    'Simulations Developed': 'sum',
    'Assessment Questions (MCQ) Developed': 'sum',
    'Lab Questions Developed': 'sum'
}).reset_index()

# Performance score calculation (weighted)
performance_df['Performance Score'] = (
    performance_df['Training Hours'] * 1.0 +
    performance_df['Asset Development Hours'] * 1.2 +
    performance_df['Content Decks Developed'] * 2.0 +
    performance_df['Content Videos Developed'] * 3.0 +
    performance_df['Simulations Developed'] * 4.0 +
    performance_df['Assessment Questions (MCQ) Developed'] * 0.5 +
    performance_df['Lab Questions Developed'] * 1.0
)

if not performance_df.empty:
    fig_performance = px.bar(
        performance_df.sort_values('Performance Score', ascending=False),
        x='Name',
        y='Performance Score',
        title='🌟 Overall Performance Score by Trainer',
        color='Performance Score',
        color_continuous_scale='Viridis',
        height=400
    )
    st.plotly_chart(fig_performance, use_container_width=True)

# Training vs Asset Development Comparison
st.subheader("⚖️ Training vs Asset Development")

col1, col2 = st.columns(2)

with col1:
    # Training hours by task type
    task_hours = filtered_df.groupby('Task Allocated')['Training Hours'].sum()
    if not task_hours.empty:
        fig_task_hours = px.bar(
            x=task_hours.index,
            y=task_hours.values,
            title='Training Hours by Task Type',
            color=task_hours.values,
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_task_hours, use_container_width=True)

with col2:
    # Asset development hours by task type
    asset_hours = filtered_df.groupby('Task Allocated')['Asset Development Hours'].sum()
    if not asset_hours.empty:
        fig_asset_hours = px.bar(
            x=asset_hours.index,
            y=asset_hours.values,
            title='Asset Development Hours by Task Type',
            color=asset_hours.values,
            color_continuous_scale='Greens'
        )
        st.plotly_chart(fig_asset_hours, use_container_width=True)

# Detailed Data Table
st.subheader("📋 Detailed Trainer Data")

# Display options
display_columns = st.multiselect(
    "Select columns to display:",
    options=filtered_df.columns.tolist(),
    default=['Name', 'Status Date', 'Task Allocated', 'Client Name', 'Training Hours', 'Asset Development Hours']
)

if display_columns:
    # Sort by most recent
    if 'Status Date' in display_columns:
        display_df = filtered_df[display_columns].sort_values('Status Date', ascending=False)
    else:
        display_df = filtered_df[display_columns]
    
    st.dataframe(display_df, use_container_width=True, height=400)
    
    # Download button
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name=f"trainer_dashboard_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

# Summary Statistics
st.subheader("📊 Summary Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Training Statistics**")
    st.write(f"• Average training hours: {filtered_df['Training Hours'].mean():.1f}")
    st.write(f"• Max training hours: {filtered_df['Training Hours'].max():.1f}")
    st.write(f"• Min training hours: {filtered_df['Training Hours'].min():.1f}")

with col2:
    st.write("**Asset Development Statistics**")
    st.write(f"• Total content decks: {filtered_df['Content Decks Developed'].sum()}")
    st.write(f"• Total videos: {filtered_df['Content Videos Developed'].sum()}")
    st.write(f"• Total simulations: {filtered_df['Simulations Developed'].sum()}")

with col3:
    st.write("**Assessment Statistics**")
    st.write(f"• Total MCQ questions: {filtered_df['Assessment Questions (MCQ) Developed'].sum()}")
    st.write(f"• Total lab questions: {filtered_df['Lab Questions Developed'].sum()}")
    st.write(f"• Average asset dev hours: {filtered_df['Asset Development Hours'].mean():.1f}")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Dashboard Info")
st.sidebar.info(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.sidebar.metric("📈 Total Records", len(filtered_df))

# Auto-refresh indicator
if auto_refresh:
    st.sidebar.success("🔄 Auto-refresh: ON")
else:
    st.sidebar.warning("🔄 Auto-refresh: OFF")