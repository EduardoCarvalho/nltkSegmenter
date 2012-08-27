from unittest import TestCase
from should_dsl import should
from stopwords import STOPWORDS

from reportSegmenter import ReportRequirementProcessor
from extractCluster import ClusterRequirementProcessor
from report_original_reports import ReportRequirement
from specvar import Variables


class TestClusterRequirementProcessor(TestCase):

    def setUp(self):
        self.v = Variables()
        self.crp = ClusterRequirementProcessor()
        
    def it_extracts_raw_list_from_cluster_of_related_terms(self):
        self.crp.extract_related_terms |should| equal_to(self.v.raw_text_list)
        
    def it_tokenizes_extracted_raw_list(self):
        self.crp.tokenize_related_terms(self.v.raw_text_list) \
        |should| equal_to(self.v.uni_encoded_cluster_tokenized_list)
        
    def it_converts_tokens_in_a_list_of_stems(self):
        self.crp.stem_related_terms(self.v.uni_encoded_cluster_tokenized_list) \
        |should| equal_to(self.v.encoded_stemmed_cluster)
        
    
class TestReportRequirementProcessor(TestCase):

    def setUp(self):
        self.v = Variables()
        self.rrp = ReportRequirementProcessor()
        
    def it_tokenizes_report_sents_from_report(self):
        self.rrp.tokenize_report_sents(self.v.report) \
        |should| equal_to((self.v.sentencas_raw, self.v.original_report_path, self.v.report_of_the_time))
        
    def it_converts_fileid_name_from_original_report_to_segmented_report_format(self):
        self.rrp.convert_fileid_name(self.v.original_report_path) \
        |should| equal_to(self.v.converted_fileid)
    
    def it_tokenizes_sentencas_raw_extracting_punctuations(self):
        self.rrp.tokenize_words_sents(self.v.sentencas_raw) \
        |should| equal_to(self.v.encoded_text_no_punct_list)
        
    def it_extracts_stopwords_from_report(self):
        self.rrp.extract_stopwords(STOPWORDS, self.v.encoded_text_no_punct_list) \
        |should| equal_to(self.v.encoded_text_alpha_no_punct_stopword_list)
    
    def it_converts_tokens_of_report_in_a_list_of_encoded_stems(self):
        self.rrp.stem_report_sents(self.v.encoded_text_alpha_no_punct_stopword_list) \
        |should| equal_to(self.v.encoded_stemmed_list)
        
    def it_categorizes_stemmed_sents_by_tags_based_on_cluster_of_related_terms(self):
        self.rrp.tag_stemmed_sents(self.v.encoded_stemmed_cluster, self.v.encoded_stemmed_list) \
        |should| equal_to(self.v.tagged_stemmed_sents)
        
    def it_aggregates_uncategorized_stemmed_sents_on_categorized_stemmed_sents(self):
        self.rrp.aggregate_uncategorized_stemmed_sents(self.v.tagged_stemmed_sents, self.v.encoded_stemmed_list) \
        |should| equal_to((self.v.aggregated_tagged_stemmed_sents, self.v.percent_cat))
        
    def it_sorts_aggregated_tagged_stemmed_sents_by_index(self):
        self.rrp.tag_original_sents(self.v.aggregated_tagged_stemmed_sents, self.v.encoded_stemmed_list, self.v.report_of_the_time) \
        |should| equal_to(self.v.sorted_tagged_sents_by_index)
        
    def it_groups_tagged_original_sents_by_tag(self):
        self.rrp.group_tagged_original_sents_by_tag(self.v.encoded_stemmed_cluster, self.v.sorted_tagged_sents_by_index) \
        |should| equal_to(self.v.tagged_clusters)
  
    def it_tokenizes_report_sents_from_report_1(self):
        self.rrp.tokenize_report_sents(self.v.report1) \
        |should| equal_to((self.v.sentencas_raw1, self.v.original_report_path1, self.v.report_of_the_time1))
        
    def it_converts_fileid_name_1_from_original_report_to_segmented_report_format(self):
        self.rrp.convert_fileid_name(self.v.original_report_path1) \
        |should| equal_to(self.v.converted_fileid1)
    
    def it_tokenizes_sentencas_raw_1_extracting_punctuations(self):
        self.rrp.tokenize_words_sents(self.v.sentencas_raw1) \
        |should| equal_to(self.v.encoded_text_no_punct_list1)
        
    def it_extracts_stopwords_from_report_1(self):
        self.rrp.extract_stopwords(STOPWORDS, self.v.encoded_text_no_punct_list1) \
        |should| equal_to(self.v.encoded_text_alpha_no_punct_stopword_list1)
    
    def it_converts_tokens_of_report_1_in_a_list_of_encoded_stems(self):
        self.rrp.stem_report_sents(self.v.encoded_text_alpha_no_punct_stopword_list1) \
        |should| equal_to(self.v.encoded_stemmed_list1)
        
    def it_categorizes_stemmed_sents_1_by_tags_based_on_cluster_of_related_terms(self):
        self.rrp.tag_stemmed_sents(self.v.encoded_stemmed_cluster, self.v.encoded_stemmed_list1) \
        |should| equal_to(self.v.tagged_stemmed_sents1)
        
    def it_aggregates_uncategorized_stemmed_sents_on_categorized_stemmed_sents_1(self):
        self.rrp.aggregate_uncategorized_stemmed_sents(self.v.tagged_stemmed_sents1, self.v.encoded_stemmed_list1) \
        |should| equal_to((self.v.aggregated_tagged_stemmed_sents1, self.v.percent_cat1))
        
    def it_sorts_aggregated_tagged_stemmed_sents_1_by_index(self):
        self.rrp.tag_original_sents(self.v.aggregated_tagged_stemmed_sents1, self.v.encoded_stemmed_list1, self.v.report_of_the_time1) \
        |should| equal_to(self.v.sorted_tagged_sents_by_index1)
        
    def it_groups_tagged_original_sents_1_by_tag(self):
        self.rrp.group_tagged_original_sents_by_tag(self.v.encoded_stemmed_cluster, self.v.sorted_tagged_sents_by_index1) \
        |should| equal_to(self.v.tagged_clusters1)
        
    def it_tokenizes_report_sents_from_report_2(self):
        self.rrp.tokenize_report_sents(self.v.report2) \
        |should| equal_to((self.v.sentencas_raw2, self.v.original_report_path2, self.v.report_of_the_time2))
        
    def it_converts_fileid_name_2_from_original_report_to_segmented_report_format(self):
        self.rrp.convert_fileid_name(self.v.original_report_path2) \
        |should| equal_to(self.v.converted_fileid2)
    
    def it_tokenizes_sentencas_raw_2_extracting_punctuations(self):
        self.rrp.tokenize_words_sents(self.v.sentencas_raw2) \
        |should| equal_to(self.v.encoded_text_no_punct_list2)
        
    def it_extracts_stopwords_from_report_2(self):
        self.rrp.extract_stopwords(STOPWORDS, self.v.encoded_text_no_punct_list2) \
        |should| equal_to(self.v.encoded_text_alpha_no_punct_stopword_list2)
    
    def it_converts_tokens_of_report_2_in_a_list_of_encoded_stems(self):
        self.rrp.stem_report_sents(self.v.encoded_text_alpha_no_punct_stopword_list2) \
        |should| equal_to(self.v.encoded_stemmed_list2)
        
    def it_categorizes_stemmed_sents_2_by_tags_based_on_cluster_of_related_terms(self):
        self.rrp.tag_stemmed_sents(self.v.encoded_stemmed_cluster, self.v.encoded_stemmed_list2) \
        |should| equal_to(self.v.tagged_stemmed_sents2)
        
    def it_aggregates_uncategorized_stemmed_sents_on_categorized_stemmed_sents_2(self):
        self.rrp.aggregate_uncategorized_stemmed_sents(self.v.tagged_stemmed_sents2, self.v.encoded_stemmed_list2) \
        |should| equal_to((self.v.aggregated_tagged_stemmed_sents2, self.v.percent_cat2))
        
    def it_sorts_aggregated_tagged_stemmed_sents_2_by_index(self):
        self.rrp.tag_original_sents(self.v.aggregated_tagged_stemmed_sents2, self.v.encoded_stemmed_list2, self.v.report_of_the_time2) \
        |should| equal_to(self.v.sorted_tagged_sents_by_index2)
        
    def it_groups_tagged_original_sents_2_by_tag(self):
        self.rrp.group_tagged_original_sents_by_tag(self.v.encoded_stemmed_cluster, self.v.sorted_tagged_sents_by_index2) \
        |should| equal_to(self.v.tagged_clusters2)
        
              
