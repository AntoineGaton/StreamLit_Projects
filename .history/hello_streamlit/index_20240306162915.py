import streamlit as st

# Title
st.title("My First Streamlit App")

# Text
st.write("Welcome to my Streamlit app!")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Markdown
st.markdown("### This is a markdown")

# Displaying Data
st.write("Here's a DataFrame:")
st.write(dataframe)

# Interactive Widgets
checkbox = st.checkbox("Show/Hide")
if checkbox:
    st.write("Checkbox is ON")
else:
    st.write("Checkbox is OFF")

# Button
button = st.button("Click me!")
if button:
    st.write("Button clicked!")

# Selectbox
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)

# Slider
number = st.slider("Pick a number", 0, 100, 50)
st.write("You picked:", number)
s