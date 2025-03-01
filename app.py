import streamlit as st 
import json

DATA_FILE = "students.json"

def load_data(): 
    try:
        with open(DATA_FILE, "r") as file: 
            return json.load(file) 
    except FileNotFoundError:
             return {}

def save_data(data):
     with open(DATA_FILE, "w") as file:
         json.dump(data, file, indent=4)

def main():
     st.title("Student Data Collection")

menu = ["Add Student", "Search Student"]
choice = st.sidebar.selectbox("Choose an option", menu)

students = load_data()

if choice == "Add Student":
    st.header("Enter Student Details")
    roll_no = st.text_input("Roll Number")
    name = st.text_input("Name")
    father_name = st.text_input("Father's Name")
    address = st.text_area("Address")
    phone = st.text_input("Phone Number")
    student_class = st.text_input("Class")
    
    if st.button("Save Student"):
        if roll_no and name and father_name and address and phone and student_class:
            students[roll_no] = {
                "Name": name,
                "Father's Name": father_name,
                "Address": address,
                "Phone": phone,
                "Class": student_class
            }
            save_data(students)
            st.success("Student data saved successfully!")
        else:
            st.error("Please fill all fields!")

elif choice == "Search Student":
    st.header("Search Student by Roll Number")
    search_roll = st.text_input("Enter Roll Number")
    if st.button("Search"):
        if search_roll in students:
            st.json(students[search_roll])
        else:
            st.error("Student not found!")

if __name__ == "__main__":
     main()