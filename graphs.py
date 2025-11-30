import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from db import Database


def graphs():
    st.markdown("""
        <style>
        .graphs-header {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="graphs-header">
            <h2 style="margin:0;">📊 Analytics Dashboard</h2>
            <p style="margin:5px 0 0 0;">Visual insights and data analysis</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Load student data
    db = Database()
    df = db.get_all_students()
    
    if df.empty:
        st.info("📝 No student data available. Please register students first.")
        return
    
    # Key Metrics
    st.markdown("### 📈 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="metric-card">
                <h3 style="margin:0;">{}</h3>
                <p style="margin:5px 0 0 0;">Total Students</p>
            </div>
        """.format(len(df)), unsafe_allow_html=True)
    
    with col2:
        if 'class' in df.columns:
            unique_classes = df['class'].nunique()
            st.markdown("""
                <div class="metric-card">
                    <h3 style="margin:0;">{}</h3>
                    <p style="margin:5px 0 0 0;">Classes</p>
                </div>
            """.format(unique_classes), unsafe_allow_html=True)
    
    with col3:
        if 'city' in df.columns:
            unique_cities = df['city'].nunique()
            st.markdown("""
                <div class="metric-card">
                    <h3 style="margin:0;">{}</h3>
                    <p style="margin:5px 0 0 0;">Cities</p>
                </div>
            """.format(unique_cities), unsafe_allow_html=True)
    
    with col4:
        if 'special_talent' in df.columns:
            talented_students = df[df['special_talent'].notna() & (df['special_talent'] != '')].shape[0]
            st.markdown("""
                <div class="metric-card">
                    <h3 style="margin:0;">{}</h3>
                    <p style="margin:5px 0 0 0;">Talented Students</p>
                </div>
            """.format(talented_students), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Chart 1: Students by Class (Bar Chart)
    if 'class' in df.columns:
        st.markdown("### 📊 Students Distribution by Class")
        class_counts = df['class'].value_counts().sort_index()
        
        fig1 = px.bar(
            x=class_counts.index,
            y=class_counts.values,
            labels={'x': 'Class', 'y': 'Number of Students'},
            title='Number of Students in Each Class',
            color=class_counts.values,
            color_continuous_scale='Viridis'
        )
        fig1.update_layout(
            xaxis_title="Class",
            yaxis_title="Number of Students",
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    # Chart 2: Gender Distribution (Pie Chart)
    if 'gender' in df.columns:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 👥 Gender Distribution")
            gender_counts = df['gender'].value_counts()
            
            fig2 = px.pie(
                values=gender_counts.values,
                names=gender_counts.index,
                title='Student Gender Distribution',
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig2.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig2, use_container_width=True)
        
        # Chart 3: Blood Group Distribution (Donut Chart)
        with col2:
            if 'blood_group' in df.columns:
                st.markdown("### 🩸 Blood Group Distribution")
                blood_counts = df[df['blood_group'].notna() & (df['blood_group'] != 'Select') & (df['blood_group'] != '')]['blood_group'].value_counts()
                
                if not blood_counts.empty:
                    fig3 = px.pie(
                        values=blood_counts.values,
                        names=blood_counts.index,
                        title='Blood Group Distribution',
                        hole=0.4,
                        color_discrete_sequence=px.colors.qualitative.Pastel
                    )
                    fig3.update_traces(textposition='inside', textinfo='percent+label')
                    st.plotly_chart(fig3, use_container_width=True)
                else:
                    st.info("No blood group data available")
    
    # Chart 4: Students by City (Horizontal Bar Chart)
    if 'city' in df.columns:
        st.markdown("### 🏙️ Students by City")
        city_counts = df['city'].value_counts().head(10)
        
        fig4 = px.bar(
            x=city_counts.values,
            y=city_counts.index,
            orientation='h',
            labels={'x': 'Number of Students', 'y': 'City'},
            title='Top 10 Cities (by Student Count)',
            color=city_counts.values,
            color_continuous_scale='Blues'
        )
        fig4.update_layout(height=400)
        st.plotly_chart(fig4, use_container_width=True)
    
    # Chart 5: Students by Area (if enough data)
    if 'area' in df.columns:
        area_counts = df['area'].value_counts().head(10)
        if len(area_counts) > 0:
            st.markdown("### 🏘️ Students by Area/Locality")
            
            fig5 = px.bar(
                x=area_counts.index,
                y=area_counts.values,
                labels={'x': 'Area', 'y': 'Number of Students'},
                title='Top 10 Areas (by Student Count)',
                color=area_counts.values,
                color_continuous_scale='Sunset'
            )
            fig5.update_layout(xaxis_tickangle=-45, height=400)
            st.plotly_chart(fig5, use_container_width=True)
    
    # Chart 6: Gender Distribution by Class (Stacked Bar Chart)
    if 'class' in df.columns and 'gender' in df.columns:
        st.markdown("### 📚 Gender Distribution Across Classes")
        
        class_gender = pd.crosstab(df['class'], df['gender'])
        
        fig6 = go.Figure(data=[
            go.Bar(name='Male', x=class_gender.index, y=class_gender.get('Male', [0]*len(class_gender)), marker_color='#4facfe'),
            go.Bar(name='Female', x=class_gender.index, y=class_gender.get('Female', [0]*len(class_gender)), marker_color='#f093fb'),
            go.Bar(name='Other', x=class_gender.index, y=class_gender.get('Other', [0]*len(class_gender)), marker_color='#43e97b')
        ])
        
        fig6.update_layout(
            barmode='stack',
            title='Gender Distribution by Class',
            xaxis_title='Class',
            yaxis_title='Number of Students',
            height=400
        )
        st.plotly_chart(fig6, use_container_width=True)
    
    # Chart 7: Parent Occupation Distribution (if data available)
    if 'parent_occupation' in df.columns:
        occupation_counts = df[df['parent_occupation'].notna() & (df['parent_occupation'] != '')]['parent_occupation'].value_counts().head(10)
        
        if not occupation_counts.empty:
            st.markdown("### 💼 Parent Occupation Distribution")
            
            fig7 = px.bar(
                x=occupation_counts.index,
                y=occupation_counts.values,
                labels={'x': 'Occupation', 'y': 'Count'},
                title='Top 10 Parent Occupations',
                color=occupation_counts.values,
                color_continuous_scale='Greens'
            )
            fig7.update_layout(xaxis_tickangle=-45, height=400)
            st.plotly_chart(fig7, use_container_width=True)
    
    # Chart 8: Special Talents Word Cloud / Bar Chart
    if 'special_talent' in df.columns:
        talent_counts = df[df['special_talent'].notna() & (df['special_talent'] != '')]['special_talent'].value_counts().head(15)
        
        if not talent_counts.empty:
            st.markdown("### ⭐ Special Talents Distribution")
            
            fig8 = px.bar(
                x=talent_counts.values,
                y=talent_counts.index,
                orientation='h',
                labels={'x': 'Number of Students', 'y': 'Talent'},
                title='Most Common Special Talents',
                color=talent_counts.values,
                color_continuous_scale='Purples'
            )
            fig8.update_layout(height=400)
            st.plotly_chart(fig8, use_container_width=True)
    
    # Chart 9: Admission Timeline (if admission_date available)
    if 'admission_date' in df.columns:
        df_with_dates = df[df['admission_date'].notna()].copy()
        if not df_with_dates.empty:
            df_with_dates['admission_date'] = pd.to_datetime(df_with_dates['admission_date'], errors='coerce')
            df_with_dates = df_with_dates[df_with_dates['admission_date'].notna()]
            
            if not df_with_dates.empty:
                st.markdown("### 📅 Admission Timeline")
                
                df_with_dates['year_month'] = df_with_dates['admission_date'].dt.to_period('M').astype(str)
                admission_timeline = df_with_dates.groupby('year_month').size().reset_index(name='count')
                
                fig9 = px.line(
                    admission_timeline,
                    x='year_month',
                    y='count',
                    labels={'year_month': 'Month', 'count': 'New Admissions'},
                    title='Student Admissions Over Time',
                    markers=True
                )
                fig9.update_layout(height=400)
                st.plotly_chart(fig9, use_container_width=True)
    
    # Chart 10: Age Distribution (calculated from DOB)
    if 'dob' in df.columns:
        df_with_dob = df[df['dob'].notna()].copy()
        if not df_with_dob.empty:
            df_with_dob['dob'] = pd.to_datetime(df_with_dob['dob'], errors='coerce')
            df_with_dob = df_with_dob[df_with_dob['dob'].notna()]
            
            if not df_with_dob.empty:
                from datetime import datetime
                current_year = datetime.now().year
                df_with_dob['age'] = current_year - df_with_dob['dob'].dt.year
                
                st.markdown("### 🎂 Age Distribution")
                
                fig10 = px.histogram(
                    df_with_dob,
                    x='age',
                    nbins=20,
                    labels={'age': 'Age', 'count': 'Number of Students'},
                    title='Student Age Distribution',
                    color_discrete_sequence=['#667eea']
                )
                fig10.update_layout(height=400)
                st.plotly_chart(fig10, use_container_width=True)
    
    # Summary Statistics Table
    st.markdown("### 📋 Summary Statistics")
    
    summary_data = {
        'Metric': [],
        'Value': []
    }
    
    summary_data['Metric'].append('Total Students')
    summary_data['Value'].append(len(df))
    
    if 'gender' in df.columns:
        summary_data['Metric'].append('Male Students')
        summary_data['Value'].append(len(df[df['gender'] == 'Male']))
        summary_data['Metric'].append('Female Students')
        summary_data['Value'].append(len(df[df['gender'] == 'Female']))
    
    if 'class' in df.columns:
        summary_data['Metric'].append('Number of Classes')
        summary_data['Value'].append(df['class'].nunique())
    
    if 'city' in df.columns:
        summary_data['Metric'].append('Cities Covered')
        summary_data['Value'].append(df['city'].nunique())
    
    if 'special_talent' in df.columns:
        summary_data['Metric'].append('Students with Special Talents')
        summary_data['Value'].append(len(df[df['special_talent'].notna() & (df['special_talent'] != '')]))
    
    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
