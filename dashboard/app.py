import sys
from pathlib import Path
import streamlit as st

# ====== added to fix pathing issue ======
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
# ========================================

from main import run_pipeline

st.title("TotallyANZ Bank Customer Data Dashboard")

st.markdown(
    """
    This is a test web application to Streamlit and run the ETL Pipeline.

    **There's :rainbow[so much] you can do with an ETL Pipeline! (not really)**

    Click the button below to run the ETL Pipeline and display the transformed and loaded dataframes.
    """
)

if st.button("Run ETL Pipeline"):
    st.balloons()

    # result = subprocess.run(['python', '../src/main.py'], capture_output=True, text=True)
    with st.spinner("Running ETL pipeline..."):    
        try:
            # this is because an error is thrown on runtime.  object is a Python tuple containing two identical Pandas DataFrames, one for the transformed data and one for the loaded data. The load function in the load.py script is designed to return the transformed dataframe after loading it into the database, so that it can be displayed in the Streamlit app. However, due to an error in the load function, it is currently returning a tuple containing both the transformed and loaded dataframes instead of just the transformed dataframe. This is why we are seeing two identical dataframes being displayed in the Streamlit app instead of just one.
            # Streamlit's st.dataframe() and st.table() require a single, standalone DataFrame, Series, or convertible data structure st.dataframe. Passing a tuple throws this exception.
            # This is fixed by unpacking the tuple by using two variables.
            # loaded_df1, loaded_df2 = run_pipeline()
            loaded_df1 = run_pipeline()
        except Exception as error:
            st.error("Error executing ETL Pipeline.")
            st.exception(error)
            st.stop()

    st.success("ETL Pipeline executed successfully!")

    st.subheader("Transformed and loaded dataframe")
    st.dataframe(loaded_df1, use_container_width=True)
    st.caption(f"Showing {len(loaded_df1)} rows.")
