import os
import shutil
import streamlit as st

def create_nested_folders(parent_path, structure, file_mapping=None, source_path=None):
    for key, value in structure.items():
        folder_path = os.path.join(parent_path, key)
        os.makedirs(folder_path, exist_ok=True)

        # Copy the corresponding file if available
        if file_mapping and key in file_mapping and source_path:
            file = file_mapping[key]
            source_file = os.path.join(source_path, file)
            if os.path.exists(source_file):
                shutil.copy(source_file, folder_path)
            else:
                st.warning(f"File {file} not found in source directory: {source_path}")

        # Create nested folders if the value is a dictionary
        if isinstance(value, dict):
            create_nested_folders(folder_path, value, file_mapping, source_path)

def create_folders_and_allocate_files(location, target_path, source_path=None):
    if location.lower() == "europe":
        europe_structure = {
            "1. Introduction": {},
            "2. Submission and Technical Documentation contents": {
                "2.1 Cover letter": {},
                "2.2 The Technical Documentation": {},
                "2.3 Authorisation for the work to be conducted": {}
            },
            "3. Submission Method": {},
            "4. Document Format": {
                "4.1 Language": {},
                "4.2 Electronic File Format": {
                    "4.2.1 Format and file size limits": {},
                    "4.2.2 Optical Character Recognition (searchable Format)": {},
                    "4.2.3 Bookmarks": {},
                    "4.2.4 Signatures": {}
                }
            },
            "5. Submission process": {},
            "6. Additional topics to consider when preparing Technical Documentation for submission": {
                "6.1 Manufacturer personnel support": {},
                "6.2 Document availability": {},
                "6.3 Languages": {},
                "6.4 Certificate scope": {},
                "6.5 Subcontractors & Suppliers": {},
                "6.6 Accessories": {},
                "6.7 Novelty": {}
            },
            "7. Information to provide in a Technical Documentation submission": {},
            "8. Reference documents": {}
        }

        europe_file_mapping = {
            "1. Introduction": "CHP.docx",
            "2.1 Cover letter": "DCRM.docx",
            "2.2 The Technical Documentation": "IFU.docx",
            "2.3 Authorisation for the work to be conducted": "MFG PLAN.docx",
            "3. Submission Method": "MPI.docx",
            "4.1 Language": "PMSR.docx",
            "4.2.1 Format and file size limits": "PRM.docx",
            "4.2.2 Optical Character Recognition (searchable Format)": "PVEP.docx",
            "4.2.3 Bookmarks": "PVER.docx",
            "4.2.4 Signatures": "REG DRAWING.docx",
            "5. Submission process": "TMVP.docx",
            "6.1 Manufacturer personnel support": "MFG PLAN.docx",
            "7. Information to provide in a Technical Documentation submission": "PRM.docx",
            "8. Reference documents": "PVEP.docx"
        }

        location_path = os.path.join(target_path, "Europe")
        os.makedirs(location_path, exist_ok=True)
        create_nested_folders(location_path, europe_structure, europe_file_mapping, source_path)
        st.success("Europe folders created and files allocated successfully.")

    elif location.lower() == "united states":
        us_structure = [
            "1 MEDICAL DEVICE USER FEE COVER SHEET (FORM FDA 3601)",
            "2 CENTER FOR DEVICES AND RADIOLOGICAL HEALTH (CDRH) PREMARKET REVIEW SUBMISSION COVER SHEET (FORM FDA 3514)",
            "3 510(K) COVER LETTER",
            "4 INDICATIONS FOR USE STATEMENT (FORM FDA 3881)",
            "5 510(K) SUMMARY OR 510(K) STATEMENT",
            "6 TRUTHFUL AND ACCURATE STATEMENT",
            "7 CLASS III SUMMARY AND CERTIFICATION",
            "8 FINANCIAL CERTIFICATION OR DISCLOSURE STATEMENT",
            "9 DECLARATIONS OF CONFORMITY AND SUMMARY REPORTS",
            "10 DEVICE DESCRIPTION",
            "11 EXECUTIVE SUMMARY/PREDICATE COMPARISON"
        ]

        file_mapping = {
            "1 MEDICAL DEVICE USER FEE COVER SHEET (FORM FDA 3601)": "CHP.docx",
            "2 CENTER FOR DEVICES AND RADIOLOGICAL HEALTH (CDRH) PREMARKET REVIEW SUBMISSION COVER SHEET (FORM FDA 3514)": "DCRM.docx",
            "3 510(K) COVER LETTER": "IFU.docx",
            "4 INDICATIONS FOR USE STATEMENT (FORM FDA 3881)": "MFG PLAN.docx",
            "5 510(K) SUMMARY OR 510(K) STATEMENT": "MPI.docx",
            "6 TRUTHFUL AND ACCURATE STATEMENT": "PMSR.docx",
            "7 CLASS III SUMMARY AND CERTIFICATION": "PRM.docx",
            "8 FINANCIAL CERTIFICATION OR DISCLOSURE STATEMENT": "PVEP.docx",
            "9 DECLARATIONS OF CONFORMITY AND SUMMARY REPORTS": "PVER.docx",
            "10 DEVICE DESCRIPTION": "REG DRAWING.docx",
            "11 EXECUTIVE SUMMARY/PREDICATE COMPARISON": "TMVP.docx"
        }

        location_path = os.path.join(target_path, "United States")
        os.makedirs(location_path, exist_ok=True)

        for folder in us_structure:
            folder_path = os.path.join(location_path, folder)
            os.makedirs(folder_path, exist_ok=True)

            if folder in file_mapping and source_path:
                file = file_mapping[folder]
                source_file = os.path.join(source_path, file)
                if os.path.exists(source_file):
                    shutil.copy(source_file, folder_path)
                else:
                    st.warning(f"File {file} not found in source directory: {source_path}")

        st.success("United States folders created and files allocated successfully.")

    else:
        st.error("Invalid location input.")
        return

def main():
    st.set_page_config(page_title="Document Management System", layout="wide")
    
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        .stApp {
            background: #0e4166;
            font-family: 'Roboto', sans-serif;
        }
        [data-testid=stHeader] {
            background: #0e4166;
        }
        [data-testid=stWidgetLabel] {
            color:#f4a303;
        }
        .stHeading h1 {
            color:#f4a303;
        }
        [data-testid=stAppViewBlockContainer],[data-testid=stVerticalBlock] {
            margin-top:30px;
        }
        .title-container {
            background: rgb(0,27,44);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            text-align:center;
            padding:5px;
            margin-bottom:10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("Document Management System")
    
    location = st.selectbox("Select Location", ["Europe", "United States"])
    target_path = st.text_input("Enter the path where you want to create the folders:")
    source_path = st.text_input("Enter the path where your source files are located:")

    if st.button("Process"):
        if location and target_path:
            create_folders_and_allocate_files(location, target_path, source_path)
            st.success(f"Task completed successfully. Folders and files created in {target_path}")
        else:
            st.error("Please select a location and provide a target path before processing.")

if __name__ == "__main__":
    main()
