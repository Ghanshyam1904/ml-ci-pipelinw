import streamlit as st

# streamlit

st.title('Calculator')
st.write('Enter a number to calculate its square ,cube and power')

# Get user input
n = st.number_input('Enter a number',value=1,step=1)

# Calculate the result
square = n**2
cube = n**3
power = n**n

# Display the result
st.write(f'The square of {n} is {square}')
st.write(f'The cube of {n} is {cube}')
st.write(f'The power of {n} is {power}')