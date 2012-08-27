from os import environ

class ReportEnviroments(object):

    def __init__(self):
        self.cluster_corpus_path = environ["HOME"]+'/nltkSegmenter/clusters'
        self.original_reports_corpus_path = environ["HOME"]+'/nltkSegmenter/reports/test/original_reports/'
        self.segmented_reports_corpus_path = environ["HOME"]+'/nltkSegmenter/reports/test/segmented_reports/'
        self.nltksegmenter_fold = environ["HOME"] + '/nltkSegmenter'
