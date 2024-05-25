import streamlit as st

def main():
    st.title("Simple Calculator")

    st.write("This is a simple calculator by ABDULLAH.")

    num1 = st.number_input("Enter the first number: ")
    num2 = st.number_input("Enter the second number: ")

    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        result = None
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
                st.error("You can not divide by zero")

        if result is not None:
            st.write(f"The result is: {result}")

if __name__ == "__main__":
    main()
