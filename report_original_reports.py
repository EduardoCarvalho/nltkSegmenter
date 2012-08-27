from os import environ

from nltk.corpus import PlaintextCorpusReader
from enviroment_vars import ReportEnviroments


class ReportRequirement(object):

    @property
    def report_original_reports(self):
        re = ReportEnviroments()
        new_corpus_reports_fileids_list = PlaintextCorpusReader(re.original_reports_corpus_path, '.*')
        original_reports_list = new_corpus_reports_fileids_list.fileids()
        return original_reports_list


