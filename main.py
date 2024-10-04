import streamlit as st
from collections import defaultdict

def create_nested_folders(structure, file_mapping=None, uploaded_files=None):
    virtual_structure = defaultdict(dict)

    def recursive_create(current_structure, path=""):
        for key, value in current_structure.items():
            current_path = f"{path}/{key}" if path else key
            virtual_structure[current_path] = {}

            if file_mapping and key in file_mapping and uploaded_files:
                file = file_mapping[key]
                matching_files = [f for f in uploaded_files if f.name == file]
                if matching_files:
                    virtual_structure[current_path]["file"] = matching_files[0].name
                    st.info(f"File {matching_files[0].name} would be saved to {current_path}")
                else:
                    st.warning(f"File {file} not found in uploaded files.")

            if isinstance(value, dict):
                recursive_create(value, current_path)

    recursive_create(structure)
    return virtual_structure

def create_folders_and_allocate_files(location, uploaded_files=None):
    if location.lower() == "europe":
        europe_structure = {
            "1. Introduction": {},
            "2. Submission and Technical Documentation contents": {
                "2.1 Cover letter": {},
                "2.2 The Technical Documentation": {},
                "2.3 Authorisation for the work to be conducted": {}
            },
            # ... (rest of the Europe structure)
        }

        europe_file_mapping = {
            "1. Introduction": "CHP.docx",
            "2.1 Cover letter": "DCRM.docx",
            # ... (rest of the Europe file mapping)
        }

        virtual_structure = create_nested_folders(europe_structure, europe_file_mapping, uploaded_files)
        st.success("Europe virtual folder structure created and files allocated successfully.")

    elif location.lower() == "united states":
        us_structure = {
            "1 MEDICAL DEVICE USER FEE COVER SHEET (FORM FDA 3601)": {},
            "2 CENTER FOR DEVICES AND RADIOLOGICAL HEALTH (CDRH) PREMARKET REVIEW SUBMISSION COVER SHEET (FORM FDA 3514)": {},
            # ... (rest of the US structure)
        }

        us_file_mapping = {
            "1 MEDICAL DEVICE USER FEE COVER SHEET (FORM FDA 3601)": "CHP.docx",
            "2 CENTER FOR DEVICES AND RADIOLOGICAL HEALTH (CDRH) PREMARKET REVIEW SUBMISSION COVER SHEET (FORM FDA 3514)": "DCRM.docx",
            # ... (rest of the US file mapping)
        }

        virtual_structure = create_nested_folders(us_structure, us_file_mapping, uploaded_files)
        st.success("United States virtual folder structure created and files allocated successfully.")

    else:
        st.error("Invalid location input.")
        return

    return virtual_structure

def display_virtual_structure(structure, indent=0):
    for path, content in structure.items():
        st.markdown("  " * indent + f"📁 {path.split('/')[-1]}")
        if "file" in content:
            st.markdown("  " * (indent + 1) + f"📄 {content['file']}")
        display_virtual_structure(content, indent + 1)

def main():
    st.title("Virtual Document Management System")
    location = st.selectbox("Select Location", ["Europe", "United States"])

    uploaded_files = st.file_uploader("Upload the source files", accept_multiple_files=True, type=["docx"])

    if st.button("Process"):
        if location and uploaded_files:
            virtual_structure = create_folders_and_allocate_files(location, uploaded_files)
            st.subheader("Virtual Folder Structure:")
            display_virtual_structure(virtual_structure)
        else:
            st.error("Please provide all inputs (location and upload files).")

if __name__ == "__main__":
    main()
