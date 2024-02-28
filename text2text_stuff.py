from transformers import pipeline

corrector = pipeline(
    "text2text-generation",
    "pszemraj/flan-t5-large-grammar-synthesis",
)

raw_text = "Iwen 2the store yesturday to bye some food. I needd milk, bread, andafew otter things. The $$tore was reely crowed and I had a hard time finding everyting I needed. I finaly madeit t0 dacheck 0ut line and payed for my stuff."
print(f"input text:\n\t{raw_text}")

params = {
    'max_length':64,
    'repetition_penalty':1.05,
    'early_stopping':True,
    'num_beams':4
}

results = corrector(raw_text, **params)
print(results[0]['generated_text'], "\n"*2)
