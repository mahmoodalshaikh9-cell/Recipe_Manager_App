import streamlit as st
import pandas as pd

def shoppinglist2(added,identfier, value):
    
    inglis = added[identfier].astype(str) == str(value) 
    
    recing = added.loc[inglis, "Ingredients"]
    
 
    return recing.dropna().tolist()
