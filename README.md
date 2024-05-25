# Byte Pair Encoding (BPE) Tokenizer

Byte Pair Encoding (BPE) is a data compression algorithm that iteratively replaces the most frequent pair of bytes in a text with a single, unused byte, effectively reducing the size of the data

This repository contains code to train and use two types of tokenizers:
1. Basic_Tokenizer - The simplest implementation of the BPE algorithm, does not handle special tokens. 

2. Regex_Tokenizer - Before tokenization, the input text is split using a regex pattern, the splitting ensures that text is divided into meaningful categories such as letters, numbers and punctuation. This also handles special tokens. 

# How to use

Both the Basic_Tokenizer and Regex_Tokenizer inherit from the base tokenizer class [Base.py], which provides the functionaity to train the tokenizers and also provides functions to save and load models. 

To train the model on your custom data in [.txt] format, use the following code

```python
tokenizer_name = 'regex' - #The name of the specific tokenizer you want to train
save_path = r'\models' - #File path to save the models
file = r'sample.txt' - #.txt file containing your custom data
vocab_size = 512 #Vocabulary size, for demonstration set to 512
verbose = #Provides iteration information

from Train import train

train(tokenizer_name, save_path, vocab_size, file, verbose=True)

```

The train function will save the trained model in a .model file in the save_path

To use this model for inference 

```python
from Basic_Tokenizer import BasicTokenizer

tokenizer = BasicTokenizer()
tokenizer.load(model)

# Encode text

text = "Hello, how are you"
tokenizer.encode(text)

# Decode ids

tokenizer.decode(ids)
```

**Special Tokens** = You can register special tokens when using the RegexTokenizer, to do so use the `register_special_tokens` function. 

```python
from Regex_Tokenizer import RegexTokenizer
tokenizer = RegexTokenizer()
vocab_size = 32768

train(tokenizer_name, save_path, vocab_size, file, verbose=True)

tokenizer.register_special_tokens({"<|endoftext|>": 32768})

tokenizer.encode("<|endoftext|>hello world", allowed_special="all")

# allowed_special has 3 modes all, none and none_raise
```






