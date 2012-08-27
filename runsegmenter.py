from os import environ

from extractCluster import ClusterRequirementProcessor
from report_original_reports import ReportRequirement
from reportSegmenter import ReportRequirementProcessor
from stopwords import STOPWORDS


class runSegmenter(object):

    def extract_cluster_and_list_original_reports(self):
        crp = ClusterRequirementProcessor()
        raw_text_list = crp.extract_related_terms
        uni_encoded_cluster_tokenized_list = \
            crp.tokenize_related_terms(raw_text_list)
        encoded_stemmed_cluster = \
            crp.stem_related_terms(uni_encoded_cluster_tokenized_list)      
        rr = ReportRequirement()
        original_reports_list = rr.report_original_reports
        return original_reports_list, \
               encoded_stemmed_cluster, \
               uni_encoded_cluster_tokenized_list
    
    def indicates_report_of_the_time(self, original_reports_list, \
                                           encoded_stemmed_cluster, \
                                           uni_encoded_cluster_tokenized_list):    
        for i in range(len(original_reports_list)):
            report_of_the_time = original_reports_list[i]
            rrp = ReportRequirementProcessor()
            sentencas_raw, \
            original_report_path, \
            report_of_the_time = rrp.tokenize_report_sents(report_of_the_time)
            converted_fileid = rrp.convert_fileid_name(original_report_path)
            encoded_text_no_punct_list = rrp.tokenize_words_sents(sentencas_raw)
            encoded_text_alpha_no_punct_stopword_list = \
                rrp.extract_stopwords(STOPWORDS, 
                                      encoded_text_no_punct_list)
            encoded_stemmed_list = \
                rrp.stem_report_sents(encoded_text_alpha_no_punct_stopword_list)
            tagged_stemmed_sents = rrp.tag_stemmed_sents(encoded_stemmed_cluster, 
                                                         encoded_stemmed_list)
            aggregated_tagged_stemmed_sents, \
            percent_cat = \
            rrp.aggregate_uncategorized_stemmed_sents(tagged_stemmed_sents, 
                                                      encoded_stemmed_list)
            sorted_tagged_sents_by_index = \
                rrp.tag_original_sents(aggregated_tagged_stemmed_sents, 
                                       encoded_stemmed_list, 
                                       report_of_the_time)
            tagged_clusters = \
                rrp.group_tagged_original_sents_by_tag(encoded_stemmed_cluster, 
                                                       sorted_tagged_sents_by_index)
            rrp.segment_original_report(tagged_clusters, 
                                        uni_encoded_cluster_tokenized_list, 
                                        original_report_path, 
                                        percent_cat, 
                                        converted_fileid)
            
    def segment_report(self):
        rs = runSegmenter()
        original_reports_list, \
        encoded_stemmed_cluster, \
        uni_encoded_cluster_tokenized_list = \
            rs.extract_cluster_and_list_original_reports()
        rs.indicates_report_of_the_time(original_reports_list, \
                                        encoded_stemmed_cluster, \
                                        uni_encoded_cluster_tokenized_list)
 
                
