from transformers import AutoTokenizer, OPTForQuestionAnswering
import torch

torch.manual_seed(4)
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")

# note: we are loading a OPTForQuestionAnswering from the hub here,
# so the head will be randomly initialized, hence the predictions will be random
model = OPTForQuestionAnswering.from_pretrained("facebook/opt-350m")

question, text = "Who was Chrisitan?", "Christian is a an engineer and CEO of codeblaze academy"

inputs = tokenizer(question, text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

answer_start_index = outputs.start_logits.argmax()
answer_end_index = outputs.end_logits.argmax()

answer_offset = len(tokenizer(question)[0])

predict_answer_tokens = inputs.input_ids[
    0, answer_offset + answer_start_index : answer_offset + answer_end_index + 1
]

predicted = tokenizer.decode(predict_answer_tokens)
print(predicted)


