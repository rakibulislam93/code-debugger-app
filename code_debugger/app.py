import streamlit as st
from api_call import code_debugger, parse_debugger_response
from PIL import Image


st.title("🐞 AI Code Debugger App")
st.markdown("Find and fix bugs in your code instantly :zap:")
st.divider()

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.header("Control Panel")

    file_error_box = st.empty()

    images = st.file_uploader(
        "Upload Code Screenshot(s)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )
    if images:
        if len(images) > 3:
            file_error_box.error("Please upload a maximum of 3 images.")
        else:
            st.markdown("Uploaded files")
            col = st.columns(len(images))
            for i, img in enumerate(images):
                col[i].image(img, caption=img.name)

    options = st.selectbox(
        "What do you want?",
        ("Hints", "Solution with code"),
        index=None
    )
    if options:
        st.write(f"You selected **{options}** as your output type.")

    button = st.button("Debug Code",type="primary")
    options_error_box = st.empty()


if button and not images:
    file_error_box.error("Please upload at least one code screenshot to proceed.")

elif button and not options:
    options_error_box.error("Please select an output type to proceed.")


elif button and images and options:
    # Output results based on the selected options
    with st.container(border=True): 
        tab1, tab2, tab3 = st.tabs(["💡 Hints", "📖 Explanation", "✅ Solved Code"])

        with st.spinner("Analyzing code and generating hints..."):
            images = [Image.open(img) for img in images]
            response = code_debugger(images, options)
            hints, explanation, solved_code = parse_debugger_response(response) #parse the response into sections
                
        with tab1:
            if hints:
                st.markdown(hints)
            else:
                st.info("No hints available.")

        with tab2:
            if explanation:
                st.markdown(explanation)
            else:
                st.info("No explanation available.")
        with tab3:
            if solved_code:
                clean_code = solved_code.strip("```python").strip("```") #remove code block formatting if present
                st.code(clean_code)
            else:
                st.info("No solved code available.")
