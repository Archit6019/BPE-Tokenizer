import os
import time
from Basic_Tokenizer  import BasicTokenizer
from Regex_Tokenizer import RegexTokenizer

def train(tokenizer_name : str, save_path : str, vocab_size : int, file, verbose = False):
    text = open(file, 'r', encoding="utf-8").read()
    tokenizer = None
    if tokenizer_name == 'basic':
        t0 = time.time()
        tokenizer = BasicTokenizer()
        tokenizer.train(text, vocab_size=vocab_size, verbose=verbose)
        path = os.path.join(save_path, tokenizer_name)
        tokenizer.save(path)
        t1 = time.time()
        print(f"Training took {t1 - t0:.2f} seconds")
    elif tokenizer_name == 'regex':
        t0 = time.time()
        tokenizer = RegexTokenizer()
        tokenizer.train(text, vocab_size=vocab_size, verbose=verbose)
        path = os.path.join(save_path, tokenizer_name)
        tokenizer.save(path)
        t1 = time.time()
        print(f"Training took {t1 - t0:.2f} seconds")

# if __name__ == '__main__':
#     tokenizer_name = 'basic'
#     save_path = r'\models'
#     file = r'sample.txt'
#     vocab_size=512
#     train(tokenizer_name, save_path, vocab_size, file, verbose=True)

