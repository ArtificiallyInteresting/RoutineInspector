import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
with st.form("my_form"):
   st.write("Inside the form")

   input = st.text_input('What is your current routine?')

   f = open("prompt.txt")
   prompt = f.readlines()

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       QA_input = {
           'question': input,
           'context': "\n".join(prompt)
       }
       res = nlp(QA_input)
       st.write(res)



# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

