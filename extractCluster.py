from os import environ

from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import RSLPStemmer
from enviroment_vars import ReportEnviroments


class ClusterRequirementProcessor(object):

    def __init__(self):
        object.__init__(self)

    @property   
    def extract_related_terms(self):
        re = ReportEnviroments()
        new_corpus_clusters_fileids_list = PlaintextCorpusReader(re.cluster_corpus_path, '.*')
        raw_text_list = []
        for i in range(len(new_corpus_clusters_fileids_list.fileids())):
            raw_text_list.extend([[new_corpus_clusters_fileids_list.raw(fileids=new_corpus_clusters_fileids_list.fileids()[i])]])
        return raw_text_list
        
    def tokenize_related_terms(self, raw_text_list):
        uni_decoded_cluster_tokenized_list = []
        for c1 in range(len(raw_text_list)):
            for raw_cluster_token in raw_text_list[c1]:
                uni_decoded_cluster_tokenized_list.append(wordpunct_tokenize(raw_cluster_token.decode('utf-8')))
        uni_encoded_cluster_tokenized_list = []
        for i in range(len(uni_decoded_cluster_tokenized_list)):
            uni_encoded_cluster_tokenized_list.append([])
        for c1 in range(len(uni_decoded_cluster_tokenized_list)):
            for c2 in range(len(uni_decoded_cluster_tokenized_list[c1])):
                uni_encoded_cluster_tokenized_list[c1].append(uni_decoded_cluster_tokenized_list[c1][c2].encode('utf-8'))
        return uni_encoded_cluster_tokenized_list
        
    def stem_related_terms(self, uni_encoded_cluster_tokenized_list):
        stemmer = RSLPStemmer()
        decoded_stemmed_cluster = []
        encoded_stemmed_cluster = []
        for i in range(len(uni_encoded_cluster_tokenized_list)):
            decoded_stemmed_cluster.append([])
            encoded_stemmed_cluster.append([])
        for c1 in range(len(uni_encoded_cluster_tokenized_list)):
            for c2 in range(len(uni_encoded_cluster_tokenized_list[c1])):
                decoded_stemmed_cluster[c1].append(stemmer.stem(uni_encoded_cluster_tokenized_list[c1][c2].decode('utf-8')))
        for c1 in range(len(decoded_stemmed_cluster)):
            for c2 in range(len(decoded_stemmed_cluster[c1])):
                encoded_stemmed_cluster[c1].append(decoded_stemmed_cluster[c1][c2].encode('utf-8'))
        return encoded_stemmed_cluster
