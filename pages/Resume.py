import streamlit as st
import base64


def displaypdf(file_path):
    # Opening file from file path
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


def main():
    st.title("Resume")
    st.write("Below is my resume:")

    # Call displaypdf function with the path to your PDF file
    displaypdf("pages/Resume.pdf")


if __name__ == "__main__":
    main()
