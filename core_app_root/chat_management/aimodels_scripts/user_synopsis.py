from transformers import AutoTokenizer, OPTForQuestionAnswering
import torch

def process_user_response(question,answer):
    torch.manual_seed(4)
    
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")
    model = OPTForQuestionAnswering.from_pretrained("facebook/opt-350m")

    question, text = question, answer

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
    return predicted