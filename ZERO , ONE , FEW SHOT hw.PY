from transformers import GPT2LMHeadModel , GPT2Tokenizer

import torch 

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def get_response(prompt , max_length = 100):
    inputs = tokenizer.encode(prompt , return_tensors = "pt" , ).to(device)

    output = model.generate(
        inputs,
        max_length = max_length,
        do_sample = True,
        tempreature = 0.7,
        top_p = 0.95,
        repition_penalty = 1.2,
        num_return_sequences = 1,
        pad_token_id = tokenizer.eos_token_id
    )

    response = tokenizer.decode(output[0],skip_tokens_symbols = True)
    return response

question = "what are the benefits of exercise?"
print(get_response(question))

command = "explain why the sky appears blue during the day scientifically"
print("\n",get_response(command))