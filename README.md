# NLP Experiments using Digital Corpus of Sanskrit

For a [Sanskrit parser project](https://github.com/kmadathil/sanskrit_parser) that I am collaborating on, we have been discussing and investigating different language models, and their applicability to parsing Sanskrit. I have been particularly interested in deep learning approaches for language modeling, such as Seq2Seq (+ attention), etc.

This git repository contains scripts and ipython notebooks with my experiments.

## Word2vec using sentence roots
A building block in many of these deep learning approaches is the embedding of words in a vector space using word2vec or GloVe. [This notebook](word2vec_experiments.ipynb) contains some of my experiments with word2vec using the Digital Corpus of Sanskrit to investigate the feasibility of using word2vec on just root words (prAtipadikas/dhAtus) in Sanskrit.

The DCS database is quite small from a deep learning perspective (about 30 MB if we count just the root words), so it was unclear how good the results would be or what to expect. (Spoiler - I was pleasantly surprised by the quality of the results obtained for a first pass).