from polls.factex.const import PER, LOC, ORG

from polls.factex.segment import Segmenter
from polls.factex.morph.vocab import MorphVocab

from polls.factex.emb import NewsEmbedding
from polls.factex.morph.tagger import NewsMorphTagger
from polls.factex.syntax import NewsSyntaxParser
from polls.factex.ner import NewsNERTagger

from polls.factex.extractors import NamesExtractor
from polls.factex.extractors import DatesExtractor
from polls.factex.extractors import MoneyExtractor
from polls.factex.extractors import AddrExtractor
fro
from polls.factex.doc import Doc
from models import BiLSTM_CRF

def Analyze(text, nerneed=False, morphneed=False, index=0):
        res = ""
        segmenter = Segmenter()
        morph_vocab = MorphVocab()

        emb = NewsEmbedding()
        morph_tagger = NewsMorphTagger(emb)
        syntax_parser = NewsSyntaxParser(emb)
        ner_tagger = NewsNERTagger(emb)

        names_extractor = NamesExtractor(morph_vocab)
        dates_extractor = DatesExtractor(morph_vocab)
        money_extractor = MoneyExtractor(morph_vocab)
        addr_extractor = AddrExtractor(morph_vocab)

        # преобразуем текст в объект
        doc = Doc(text)
        # делим на слова
        doc.segment(segmenter)
        # выделяем морфемы
        doc.tag_morph(morph_tagger)
        doc.parse_syntax(syntax_parser)
        # выделяем именованные сущности
        doc.tag_ner(ner_tagger)
        ##если необходимо отображение распознанных сущностей, добавляем его к результату
        if nerneed:
            res += doc.ner.getresult()
        ##если необходим морфологический анализ, добавляем его к результату
        sent = doc.sents[index]
        if morphneed:
            res += doc.morph.getresult()
        # строим синтаксическое дерево для выбранного предложения, добавляем его к результату
        res += sent.syntax.getresult()
        # получаем выборку найденных сущностей
        # model=BiLSTM_CRF()
        # model.train()
        # model.test(doc)
        #entities = doc.DocFact
        #return entities
