import streamlit as st
import pandas as pd
from db import Database
from dropbox_utils import get_dropbox_client, download_image_from_dropbox
from io import BytesIO
from PIL import Image
import base64


def reports():
    st.markdown("""
        <style>
        .report-header {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        .student-card {
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="report-header">
            <h2 style="margin:0;">📊 Student Records & Reports</h2>
            <p style="margin:5px 0 0 0;">Search and view student information</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Load all student data
    db = Database()
    df = db.get_all_students()
    
    if df.empty:
        st.info("📝 No student records found. Please register students first.")
        return
    
    st.success(f"📚 Total Students: **{len(df)}**")
    
    # Search and Filter Section
    st.markdown("### 🔍 Search & Filter")
    
    with st.expander("Search Options", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_name = st.text_input("Student Name", placeholder="Search by name")
            search_class = st.multiselect(
                "Class",
                options=["All"] + sorted(df['class'].unique().tolist()) if 'class' in df.columns else ["All"]
            )
        
        with col2:
            search_city = st.text_input("City", placeholder="Search by city")
            search_area = st.text_input("Area", placeholder="Search by area")
        
        with col3:
            search_parent = st.text_input("Parent Name", placeholder="Search by parent name")
            search_talent = st.text_input("Special Talent", placeholder="Search by talent")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            search_button = st.button("🔎 Search", use_container_width=True)
        with col2:
            clear_button = st.button("🔄 Clear Filters", use_container_width=True)
    
    # Apply filters
    filtered_df = df.copy()
    
    if search_button or search_name or search_city or search_area or search_parent or search_talent:
        if search_name:
            filtered_df = filtered_df[filtered_df['name'].str.contains(search_name, case=False, na=False)]
        
        if search_class and "All" not in search_class:
            filtered_df = filtered_df[filtered_df['class'].isin(search_class)]
        
        if search_city:
            filtered_df = filtered_df[filtered_df['city'].str.contains(search_city, case=False, na=False)]
        
        if search_area:
            filtered_df = filtered_df[filtered_df['area'].str.contains(search_area, case=False, na=False)]
        
        if search_parent:
            filtered_df = filtered_df[filtered_df['parent_name'].str.contains(search_parent, case=False, na=False)]
        
        if search_talent:
            filtered_df = filtered_df[filtered_df['special_talent'].str.contains(search_talent, case=False, na=False)]
    
    st.markdown(f"### 📋 Search Results ({len(filtered_df)} students)")
    
    if filtered_df.empty:
        st.warning("No students found matching your search criteria.")
        return
    
    # Display options
    view_mode = st.radio("View Mode", ["Card View", "Table View"], horizontal=True)
    
    if view_mode == "Card View":
        # Card View - showing students with photos
        dbx = get_dropbox_client()
        
        for idx, row in filtered_df.iterrows():
            with st.container():
                col1, col2, col3 = st.columns([1, 2, 2])
                
                with col1:
                    # Try to load and display student photo
                    try:
                        if dbx:
                            image_bytes = download_image_from_dropbox(dbx, str(row['id']))
                            if image_bytes:
                                img = Image.open(BytesIO(image_bytes))
                                st.image(img, width=150, caption=f"ID: {row['id']}")
                            else:
                                st.image("https://via.placeholder.com/150?text=No+Photo", width=150)
                        else:
                            st.image("https://via.placeholder.com/150?text=No+Photo", width=150)
                    except:
                        st.image("https://via.placeholder.com/150?text=No+Photo", width=150)
                
                with col2:
                    st.markdown(f"**👤 Name:** {row.get('name', 'N/A')}")
                    st.markdown(f"**🆔 Student ID:** {row.get('id', 'N/A')}")
                    st.markdown(f"**📚 Class:** {row.get('class', 'N/A')}")
                    st.markdown(f"**👥 Gender:** {row.get('gender', 'N/A')}")
                    st.markdown(f"**🎂 DOB:** {row.get('dob', 'N/A')}")
                    st.markdown(f"**🩸 Blood Group:** {row.get('blood_group', 'N/A')}")
                
                with col3:
                    st.markdown(f"**📍 Address:** {row.get('address', 'N/A')}")
                    st.markdown(f"**🏘️ Area:** {row.get('area', 'N/A')}")
                    st.markdown(f"**🏙️ City:** {row.get('city', 'N/A')}")
                    st.markdown(f"**📮 Pincode:** {row.get('pincode', 'N/A')}")
                    st.markdown(f"**⭐ Special Talent:** {row.get('special_talent', 'N/A')}")
                
                # Expandable section for more details
                with st.expander("👨‍👩‍👧 Parent Details & More"):
                    pcol1, pcol2 = st.columns(2)
                    
                    with pcol1:
                        st.markdown("**Parent/Guardian Information:**")
                        st.markdown(f"- **Name:** {row.get('parent_name', 'N/A')}")
                        st.markdown(f"- **Relation:** {row.get('parent_relation', 'N/A')}")
                        st.markdown(f"- **Contact:** {row.get('parent_contact', 'N/A')}")
                        st.markdown(f"- **Occupation:** {row.get('parent_occupation', 'N/A')}")
                        st.markdown(f"- **Email:** {row.get('parent_email', 'N/A')}")
                        st.markdown(f"- **Emergency:** {row.get('emergency_contact', 'N/A')}")
                    
                    with pcol2:
                        st.markdown("**Academic Information:**")
                        st.markdown(f"- **Admission Date:** {row.get('admission_date', 'N/A')}")
                        st.markdown(f"- **Previous School:** {row.get('previous_school', 'N/A')}")
                        st.markdown(f"- **Achievements:** {row.get('achievements', 'N/A')}")
                        st.markdown(f"- **Medical Conditions:** {row.get('medical_conditions', 'N/A')}")
                        st.markdown(f"- **Notes:** {row.get('additional_notes', 'N/A')}")
                
                st.markdown("---")
    
    else:
        # Table View
        # Select columns to display
        display_columns = st.multiselect(
            "Select columns to display",
            options=filtered_df.columns.tolist(),
            default=['id', 'name', 'class', 'gender', 'parent_name', 'parent_contact', 'city'] if all(col in filtered_df.columns for col in ['id', 'name', 'class']) else filtered_df.columns.tolist()[:7]
        )
        
        if display_columns:
            st.dataframe(
                filtered_df[display_columns],
                use_container_width=True,
                height=400
            )
        else:
            st.dataframe(filtered_df, use_container_width=True, height=400)
    
    # Export options
    st.markdown("### 📥 Export Data")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Export to CSV
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📄 Download as CSV",
            data=csv,
            file_name=f"students_report_{pd.Timestamp.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    with col2:
        # Export to Excel
        from io import BytesIO
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            filtered_df.to_excel(writer, sheet_name='Students', index=False)
        
        st.download_button(
            label="📊 Download as Excel",
            data=buffer.getvalue(),
            file_name=f"students_report_{pd.Timestamp.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.ms-excel",
            use_container_width=True
        )
    
    with col3:
        st.info(f"📊 {len(filtered_df)} records ready to export")
    
    # Summary Statistics
    st.markdown("### 📈 Quick Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Students", len(filtered_df))
    
    with col2:
        if 'gender' in filtered_df.columns:
            male_count = len(filtered_df[filtered_df['gender'] == 'Male'])
            st.metric("Male Students", male_count)
    
    with col3:
        if 'gender' in filtered_df.columns:
            female_count = len(filtered_df[filtered_df['gender'] == 'Female'])
            st.metric("Female Students", female_count)
    
    with col4:
        if 'class' in filtered_df.columns:
            classes_count = filtered_df['class'].nunique()
            st.metric("Classes", classes_count)
