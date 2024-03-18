import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import plotly.graph_objects as go
import google.generativeai as genai

from io import StringIO

st.set_page_config(layout="wide")
st.markdown("""
    <style>
    .reportview-container {
        background: rgb(228, 241, 247);
    }
    .button{
        width: 390px;
        height: 50px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



# Ideal matrix


 

 
genai.configure(api_key="AIzaSyBNKJ5UoqldD8BwNVCwbDHs3GquaZ9OIjM")
 
# Set up the model
generation_config = {
  "temperature": 0,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}
 


model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config
                              )
 




# st.set_page_config(page_title="Client Experience 2.0", layout="wide", initial_sidebar_state="auto")
st.markdown("""
 <style>
 .block-container {
 padding-top: 1rem;
 padding-bottom: 0rem;

 padding-right: 5rem;
 }
 </style>
 """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Product Analysis</h1>", unsafe_allow_html=True)

# st.markdown("<p style='text-align: center; font-size: 20px;'><b>Structured Approaches to Strategic Solutions!</b></p>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; font-size: 18px;'><i>Client Experience 2.0: We are working towards building a repository of key consulting resources to help you improve your client experience from the very first touch point</i></p>", unsafe_allow_html=True)

# if st.session_state.selected_team != 8:
#     st.header("**Case Study:**")
#     st.write('''Client Experience or Customer Experience it does not matter we are MBA graduates, sab kuch ek hi hai. humko bus pagal banana hai. 
#                 Give us anything we will sell it. Pagal banane is our expertise. But today we will learn something important and useful, something which
#                 a B.Tech graduate would like to learn.
#                 ''')

m = st.markdown("""

    <style>
        .multiselect{
            background-color: #6C92B5;
            width: 290px;
            height: 50px;
        }
    </style>
""", unsafe_allow_html=True)



st.sidebar.markdown("<div style='margin-top: -20px;'></div>", unsafe_allow_html=True)
# st.sidebar.image("logoha.png", width=200 )




user_input = st.sidebar.text_input("Enter Product name", "")



home = st.sidebar.button("**Home 🏠**")
st.sidebar.header("Analysis:")
team1_button = st.sidebar.button("**Frequently searched products**")
team2_button = st.sidebar.button("**Top 25 Product on rating**")
team3_button = st.sidebar.button("**Sentiment Analysis**")
team4_button = st.sidebar.button("**Product Enchancement Strategy**")
team5_button = st.sidebar.button("**OverAll Product Strategy**")
# team6_button = st.sidebar.button("**1234**")
# team7_button = st.sidebar.button("**Team7**") 


if 'selected_team' not in st.session_state:
        st.session_state.selected_team = 0

    
if home:
    st.session_state.selected_team=0
elif team1_button:
    st.session_state.selected_team = 1
    
elif team2_button:
    st.session_state.selected_team = 2
elif team3_button:
    st.session_state.selected_team = 3
elif team4_button:
    st.session_state.selected_team =4
elif team5_button:
    st.session_state.selected_team =5
# elif team6_button:
#     st.session_state.selected_team =6
# elif team7_button:
#     st.session_state.selected_team =7
# elif result:
#     st.session_state.selected_team =8








col1,col3=st.columns([2.5,1])

with col1:
    

    
    if st.session_state.selected_team==0:
        # st.markdown("<p style='text-al    ign: left; font-size: 24px;'><b>🎯Product Insights::</b></p>", unsafe_allow_html=True)
        st.subheader("Wlecome to our Platform!!")
        st.write("**Comprehensive Reports**: Gain access to detailed information on top products across various categories, including prices, reviews, and best seller rankings.")
        st.write("")
        
        st.write("**Insightful Analyses**: Understand customer sentiments with our analyses, which include")
        st.write("**Overall Review Summary**: Get a detailed overview of customer opinions distilled into key insights, aiding informed decision-making.")
        st.write("**Sentiment Analysis**: Dive deeper into customer sentiments, uncovering emotional nuances and satisfaction levels.")
        st.write("")
        st.write("**Actionable Strategies**: Elevate your products with our detailed improvement strategies aimed at meeting and surpassing customer expectations.")
        
    if st.session_state.selected_team==1:
        st.header("Analysis📊:")
        st.subheader("most searched products:") 
        prompt_part1 = [ 
    "find on e-commerce platforms,Identify the most searched products in the (top 20 helathcare & medical device) category and subcategory is (blood pressure device) on over all ecommerce platform don't provide information on the basis of platform."
   ]
        response1 = model.generate_content(prompt_part1)
        content_text = response1.text
        st.write(content_text)




    if st.session_state.selected_team==2:

        st.subheader("Top 25 Product based on rating and review :") 
        prompt_part2 = [ 
    "Discover the top(25)-searched healthcare and medical devices, specifically focusing on blood pressure monitoring devices, across all e-commerce platforms. Extract details such as category,sub_category product name, brand, price, rating, review count, country of origin (India), and best sellers rank for each product."
   ]
 
        response2 = model.generate_content(prompt_part2)
        response0 = response2.text

        # Convert the response text into a file-like object for pandas
        file_like_object = StringIO(response0)

        # Read the data into a DataFrame, skipping the first row to avoid headers
        df = pd.read_table(file_like_object, sep='|', skiprows=1, skipinitialspace=True)

        # Display the DataFrame
        # df

        # Strip leading/trailing whitespaces from column names
        df.columns = df.columns.str.strip()

        # Remove leading/trailing whitespaces from each entry in the DataFrame
        df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

        
        df = df.drop(['Unnamed: 0','Unnamed: 11'], axis=1)


        # removing 1st row from df bcoz of nan value
        df = df[1:]

        # Remove commas and convert 'Price (INR),review count', 'Review Count', and 'Best Sellers Rank' columns to integer
        df['Price (INR)'] = df['Price (INR)'].str.replace(',', '').astype(int)
        df['Review Count'] = df['Review Count'].str.replace(',', '').astype(int)
        df['Best Sellers Rank'] = df['Best Sellers Rank'].astype(int)

        # Keep 'Rating' column as float
        df['Rating'] = df['Rating'].astype(float)
        st.write(df)

        mean_ratings = df.groupby('Brand')['Rating'].mean().reset_index()
        mean_ratings_sorted = mean_ratings.sort_values(by='Rating', ascending=False)

    # Plotting the bar graph for mean ratings
        plt.figure(figsize=(10, 6))
        bars = plt.bar(mean_ratings_sorted['Brand'], mean_ratings_sorted['Rating'], color='skyblue')

        # Adding labels and title
        plt.xlabel('Brand')
        plt.ylabel('Mean Rating')
        plt.title('Mean Rating of Blood Pressure Monitoring Devices by Brand')

        # Rotating x-axis labels for better readability
        plt.xticks(rotation=90)

        # Annotate each bar with its rating (rotated 90 degrees)
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height, '%.2f' % height, ha='center', va='bottom', rotation=0)
        
        # Display the plot
        st.pyplot(plt)

    if st.session_state.selected_team==3:
        
        st.subheader("Sentiment Analysis")         
        prompt_part3 = [
        """Discover the top(20) serched blood pressure monitoring devices, across all e-commerce platforms in india. and give  the positive and negative sentiments by percentage of each products drill-down in what is the most comman positive reviews and what is the most comman nagative reviews,and OverAll Customer Review Summary for each product by product.
        output like be productname:
        
               

                provide a customer review summary in 3-4 lines of each product basis on the customer reveiw also:

                output should be 

                review summary:

                positive(percentage):

                negative(percentage):
                

            
                                                                                                                                                                                                                                                                                                                                                            
        """]

        response3 = model.generate_content(prompt_part3)
        st.write(response3.text)
        
    
        
    if st.session_state.selected_team==4:
        st.subheader("Product Enhancement Strategy") 

        prompt_part4 = [ 
    "Develop a product improvement strategy for each product based on competitors' top-performing products in the list. The strategy should focus on enhancing the features or addressing shortcomings identified in the competitor products to maintain or improve competitiveness. where the category is healthcare and subcategory is blood pressure monitor device"
   ]
 
 
        response4 = model.generate_content(prompt_part4)

# Access the 'text' attribute of the response object
        response_text04 = response4.text

        st.write(response_text04)


       
        
    
    if st.session_state.selected_team==5:
        st.subheader("Overall Product Strategy:")
        prompt_part5=[
       """ Develop a product enhancement strategy for blood pressure monitoring devices based on insights from competitors and customer preferences. Address key aspects such as accuracy and reliability, user interface and design, connectivity and data management, as well as additional features and value-adds. Ensure to include relevant insights, strategies, and percentages for each aspect.
       """]
        response5=model.generate_content(prompt_part5)
        st.write(response5.text)
       


    # if st.session_state.selected_team==6:
    #     st.subheader("Innovation Matrix💡:")
    #     st.write("Allocate your total budget according to the below matrix:")     
    #     st.write("**Team 6**")
       
      

    # if st.session_state.selected_team==7:
    #     st.header("Innovation Matrix💡:")
    #     st.write("Allocate your total budget according to the below matrix:")     
    #     st.write("**Team 7**") 

footer = """
<style>
a:link, a:visited {
    color: white;
    background-color: transparent;
    text-decoration: underline;
}
a:hover, a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    color: black;
    text-align: right;
    margin-right: 5px;
    margin-bottom: 5px;
}
</style>
<div class="footer">
    <p>Powered By <a style='color:black;' href="https://healtharkinsights.com/analytics-demo/" target="_blank">Team-5©</a></p>
</div>
"""
# st.markdown(footer, unsafe_allow_html=True)
# if st.session_state.selected_team==8:
        
#         st.header("Result Summary📖")

       
       
