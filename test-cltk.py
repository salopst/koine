# 2022-08-02T05:28:04+0100
# https://www.youtube.com/watch?v=OtxC44b1rws

## reload pipewire
# systemctl --user restart pipewire pipewire-pulse and systemctl --user daemon-reload
# systemctl --user daemon-reload

## restart pipewire
systemctl --user restart pipewire.service && systemctl --user restart pipewire-pulse.service
# https://linuxmusicians.com/viewtopic.php?f=6&t=23272
sudo nano "options snd_usb_audio vid=0x1235 pid=0x8210 device_setup=1" > /etc/modprobe.d/scarlett.conf
# reboot, then:
dmesg|grep -A 5 -B 5 Scarlett
alsamixer -cUSB



########## TEST CLTK INSTALLATION ##########

# some stuff will be downloaded on first run

import cltk
import numpy as np
## 0.10
# from cltk.stem.latin.declension   import CollatinusDecliner

## 1.0
from cltk.morphology.lat  import CollatinusDecliner

from cltk import NLP
from cltk.languages.example_texts import get_example_text

## 0.10
# from cktk.corpus.utils. import CorpusImporter

## Un poco de inspección
print(f"cltk version: {cltk.__version__}")
print(f"cltk.__path__: {cltk.__path__}")
print(f"cltk.__file__: {cltk.__file__}")
print(f"cltk.__class__: {cltk.__class__}")
print(f"cltk.__doc__: {cltk.__doc__}")
print(f"cltk.__name__: {cltk.__name__}")
print(f"cltk.__package__: {cltk.__package__}")
print(f"cltk.__spec__: {cltk.__spec__}")

grc_example = get_example_text('grc')
lat_example = get_example_text('lat')
ang_example = get_example_text('ang')

example_texts = {'grc': grc_example, 'lat': lat_example, 'ang': ang_example}
# for iso, text in example_texts:
#   print(f"EXAMPLE TEXT ({iso}): {text[0]}")
print(f"EXAMPLE TEXT: {example_texts}\n")
print(f"len(example_texts): {len(example_texts)}\n")

##############################
cltk_grc_nlp = NLP(language="grc", suppress_banner=True)
cltk_grc_doc = cltk_grc_nlp.analyze(text=get_example_text("grc"))
cltk_lat_nlp = NLP(language="lat", suppress_banner=True)
cltk_lat_doc = cltk_lat_nlp.analyze(text=get_example_text("lat"))
cltk_ang_nlp = NLP(language="ang", suppress_banner=True)
cltk_ang_doc = cltk_ang_nlp.analyze(text=get_example_text("ang"))

## v 0.10
# from cltk.corpus.utils.importer import CorpusImporter
# corpus_importer = CorpusImporter('latin', 'latin_text_perseus')
# print(f"corpora list: {corpus_importer.list_corpora()}")
# corpus_importer.import_corpus('latin_treebank_perseus')

## v 1.0
from cltk.data.fetch import FetchCorpus

# my_langs = ['lat', 'grc', 'ang']
# for lang in my_langs:
#   model_name = lang + '_models_cltk'
#   corpus_downloader = FetchCorpus(language=lang)
#   corpus_downloader.import_corpus(model_name)
#   print(f"available corpora for {lang}: {corpus_downloader.list_corpora}")

### Aaaand in longhand
## should have been done already... see https://stephen.yearl.us/anaconda-and-language-processing-installs/

corpus_downloader = FetchCorpus(language="lat")
#corpus_downloader.import_corpus("lat_models_cltk")
corpus_downloader.import_corpus("lat_text_perseus") # does not exist--(wtf?)

## Greek 
#corpus_downloader = FetchCorpus(language="grc")
#corpus_downloader.import_corpus("grc_models_cltk")
# corpus_downloader.import_corpus("greek_treebank_perseus")
# In linguistics, a treebank is a parsed text corpus that annotates syntactic or semantic sentence structure. The construction of parsed corpora in the early ...

##### Check what corpora are available
#
print(f"FetchCorpus.__dict__: {FetchCorpus.__dict__}")
print("\n\n--------------------------\n\n")
print(f"corpus_downloader.__dict__: {corpus_downloader.__dict__}")

##### from cltk locally installed
# corpus_importer.import_corpus('greek_treebank_perseus', '~/ctlk_data/')

## from custom git repos declared in ~/cltk_data/distributed_corpora.yaml with the  format:

# example_distributed_latin_corpus:
#     origin: https://github.com/kylepjohnson/latin_corpus_newton_example.git
#     language: latin
#     type: text

# example_distributed_greek_corpus:
#     origin: https://github.com/kylepjohnson/a_nonexistent_repo.git
#     language: pali
#     type: treebank


##### all below work #####

# forty_two_chars = cltk_grc_doc.raw[:42]
# print(f"forty_two_chars: {forty_two_chars}")

# isinstance(cltk_grc_doc.raw, str)
# print(f"isinstance(cltk_lat_doc.raw, str): {isinstance(cltk_lat_doc.raw, str)}")

# cltk_grc_doc.tokens[:10]
# print(f"cltk_grc_doc.tokens[:10]: {cltk_grc_doc.tokens[:10]}")

# cltk_grc_doc.tokens_stops_filtered[:10]
# print(f"cltk_grc_doc.tokens_stops_filtered[:10]: {cltk_grc_doc.tokens_stops_filtered[:10]}")

# cltk_grc_doc.pos[:3]
# print(f"cltk_grc_doc.pos[:3]: {cltk_grc_doc.pos[:3]}")

# cltk_grc_doc.morphosyntactic_features[:3]
# print(f"cltk_grc_doc.morphosyntactic_features[:3]: {cltk_grc_doc.morphosyntactic_features[:3]}")

# cltk_grc_doc[0].gender
# print(f"cltk_grc_doc[0].gender: {cltk_grc_doc[0].gender}")


# cltk_grc_doc.lemmata[:5]
# print(f"cltk_grc_doc.lemmata[:5]: {cltk_grc_doc.lemmata[:5]}")

# no_sentences = len(cltk_grc_doc.sentences)
# print(f"How many sentences?: {no_sentences}")

# #no_sentences2 = len(cltk_grc_doc.sentences[0])
# print(f"len(cltk_grc_doc.sentences[0]): {len(cltk_grc_doc.sentences[0])}")

# #no_sentences3 = len(cltk_grc_doc.sentences[0][2])
# print(f"len(cltk_grc_doc.sentences[0][2]): {len(cltk_grc_doc.sentences[0][2])}")

# is_numpy_arry = isinstance(cltk_grc_doc.embeddings[1], np.ndarray)
# print(f"is_numpy_arry: {is_numpy_arry}")
