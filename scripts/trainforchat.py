import torch
import transformers

torch.manual_seed(4)
tokenizer = transformers.AutoTokenizer.from_pretrained("facebook/opt-350m")
model = transformers.OPTForQuestionAnswering.from_pretrained("facebook/opt-350m")