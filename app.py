import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline, Conversation

# model_name = "deepset/roberta-base-squad2"
# model_name = "microsoft/DialoGPT-medium"
model_name = "PygmalionAI/pygmalion-6b"
# a) Get predictions
nlp = pipeline('conversational', model=model_name, tokenizer=model_name)
with st.form("my_form"):
   st.write("Inside the form")

   input = st.text_input('What is your current routine?')

   f = open("prompt.txt")
   prompt = f.readlines()
   conversation = Conversation("\n".join(prompt))

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       # QA_input = {
       #     'question': input,
       #     'context':
       # }
       # res = nlp(QA_input)
       st.write("Response:\n")
       conversation = nlp(conversation)
       res = conversation.generated_responses[-1]
       st.write(res)
       st.write("After user input:\n")
       st.write(input)
       conversation.add_user_input(input)
       conversation = nlp(conversation)
       res = conversation.generated_responses
       st.write(res)



# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

