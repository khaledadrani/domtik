from torchtext.datasets import WikiText2
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator


def remove_duplicates_preserve_order(input_list):
    seen = set()
    return [x for x in input_list if not (x in seen or seen.add(x))]


special_tokens = ['<sos>', '<eos>', '<unk>', '<pad>', '<mask>', '<sep>']

tokenizer = get_tokenizer('basic_english')
# vocab = build_vocab_from_iterator(map(tokenizer, text), specials=special_tokens)
# use this to tokenize
# tokens = special_tokens + tokenizer(text)
# tokens = remove_duplicates_preserve_order(tokens)
# tokens[0], len(tokens)
# stoi = { ch:i for i,ch in enumerate(tokens) }
# itos = { i:ch for i,ch in enumerate(tokens) }
# encode = lambda text: [ stoi.get(token, stoi["<unk>"]) for token in tokenizer(text) ]
# decode = lambda indexes: " ".join([ itos[index] for index in indexes])
# # encoded = encode("before there")
# # print(encoded)
#
# import torch # we use PyTorch: https://pytorch.org
# data = torch.tensor(encode(text), dtype=torch.long)
# print(data.shape, data.dtype)
# print(data[:40])
