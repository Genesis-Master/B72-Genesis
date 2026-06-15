import streamlit as st
import streamlit.components.v1 as components

# Set up the main page configuration
st.set_page_config(page_title="B72-Genesis Dashboard", layout="wide")

# This is the master HTML/CSS payload.
# It is defined as a plain multi-line string (no 'f' prefix)
# to avoid syntax errors with CSS curly braces.
html_code = '''
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: #111;
            color: white;
            font-family: sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .dashboard-container {
            text-align: center;
            padding: 20px;
            border: 1px solid #444;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <h1>B72-Genesis Dashboard Active</h1>
        <p>System Initialized: Y10 Blueprint Logic</p>
    </div>
</body>
</html>
'''

# Rendering the component
st.title("B72-Genesis Workspace")
components.html(html_code, height=650, scrolling=True)
