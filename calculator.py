import streamlit as st

# Streamlit app title
st.title("Simple Calculator")

# Input fields for numbers and operator
num1 = st.number_input("Enter first number", step=1.0)
num2 = st.number_input("Enter second number", step=1.0)
operation = st.selectbox("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on the selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Cannot divide by zero")
        result = None

# Display the result
if result is not None:
    st.write(f"Result: {result}")
