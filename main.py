import os
import shutil
import streamlit as st

def create_nested_folders(parent_path, structure, file_mapping=None, uploaded_files=None):
    # Ensure the folder structure is created first
    for key, value in structure.items():
        folder_path = os.path.join(parent_path, key)
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

        # Handle file placement
        if file_mapping and key in file_mapping and uploaded_files:
            file = file_mapping[key]
            matching_files = [f for f in uploaded_files if f.name == file]
            if matching_files:
                # Write the file to the folder
                target_file_path = os.path.join(folder_path, matching_files[0].name)
                with open(target_file_path, "wb") as f:
                    f.write(matching_files[0].getbuffer())
                st.info(f"File {matching_files[0].name} saved to {target_file_path}")
            else:
                st.warning(f"File {file} not found in uploaded files.")

        # Recursively create nested folders if needed
        if isinstance(value, dict):
            create_nested_folders(folder_path, value, file_mapping, uploaded_files)

def create_folders_and_allocate_files(location, target_path, uploaded_files=None):
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

        target_path = os.path.join(target_path, "Europe")
        os.makedirs(location_path, exist_ok=True)  # Ensure the main location folder is created
        create_nested_folders(location_path, europe_structure, europe_file_mapping, uploaded_files)
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

        target_path = os.path.join(target_path, "United States")
        os.makedirs(location_path, exist_ok=True)  # Ensure the main location folder is created

        for folder in us_structure:
            folder_path = os.path.join(location_path, folder)
            os.makedirs(folder_path, exist_ok=True)

            if folder in file_mapping and uploaded_files:
                file = file_mapping[folder]
                matching_files = [f for f in uploaded_files if f.name == file]
                if matching_files:
                    target_file_path = os.path.join(folder_path, matching_files[0].name)
                    with open(target_file_path, "wb") as f:
                        f.write(matching_files[0].getbuffer())
                    st.info(f"File {matching_files[0].name} saved to {target_file_path}")
                else:
                    st.warning(f"File {file} not found in uploaded files.")

        st.success("United States folders created and files allocated successfully.")

    else:
        st.error("Invalid location input.")
        return

def main():
    st.title("Document Management System")
    location = st.selectbox("Select Location", ["Europe", "United States"])
    target_path = st.text_input("Enter the path where you want to create the folders:")

    uploaded_files = st.file_uploader("Upload the source files", accept_multiple_files=True, type=["docx"])

    if st.button("Process"):
        if location and target_path and uploaded_files:
            create_folders_and_allocate_files(location, target_path, uploaded_files)
        else:
            st.error("Please provide all inputs (location, target path, and upload files).")

if __name__ == "__main__":
    main()
