from os import environ
from os.path import split, splitext
from time import strftime as date

from re import sub

from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import sent_tokenize
from nltk.tokenize import wordpunct_tokenize
from string import punctuation
from stopwords import STOPWORDS
from nltk.stem import RSLPStemmer
from nltk.corpus import MacMorphoCorpusReader
from enviroment_vars import ReportEnviroments
from commands import getstatusoutput


class ReportRequirementProcessor(object):

    def __init__(self):
        object.__init__(self)
        
    def tokenize_report_sents(self, report_of_the_time):
        re = ReportEnviroments()
        new_corpus_reports_fileids_list = PlaintextCorpusReader(re.original_reports_corpus_path, '.*')
        raw_text = new_corpus_reports_fileids_list.raw(report_of_the_time)
        sentencas_raw = sent_tokenize(raw_text)
        original_report_path = str(new_corpus_reports_fileids_list.abspath(report_of_the_time))
        return sentencas_raw, original_report_path, report_of_the_time
        
    def convert_fileid_name(self, original_report_path):
        original_report_fileid = split(original_report_path)[1]
        fileid_name_component = splitext(original_report_fileid)[0]
        formatted_original_report_fileid = original_report_fileid + '%s'
        converted_fileid = sub(r'.*(%s)', fileid_name_component + r'\1.txt', 
                                          formatted_original_report_fileid) %'_seg'
        return converted_fileid    
        
    def tokenize_words_sents(self, sentencas_raw):
        uni_decoded_list = []
        for sentenca in sentencas_raw:
            uni_decoded_list.append(wordpunct_tokenize(sentenca.decode('utf-8')))
        punct_list = list(punctuation) + ['),', ').', '%),', '%).', '):', '()', '://', '>.', '.;', '...', '/>.']
        uni_encoded_list = []
        for i in range(len(uni_decoded_list)):
            uni_encoded_list.append([])
        for c1 in range(len(uni_decoded_list)):
            for c2 in range(len(uni_decoded_list[c1])):
                uni_encoded_list[c1].append(uni_decoded_list[c1][c2].encode('utf-8'))
        encoded_text_no_punct_list = []
        for i in range(len(uni_encoded_list)):
            encoded_text_no_punct_list.append([w.lower() for w in uni_encoded_list[i] 
                                              if w.lower() not in punct_list])
        return encoded_text_no_punct_list
        
    def extract_stopwords(self, STOPWORDS, encoded_text_no_punct_list): 
        uni_decoded_stopwords_list = wordpunct_tokenize(STOPWORDS.decode('utf-8'))
        encoded_stopwords_list = []
        for uni_stpw in uni_decoded_stopwords_list:
            encoded_stopwords_list.append(uni_stpw.encode('utf-8'))
        encoded_text_alpha_no_punct_stopword_list = []
        for i in range(len(encoded_text_no_punct_list)):
            encoded_text_alpha_no_punct_stopword_list.append([w for w in encoded_text_no_punct_list[i] 
                                                                if w not in encoded_stopwords_list])
        return encoded_text_alpha_no_punct_stopword_list
        
    def stem_report_sents(self, encoded_text_alpha_no_punct_stopword_list):
        decoded_stemmed_list = []
        encoded_stemmed_list = []
        for i in range(len(encoded_text_alpha_no_punct_stopword_list)):
            decoded_stemmed_list.append([])
            encoded_stemmed_list.append([])
        stemmer = RSLPStemmer()
        for c1 in range(len(encoded_text_alpha_no_punct_stopword_list)):
            for c2 in range(len(encoded_text_alpha_no_punct_stopword_list[c1])):
                decoded_stemmed_list[c1].append(stemmer.stem(encoded_text_alpha_no_punct_stopword_list[c1][c2].decode('utf-8')))
        for c1 in range(len(decoded_stemmed_list)):
            for c2 in range(len(decoded_stemmed_list[c1])):
                encoded_stemmed_list[c1].append(decoded_stemmed_list[c1][c2].encode('utf-8'))
        return encoded_stemmed_list
        
    def tag_stemmed_sents(self, encoded_stemmed_cluster, encoded_stemmed_list):
        tagged_stemmed_sents = []
        for i in range(len(encoded_stemmed_cluster)):      
            for j in range(len(encoded_stemmed_cluster[i])):
                for x in range(len(encoded_stemmed_list)):
                    if encoded_stemmed_cluster[i][j] in encoded_stemmed_list[x]:
                        tagged_stemmed_sents.append(tuple([encoded_stemmed_list[x], 
                                                           encoded_stemmed_cluster[i][0]]))
        return tagged_stemmed_sents
        
    def aggregate_uncategorized_stemmed_sents(self, tagged_stemmed_sents, encoded_stemmed_list):
        uncategorized_sents = []
        categorized_stemmed_sents_list = []
        for i in range(len(tagged_stemmed_sents)):
            categorized_stemmed_sents_list.append(tagged_stemmed_sents[i][0])
        len_cat = len(categorized_stemmed_sents_list)
        uncategorized_sents = [sent for sent in encoded_stemmed_list 
                                    if sent not in categorized_stemmed_sents_list]    
        len_uncat = len(uncategorized_sents)
        percent_cat = '%.2f' %(len_cat/float(len_cat + len_uncat))
        tagged_uncategorized_sents = []
        for i in range(len(uncategorized_sents)):
            tagged_uncategorized_sents.append(tuple([uncategorized_sents[i], 'uncategorized']))
        tagged_stemmed_sents.extend(tagged_uncategorized_sents)
        aggregated_tagged_stemmed_sents = tagged_stemmed_sents
        return aggregated_tagged_stemmed_sents, percent_cat
        
    def tag_original_sents(self, aggregated_tagged_stemmed_sents, 
                                 encoded_stemmed_list, 
                                 report_of_the_time):
        re = ReportEnviroments()
        indexed_tagged_list = []
        for i in range(len(aggregated_tagged_stemmed_sents)):
            indexed_tagged_list.append(tuple([encoded_stemmed_list.index(aggregated_tagged_stemmed_sents[i][0]), 
                                               aggregated_tagged_stemmed_sents[i][1]]))
        reader = MacMorphoCorpusReader(re.original_reports_corpus_path, report_of_the_time)
        indexed_tagged_sents = []
        for i in range(len(aggregated_tagged_stemmed_sents)):
            indexed_tagged_sents.append(tuple([reader.sents()[0][indexed_tagged_list[i][0]],
                                                indexed_tagged_list[i][1], 
                                                indexed_tagged_list[i][0]]))
        sorted_tagged_sents_by_index = sorted(indexed_tagged_sents, key=lambda indexed: indexed[2])
        return sorted_tagged_sents_by_index
        
    def group_tagged_original_sents_by_tag(self, encoded_stemmed_cluster, 
                                                 sorted_tagged_sents_by_index):
        stemmed_topic_titles = []
        for i in range(len(encoded_stemmed_cluster)):
            stemmed_topic_titles.append(encoded_stemmed_cluster[i][0])
        stemmed_topic_titles.append('uncategorized')
        tagged_clusters = []
        for i in range(len(stemmed_topic_titles)):
            tagged_clusters.append(tuple([[pos[0] for pos in sorted_tagged_sents_by_index 
                                            if pos[1]==stemmed_topic_titles[i]], 
                                            stemmed_topic_titles[i]]))
        return tagged_clusters
    
    def segment_original_report(self, tagged_clusters, 
                                       uni_encoded_cluster_tokenized_list, 
                                       original_report_path, percent_cat, 
                                       converted_fileid):
        re = ReportEnviroments()
        sent_by_topic = []
        for i in range(len(tagged_clusters)):
            sent_by_topic.append([sent for sent in tagged_clusters[i][0]])
        topic_titles = []
        for i in range(len(uni_encoded_cluster_tokenized_list)):
            topic_titles.append(uni_encoded_cluster_tokenized_list[i][0])
        topic_titles.append('uncategorized')
        with open(re.segmented_reports_corpus_path+converted_fileid, 'w') as f:
            timestamp = 'relatorio segmentado de ' + original_report_path \
                                                   + '\nconvertido em ' \
                                                   + date("%H:%M:%S %d/%m/%Y") \
                                                   + '\n%cat=' + percent_cat 
            f.write(timestamp)
            for i in range(len(sent_by_topic)):
                topic_title = '\n\n' + topic_titles[i].upper() + '\n\n'
                f.write(topic_title)
                for j in range(len(sent_by_topic[i])):
                    f.write(sent_by_topic[i][j] + '\n')
        f.close()
            
                        
