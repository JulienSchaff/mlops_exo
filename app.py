from transformers import AutoModelForCausalLM, AutoTokenizer
from fastapi import FastAPI
import torch
app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

@app.post("/chat")
def predict(data: dict):
    input_text = data["input"]
    new_user_input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')
    response = model.generate(new_user_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    return {"response": tokenizer.decode(response[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)}