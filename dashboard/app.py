import streamlit as st
import pandas as pd
# the following import is to run a python script which is completely external to this dashboard and is not imported as a module.
import subprocess

st.title('AnoukBank Customer Data Dashboard')

st.markdown(
    """ 
    This is a test web application to Streamlit and run the ETL Pipeline. 

    **There's :rainbow[so much] you can do with an ETL Pipeline! (not really)**
    
    click on the button below to run the ETL Pipeline and see a cute animation 
    """
)

# if st.button("Send balloons!"):
#     st.balloons()

if st.button("Run ETL Pipeline"):
    # some flare to make it more fun when the button is clicked to run the ETL pipeline.
    st.balloons()
    # Run the ETL pipeline by executing the main.py script using subprocess.run and passing the command to run the script as a list of arguments to it to execute the script and run the ETL pipeline.
    result = subprocess.run(['python', '../src/main.py'], capture_output=True, text=True)
    # Check if the command was executed successfully by checking the return code of the subprocess.run function and printing the output or error message accordingly to provide feedback on the execution of the ETL pipeline.
    if result.returncode == 0:
        st.success("ETL Pipeline executed successfully!")
        st.text(result.stdout)
    else:
        st.error("Error executing ETL Pipeline.")
        st.text(result.stderr)