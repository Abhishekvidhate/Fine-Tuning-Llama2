# Use the text generation pipeline to ask questions
# Note that I’m formatting the input to match Llama 2 prompt template

# format :
#    System Prompt (optional) to guide the model
#    User prompt (required) to give the instruction
#    Model Answer (required)

# Ignore warnings
logging.set_verbosity(logging.CRITICAL)

# Run text generation pipeline with our next model
prompt = "how created you?"
pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200)
result = pipe(f"<s>[INST] {prompt} [/INST]")
print(result[0]['generated_text'])