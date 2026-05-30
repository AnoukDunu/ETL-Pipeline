# IGNORE THIS FILE COMPLETELY. THIS FILE IS NOT USED IN THE PROJECT. THIS FILE WAS CREATED TO TEST STREAMLIT AND RUN THE ETL PIPELINE IN A WEB APPLICATION. THIS FILE IS NOT PART OF THE ETL PIPELINE. THIS FILE IS NOT USED IN THE PROJECT. THIS FILE WAS CREATED TO TEST STREAMLIT AND RUN THE ETL PIPELINE IN A WEB APPLICATION. THIS FILE IS NOT PART OF THE ETL PIPELINE. THIS FILE IS NOT USED IN THE PROJECT. THIS FILE WAS CREATED TO TEST STREAMLIT AND RUN THE ETL PIPELINE IN A WEB APPLICATION. THIS FILE IS NOT PART OF THE ETL PIPELINE. THIS FILE IS NOT USED IN THE PROJECT. THIS FILE WAS CREATED TO TEST STREAMLIT AND RUN THE ETL PIPELINE IN A WEB APPLICATION. THIS FILE IS NOT PART OF THE ETL PIPELINE.

# import sys
# from pathlib import Path
# import streamlit as st

# # ====== added to fix pathing issue ======
# ROOT = Path(__file__).resolve().parents[1]
# SRC = ROOT / "src"

# if str(SRC) not in sys.path:
#     sys.path.insert(0, str(SRC))
# # ========================================

# from main import run_pipeline

# st.title("TotallyANZ Bank Customer Data Dashboard")

# st.markdown(
#     """
#     This is a test web application to Streamlit and run the ETL Pipeline.

#     **There's :rainbow[so much] you can do with an ETL Pipeline! (not really)**

#     Click the button below to run the ETL Pipeline and display the transformed and loaded dataframes.
#     """
# )

# if st.button("Run ETL Pipeline"):
#     st.balloons()

#     with st.spinner("Running ETL pipeline..."):
#         try:
#             transformed_df, loaded_df = run_pipeline()
#         except Exception as error:
#             st.error("Error executing ETL Pipeline.")
#             st.exception(error)
#             st.stop()

#     st.success("ETL Pipeline executed successfully!")

#     st.subheader("Transformed dataframe")
#     st.dataframe(transformed_df, use_container_width=True)

#     st.subheader("Loaded dataframe")
#     st.dataframe(loaded_df, use_container_width=True)
#     st.caption(f"Showing {len(loaded_df)} rows.")

    