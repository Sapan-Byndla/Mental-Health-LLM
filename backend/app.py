from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()

model_path = "/Users/sapan/Desktop/Mental Health LLM/tinyllama"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

class Query(BaseModel):
    question: str

@app.post("/generate")
async def generate_text(query: Query):
    inputs = tokenizer(f"### Question:\n{query.question}\n\n### Answer:", return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=150, temperature=0.7, top_p=0.95, do_sample=True, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"answer": response}
