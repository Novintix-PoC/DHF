import os
import streamlit as st
 
def create_folders(location, target_path):
    if location.lower() == "europe":
        europe_structure = {
            "1": "Introduction",
            "2": {
                "Submission and Technical Documentation contents": {
                    "2.1": "Cover letter",
                    "2.2": "The Technical Documentation",
                    "2.3": "Authorisation for the work to be conducted"
                }
            },
            "3": "Submission Method",
            "4": {
                "Document Format": {
                    "4.1": "Language",
                    "4.2": {
                        "Electronic File Format": {
                            "4.2.1": "Format and file size limits",
                            "4.2.2": "Optical Character Recognition (searchable Format)",
                            "4.2.3": "Bookmarks",
                            "4.2.4": "Signatures"
                        }
                    }
                }
            },
            "5": "Submission process",
            "6": {
                "Additional topics to consider when preparing Technical Documentation for submission": {
                    "6.1": "Manufacturer personnel support",
                    "6.2": "Document availability",
                    "6.3": "Languages",
                    "6.4": "Certificate scope",
                    "6.5": "Subcontractors & Suppliers",
                    "6.6": "Accessories",
                    "6.7": "Novelty"
                }
            },
            "ATTACHMENT A": "Information to provide in a Technical Documentation submission",
            "ATTACHMENT B": "Reference documents"
        }
        location_path = os.path.join(target_path, "Europe")
        os.makedirs(location_path, exist_ok=True)
        def create_nested_folders(parent_path, structure):
            for key, value in structure.items():
                if isinstance(value, dict):
                    folder_path = os.path.join(parent_path, key)
                    os.makedirs(folder_path, exist_ok=True)
                    create_nested_folders(folder_path, value)
                else:
                    folder_path = os.path.join(parent_path, key + " " + value)
                    os.makedirs(folder_path, exist_ok=True)
 
        create_nested_folders(location_path, europe_structure)
 
    elif location.lower() == "united states":
        us_structure = {
            "1": "MEDICAL DEVICE USER FEE COVER SHEET (FORM FDA 3601)",
            "2": "CENTER FOR DEVICES AND RADIOLOGICAL HEALTH (CDRH) PREMARKET REVIEW SUBMISSION COVER SHEET (FORM FDA 3514)",
            "3": "510(K) COVER LETTER",
            "4": "INDICATIONS FOR USE STATEMENT (FORM FDA 3881)",
            "5": "510(K) SUMMARY OR 510(K) STATEMENT",
            "6": "TRUTHFUL AND ACCURATE STATEMENT",
            "7": "CLASS III SUMMARY AND CERTIFICATION",
            "8": "FINANCIAL CERTIFICATION OR DISCLOSURE STATEMENT",
            "9": "DECLARATIONS OF CONFORMITY AND SUMMARY REPORTS",
            "10": "DEVICE DESCRIPTION",
            "11": "EXECUTIVE SUMMARY/PREDICATE COMPARISON",
            "12": "SUBSTANTIAL EQUIVALENCE DISCUSSION",
            "13": "PROPOSED LABELING",
            "14": "STERILIZATION AND SHELF LIFE",
            "15": "BIOCOMPATIBILITY",
            "16": "SOFTWARE",
            "17": "ELECTROMAGNETIC COMPATIBILITY AND ELECTRICAL SAFETY",
            "18": "PERFORMANCE TESTING - BENCH",
            "19": "PERFORMANCE TESTING – ANIMAL",
            "20": "PERFORMANCE TESTING – CLINICAL"
        }
        location_path = os.path.join(target_path, "United States")
        os.makedirs(location_path, exist_ok=True)
 
        for key, value in us_structure.items():
            folder_path = os.path.join(location_path, key + " " + value)
            os.makedirs(folder_path, exist_ok=True)
 
    else:
        st.error("Invalid location input.")
        return
    st.success("Folders created successfully.")
 
def main():
    st.title("Document Management System")
    location = st.selectbox("Select Location", ["Europe", "United States"])
    target_path = st.text_input("Enter the path where you want to create the folders:")
    if st.button("Process"):
        if location and target_path:  # Check if inputs are provided
            create_folders(location, target_path)
            st.success("Task completed successfully.")
 
if __name__ == "__main__":
    main()
