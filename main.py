from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline

PRE_TRAIN_MODEL_NAME = "uer/gpt2-chinese-cluecorpussmall"

tokenizer = BertTokenizer.from_pretrained(PRE_TRAIN_MODEL_NAME)
model = GPT2LMHeadModel.from_pretrained(PRE_TRAIN_MODEL_NAME)

text_generator = TextGenerationPipeline(model, tokenizer)

output = text_generator("西游记里面谁最强？", max_length=100, do_sample=True, return_full_text=False)

print(output)
