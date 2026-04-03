import streamlit as st

# Dummy product data
products = {
    "Laptop": 60000,
    "Phone": 30000,
    "Headphones": 3000
}

st.title("E-Commerce Testing Demo")

# Session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# If not logged in, show login only
if not st.session_state.logged_in:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Credentials")

# Product selection and cart (only if logged in)
if st.session_state.logged_in:
    st.subheader("Products")
    selected_product = st.selectbox("Select Product", list(products.keys()))
    quantity = st.number_input("Quantity", min_value=1, step=1)

    if st.button("Add to Cart"):
        total = products[selected_product] * quantity
        st.write(f"Total Price: ₹{total}")