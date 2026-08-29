import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



#file uplaoder window
uploaded_file= st.file_uploader('Choose a CSV file', type='csv')

 #asking user for the number of rows they want to display
rows=st.text_input('Enter the number of rows you want displayed:', max_chars=1)
passed=False
try:
    validate=int(rows)
    passed=True
except:
    st.write('Enter an integer between 1-9')



if uploaded_file is not None and passed==True:

    st.write('File uploaded...')

    #reading and rendering data in file
    dataframe= pd.read_csv(uploaded_file)

    #displaying a subheading and a data preview
    st.subheader('Data Preview')

    #the df.head() method in pandas returns the first n rows of a DataFrame or Series. n is 5 by default
    #.head(n)
    st.write(dataframe.head(n=int(rows)))

    #filtering data
    st.subheader('Filter Data')
    #In pandas, df.columns is an attribute that returns the column labels of a DataFrame as a pandas.Index object
    #.tolist turns it into a python object/list
    columns=dataframe.columns.tolist()
    #widget to give dropdown list
    selected_column= st.selectbox('Select column you want to filter by:',columns)
    #select unique values from slected column
    unique_values= dataframe[selected_column].unique()
    unique_value= st.selectbox('Select a value:',unique_values)

    #displaying similar data in a grid
    filtered_dataframe= dataframe[dataframe[selected_column]==unique_value]
    st.write(filtered_dataframe)

