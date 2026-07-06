import streamlit as st
from datetime import date
left, center, right = st.columns([0.5, 5, 0.5])

with center:
    
    st.title("The Recipe Address Book", width = "content")
import pandas as pd
import random 
import helper
added = pd.read_csv("added.csv")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Add Recipe", "look it up", "view options","go on ride","Rate a recipe"])






with tab1:
   
    with st.form("my_form"):
        st.header("Add Recipe")
        st.image("images.jpg")
        recipe_name = st.text_input("Recipe title")
        ingredients = st.text_input("Ingredients", "").split(",")   
        Pre_time_mins = st.number_input("Preparation time (minutes)", min_value= int(0))
        inst = st.text_area("Instructions", "")
        
        Difficulty_level = st.selectbox("Difficulty level", ["Easy", "Medium", "Hard"]) 

        Mealtime =  st.selectbox("Type", ["Dinner", "Lunch", "Breakfast",'Dessert']) 
        
        subbtn = st.form_submit_button(label="Submit")
        if subbtn:
            addedcols = ["Recipe title", "Ingredients", "Preparation time (minutes)", "Instructions", "Difficulty level",  "Meal time", "Rating"]
            row = pd.DataFrame(columns=addedcols, data=[(recipe_name, ingredients, Pre_time_mins, inst , Difficulty_level,  Mealtime , "not rated" )])

            added = pd.concat([added, row])
            added.to_csv("added.csv", index=False)
            st.rerun()

with tab2:
    st.header("search for a recipe")
    st.image("images.jpg")
    search_query = st.text_input("Enter recipe ingredient:")
    # bool_ser = added["Ingredients"].str.contains(search_query, case=False)
    
    if search_query.strip():
        
    
        bool_ser = added["Ingredients"].str.contains(search_query, case=False, na=False)
        
       
        if bool_ser.any():
            st.success(f"Found recipes containing '{search_query}':")
            st.dataframe(added[bool_ser])  
            
        else:
            st.warning("No recipes found with that ingredient. Try another one!")
            
        
    st.info("Type an ingredient above to begin your search.")    
    

with tab3:
    st.header("View")
    st.image("images.jpg")
    left, center, right = st.columns([1, 5, 1])

   
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            if st.button("Breakfast", type="primary" ):
                filtered_df = added[added["Meal time"] == "Breakfast"]
                st.dataframe(filtered_df) 
    with col2:
            if st.button("Lunch", type="primary"):
                st.dataframe(added[added["Meal time"] == "Lunch"])
    with col3:
            if st.button("Dinner", type="primary"):
                st.dataframe(added[added["Meal time"] == "Dinner"])
    with col4:
            if st.button("Dessert", type="primary"):
                st.dataframe(added[added["Meal time"] == "Dessert"])

   

    st.write(added[['Recipe title','Preparation time (minutes)']])
    
    

with tab4:
        st.header("Click below to recive a recipe suggestion")
        st.image("images.jpg")
        if  st.button("Generate Random", type="primary"):

            st.write(added.sample(n=1))
    

    
with tab5:
    st.header("Rate and generate shopping lists")
    st.image("images.jpg")
    st.write("Rate a recipe")
    rated = st.selectbox("recipe you want to rate", added["Recipe title"]) 
    rating = st.selectbox("rate receipe", ["1 star", "2 star", "3 star"]) 
    
   
    selctioninx = added["Recipe title"] == rated
    # st.write(added[selctioninx])
    if st.button("Generate shopping list", type="primary"):
          ingredients_list = helper.shoppinglist2(added, "Recipe title", rated)
          st.write("Shopping List:", ingredients_list)  

    if st.button ("rate", type="primary"):
            added.loc[selctioninx, "Rating"] = rating
   
        
            added.to_csv("added.csv", index=False)
            st.rerun()
    st.dataframe(added.sort_values("Rating", ascending=False))

identfier = "recipe title"
# helper.shoppinglist2(identfier, "beef")

