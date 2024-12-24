import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Simple Search Engine", page_icon="🔎", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Roboto', sans-serif;
    }
    .stTextInput > div {
        width: 100%;
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 1rem;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #0056b3;
        color: white;
    }
    .search-results {
        padding: 10px;
        margin-top: 20px;
        background-color: #1e1e1e;
        border-radius: 8px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.5);
    }
    .result-number {
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 5px;
        color: #074799;
    }
    .result-content {
        margin-left: 10px;
        font-size: 1rem;
        color: #D4EBF8;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app
st.markdown("<h1 style='text-align: center; color: #D4EBF8;'>🔎 Document Search Engine</h1>", unsafe_allow_html=True)

# Search bar
query = st.text_input("", placeholder="Enter your search query here...", key="query_input")

# Submit button
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
# if st.button("Search"):
if col4.button("Search"):
    if query:
        try:
            # API URL
            api_url = "http://127.0.0.1:5000/api/search"
            # Make the API call
            response = requests.post(
                api_url,
                headers={"Content-Type": "application/json"},
                json={"query": query}
            )
            # Check if the response is successful
            if response.status_code == 200:
                results = response.json()  # Assuming the API returns a JSON response
                st.markdown(f"<h3 style='text-align: center; color: #D4EBF8; '>Search Results for: \"{query}\"</h3>", unsafe_allow_html=True)
                # print(results)
                # st.write(results)
                
                # Display the results
                if results:
                    responses = results.get("response", [])
                    for i, doc in enumerate(responses, start=1):
                        st.markdown(
                            f"""
                                <div class="search-results">
                                    <div class="result-number"><strong>{i}.<strong></div>
                                    <div class="result-content">{doc.get("text", "No content available")}</div>
                                </div>
                            """,
                            unsafe_allow_html=True
                        )
                else:
                    st.info("No results found.")
            else:
                # st.error(f"Error {response.status_code}: {response.text}")
                st.info("No results found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a search query!")
