import streamlit as st

# Define functions for each page
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def page_about():
    st.title("About Page")
    st.write("Welcome to the About Page!")

def page_contact():
    st.title("Contact Page")
    st.write("Welcome to the Contact Page!")

# Define a function to display navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", options=["Home", "About", "Contact"])

    if page == "Home":
        page_home()
    elif page == "About":
        page_about()
    elif page == "Contact":
        page_contact()

# Run the main function to start the app
if __name__ == "__main__":
    main()
