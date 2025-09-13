import streamlit as st
import pandas

content = """
   I am an aspiring programmmer with a strong foundation in Python,
   currently building practical projects such as custom Youtube Downloader
   and exploring libries like yt-dlp and Pygame for game development.
   I enjoy creating lightweight, efficient code that runs smoothly on low-spec
   hardware, and I've also started experimenting with Lua for scripting and
   automation. I'm comfortable navigating Linux environments, writing Bash scripts,
   and using tools like Lutris and Wine to optimize software compatibility. My learning
   style emphasizes hands-on problem solving, project-based growth, and self-driven
   exploration of new technologies
    """




st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/Photo.jpg")
   
with col2:
    st.title("Philip Joseph")
  
    st.info(content)
st.html("<h1>Below is some apps i have developed, feel free to take a look!<h1\>")

df= pandas.read_csv("data.csv", sep=";")


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.markdown(f"[Source code]({row['url']})")

with empty_col:
    print("this is empyy")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.markdown(f"[Source code]({row['url']})")