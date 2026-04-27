import streamlit as st
import pandas as pd

# ---------------- PAGE ----------------
st.set_page_config(page_title="My Basket", layout="wide")

# ---------------- SESSION LOGIN ----------------
if "login" not in st.session_state:
    st.session_state.login = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.login:
    st.title("🔐 Login - My Basket")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.login = True
            st.success("Login successful!")
        else:
            st.error("Invalid login")

# ---------------- MAIN APP ----------------
else:
    st.title("🛒 My Basket (BigBasket Style App)")

    # ---------------- DATA ----------------
    data = {
        "Product": ["Rice", "Dal", "Oil", "Milk", "Bread", "Apple", "Soap", "Shampoo"],
        "Category": ["Grocery", "Grocery", "Grocery", "Dairy", "Bakery", "Fruits", "Personal", "Personal"],
        "Price": [60, 80, 150, 50, 40, 120, 35, 180],
        "Rating": [4.5, 4.2, 4.3, 4.6, 4.1, 4.4, 4.0, 4.3]
    }

    df = pd.DataFrame(data)

    # ---------------- SIDEBAR ----------------
    st.sidebar.title("🧾 Menu")
    menu = st.sidebar.radio("Go to", ["Home", "Products", "Offers", "Recommendation"])

    # ---------------- HOME ----------------
    if menu == "Home":
        st.subheader("🏠 Welcome to My Basket")
        st.info("Best grocery deals for you!")

    # ---------------- PRODUCTS ----------------
    elif menu == "Products":
        st.subheader("🛍️ All Products")

        for i in range(len(df)):
            st.write(f"👉 {df['Product'][i]} | ₹{df['Price'][i]} | ⭐ {df['Rating'][i]}")

    # ---------------- OFFERS ----------------
    elif menu == "Offers":
        st.subheader("🔥 Today's Offers")

        st.success("🎉 20% OFF on Groceries")
        st.success("🥛 Buy 1 Get 1 Free on Dairy")
        st.success("🍎 Fresh Fruits Discount")

    # ---------------- RECOMMENDATION ----------------
    elif menu == "Recommendation":
        st.subheader("🤖 Smart Recommendation")

        product = st.selectbox("Choose product", df["Product"])

        selected = df[df["Product"] == product]
        category = selected.iloc[0]["Category"]

        st.write(f"### Similar products in {category}")

        rec = df[df["Category"] == category]

        for _, row in rec.iterrows():
            if row["Product"] != product:
                st.write(f"👉 {row['Product']} | ₹{row['Price']} | ⭐ {row['Rating']}")

    # ---------------- LOGOUT ----------------
    if st.sidebar.button("Logout"):
        st.session_state.login = False