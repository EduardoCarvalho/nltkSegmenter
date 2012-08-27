

class Variables(object):

    def __init__(self):
        self.raw_text_list = [['discente\naluno\n'], ['docente\ndoc\xc3\xaancia\n'], ['infraestrutura\nsala\nlaborat\xc3\xb3rio\nestrutura\ngin\xc3\xa1sio\npiscina\nvesti\xc3\xa1rio\nbanheiro\n\n']]
        self.uni_encoded_cluster_tokenized_list = [['discente', 'aluno'], ['docente', 'doc\xc3\xaancia'], ['infraestrutura', 'sala', 'laborat\xc3\xb3rio', 'estrutura', 'gin\xc3\xa1sio', 'piscina', 'vesti\xc3\xa1rio', 'banheiro']]
        self.encoded_stemmed_cluster = [['disc', 'alun'], ['docent', 'doc'], ['infraestrut', 'sal', 'laborat\xc3\xb3ri', 'estrut', 'gin\xc3\xa1si', 'piscin', 'vesti', 'banh']]
        
        self.report = 'relatorio_teste.txt'
        self.sentencas_raw = ['A infraestrutura est\xc3\xa1 \xc3\xb3tima.', 'O banheiro est\xc3\xa1 em condi\xc3\xa7\xc3\xb5es razo\xc3\xa1veis.', 'O quadro de docentes \xc3\xa9 formado exclusivamente por doutores.', 'Os discentes tem apresentado rendimento acima da m\xc3\xa9dia.', 'A an\xc3\xa1lise da (informa\xc3\xa7\xc3\xa3o), de que o \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'An\xc3\xa1lise do \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'O vesti\xc3\xa1rio est\xc3\xa1 em p\xc3\xa9ssimas condi\xc3\xa7\xc3\xb5es.', 'H\xc3\xa1 muitos azulejos quebrados na piscina.', 'Os docentes est\xc3\xa3o insatisfeitos com o sal\xc3\xa1rio.\n']
        self.original_report_path = '/home/eduardo/nltkSegmenter/reports/test/original_reports/relatorio_teste.txt'
        self.report_of_the_time = 'relatorio_teste.txt'
        self.converted_fileid = 'relatorio_teste_seg.txt'
        self.encoded_text_no_punct_list = [['a', 'infraestrutura', 'est\xc3\xa1', '\xc3\xb3tima'], ['o', 'banheiro', 'est\xc3\xa1', 'em', 'condi\xc3\xa7\xc3\xb5es', 'razo\xc3\xa1veis'], ['o', 'quadro', 'de', 'docentes', '\xc3\xa9', 'formado', 'exclusivamente', 'por', 'doutores'], ['os', 'discentes', 'tem', 'apresentado', 'rendimento', 'acima', 'da', 'm\xc3\xa9dia'], ['a', 'an\xc3\xa1lise', 'da', 'informa\xc3\xa7\xc3\xa3o', 'de', 'que', 'o', '\xc3\xa1tomo', 'do', 'cora\xc3\xa7\xc3\xa3o'], ['an\xc3\xa1lise', 'do', '\xc3\xa1tomo', 'do', 'cora\xc3\xa7\xc3\xa3o'], ['o', 'vesti\xc3\xa1rio', 'est\xc3\xa1', 'em', 'p\xc3\xa9ssimas', 'condi\xc3\xa7\xc3\xb5es'], ['h\xc3\xa1', 'muitos', 'azulejos', 'quebrados', 'na', 'piscina'], ['os', 'docentes', 'est\xc3\xa3o', 'insatisfeitos', 'com', 'o', 'sal\xc3\xa1rio']]
        self.encoded_text_alpha_no_punct_stopword_list = [['infraestrutura', '\xc3\xb3tima'], ['banheiro', 'condi\xc3\xa7\xc3\xb5es', 'razo\xc3\xa1veis'], ['quadro', 'docentes', 'formado', 'exclusivamente', 'doutores'], ['discentes', 'apresentado', 'rendimento', 'acima', 'm\xc3\xa9dia'], ['an\xc3\xa1lise', 'informa\xc3\xa7\xc3\xa3o', '\xc3\xa1tomo', 'cora\xc3\xa7\xc3\xa3o'], ['an\xc3\xa1lise', '\xc3\xa1tomo', 'cora\xc3\xa7\xc3\xa3o'], ['vesti\xc3\xa1rio', 'p\xc3\xa9ssimas', 'condi\xc3\xa7\xc3\xb5es'], ['muitos', 'azulejos', 'quebrados', 'piscina'], ['docentes', 'insatisfeitos', 'sal\xc3\xa1rio']]
        self.encoded_stemmed_list = [['infraestrut', '\xc3\xb3tim'], ['banh', 'cond', 'razo\xc3\xa1'], ['quadr', 'docent', 'form', 'exclusiv', 'dou'], ['disc', 'apresent', 'rend', 'acim', 'm\xc3\xa9d'], ['an\xc3\xa1lis', 'inform', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], ['an\xc3\xa1lis', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], ['vesti', 'p\xc3\xa9ss', 'cond'], ['muit', 'azulej', 'quebr', 'piscin'], ['docent', 'insatisfeit', 'sal\xc3\xa1ri']]
        self.tagged_stemmed_sents = [(['disc', 'apresent', 'rend', 'acim', 'm\xc3\xa9d'], 'disc'), (['quadr', 'docent', 'form', 'exclusiv', 'dou'], 'docent'), (['docent', 'insatisfeit', 'sal\xc3\xa1ri'], 'docent'), (['infraestrut', '\xc3\xb3tim'], 'infraestrut'), (['muit', 'azulej', 'quebr', 'piscin'], 'infraestrut'), (['vesti', 'p\xc3\xa9ss', 'cond'], 'infraestrut'), (['banh', 'cond', 'razo\xc3\xa1'], 'infraestrut')]
        self.aggregated_tagged_stemmed_sents = [(['disc', 'apresent', 'rend', 'acim', 'm\xc3\xa9d'], 'disc'), (['quadr', 'docent', 'form', 'exclusiv', 'dou'], 'docent'), (['docent', 'insatisfeit', 'sal\xc3\xa1ri'], 'docent'), (['infraestrut', '\xc3\xb3tim'], 'infraestrut'), (['muit', 'azulej', 'quebr', 'piscin'], 'infraestrut'), (['vesti', 'p\xc3\xa9ss', 'cond'], 'infraestrut'), (['banh', 'cond', 'razo\xc3\xa1'], 'infraestrut'), (['an\xc3\xa1lis', 'inform', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], 'uncategorized'), (['an\xc3\xa1lis', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], 'uncategorized')]
        self.percent_cat = '0.78'
        self.sorted_tagged_sents_by_index = [('A infraestrutura est\xc3\xa1 \xc3\xb3tima.', 'infraestrut', 0), ('O banheiro est\xc3\xa1 em condi\xc3\xa7\xc3\xb5es razo\xc3\xa1veis.', 'infraestrut', 1), ('O quadro de docentes \xc3\xa9 formado exclusivamente por doutores.', 'docent', 2), ('Os discentes tem apresentado rendimento acima da m\xc3\xa9dia.', 'disc', 3), ('A an\xc3\xa1lise da (informa\xc3\xa7\xc3\xa3o), de que o \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'uncategorized', 4), ('An\xc3\xa1lise do \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'uncategorized', 5), ('O vesti\xc3\xa1rio est\xc3\xa1 em p\xc3\xa9ssimas condi\xc3\xa7\xc3\xb5es.', 'infraestrut', 6), ('H\xc3\xa1 muitos azulejos quebrados na piscina.', 'infraestrut', 7), ('Os docentes est\xc3\xa3o insatisfeitos com o sal\xc3\xa1rio.', 'docent', 8)]
        self.tagged_clusters = [(['Os discentes tem apresentado rendimento acima da m\xc3\xa9dia.'], 'disc'), (['O quadro de docentes \xc3\xa9 formado exclusivamente por doutores.', 'Os docentes est\xc3\xa3o insatisfeitos com o sal\xc3\xa1rio.'], 'docent'), (['A infraestrutura est\xc3\xa1 \xc3\xb3tima.', 'O banheiro est\xc3\xa1 em condi\xc3\xa7\xc3\xb5es razo\xc3\xa1veis.', 'O vesti\xc3\xa1rio est\xc3\xa1 em p\xc3\xa9ssimas condi\xc3\xa7\xc3\xb5es.', 'H\xc3\xa1 muitos azulejos quebrados na piscina.'], 'infraestrut'), (['A an\xc3\xa1lise da (informa\xc3\xa7\xc3\xa3o), de que o \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'An\xc3\xa1lise do \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.'], 'uncategorized')]
        
        self.report1 = 'relatorio_teste1.txt'
        self.sentencas_raw1 = ['A infraestrutura est\xc3\xa1 \xc3\xb3tima.', 'O banheiro n\xc3\xa3o tem chuveiro.', 'Fiquei bolado agora.', 'O quadro de docentes \xc3\xa9 formado exclusivamente por doutores.', 'Os discentes tem apresentado rendimento acima da m\xc3\xa9dia.', 'A an\xc3\xa1lise da (informa\xc3\xa7\xc3\xa3o), de que o \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'An\xc3\xa1lise do \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'O vesti\xc3\xa1rio est\xc3\xa1 em p\xc3\xa9ssimas condi\xc3\xa7\xc3\xb5es.', 'H\xc3\xa1 muitos azulejos quebrados na piscina.', 'Os docentes est\xc3\xa3o insatisfeitos com o sal\xc3\xa1rio.\n']
        self.original_report_path1 = '/home/eduardo/nltkSegmenter/reports/test/original_reports/relatorio_teste1.txt'
        self.report_of_the_time1 = 'relatorio_teste1.txt'
        self.converted_fileid1 = 'relatorio_teste1_seg.txt'
        self.encoded_text_no_punct_list1 = [['a', 'infraestrutura', 'est\xc3\xa1', '\xc3\xb3tima'], ['o', 'banheiro', 'n\xc3\xa3o', 'tem', 'chuveiro'], ['fiquei', 'bolado', 'agora'], ['o', 'quadro', 'de', 'docentes', '\xc3\xa9', 'formado', 'exclusivamente', 'por', 'doutores'], ['os', 'discentes', 'tem', 'apresentado', 'rendimento', 'acima', 'da', 'm\xc3\xa9dia'], ['a', 'an\xc3\xa1lise', 'da', 'informa\xc3\xa7\xc3\xa3o', 'de', 'que', 'o', '\xc3\xa1tomo', 'do', 'cora\xc3\xa7\xc3\xa3o'], ['an\xc3\xa1lise', 'do', '\xc3\xa1tomo', 'do', 'cora\xc3\xa7\xc3\xa3o'], ['o', 'vesti\xc3\xa1rio', 'est\xc3\xa1', 'em', 'p\xc3\xa9ssimas', 'condi\xc3\xa7\xc3\xb5es'], ['h\xc3\xa1', 'muitos', 'azulejos', 'quebrados', 'na', 'piscina'], ['os', 'docentes', 'est\xc3\xa3o', 'insatisfeitos', 'com', 'o', 'sal\xc3\xa1rio']]
        self.encoded_text_alpha_no_punct_stopword_list1 = [['infraestrutura', '\xc3\xb3tima'], ['banheiro', 'chuveiro'], ['fiquei', 'bolado', 'agora'], ['quadro', 'docentes', 'formado', 'exclusivamente', 'doutores'], ['discentes', 'apresentado', 'rendimento', 'acima', 'm\xc3\xa9dia'], ['an\xc3\xa1lise', 'informa\xc3\xa7\xc3\xa3o', '\xc3\xa1tomo', 'cora\xc3\xa7\xc3\xa3o'], ['an\xc3\xa1lise', '\xc3\xa1tomo', 'cora\xc3\xa7\xc3\xa3o'], ['vesti\xc3\xa1rio', 'p\xc3\xa9ssimas', 'condi\xc3\xa7\xc3\xb5es'], ['muitos', 'azulejos', 'quebrados', 'piscina'], ['docentes', 'insatisfeitos', 'sal\xc3\xa1rio']]
        self.encoded_stemmed_list1 = [['infraestrut', '\xc3\xb3tim'], ['banh', 'chuv'], ['fiq', 'bol', 'agor'], ['quadr', 'docent', 'form', 'exclusiv', 'dou'], ['disc', 'apresent', 'rend', 'acim', 'm\xc3\xa9d'], ['an\xc3\xa1lis', 'inform', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], ['an\xc3\xa1lis', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], ['vesti', 'p\xc3\xa9ss', 'cond'], ['muit', 'azulej', 'quebr', 'piscin'], ['docent', 'insatisfeit', 'sal\xc3\xa1ri']]
        self.tagged_stemmed_sents1 = [(['disc', 'apresent', 'rend', 'acim', 'm\xc3\xa9d'], 'disc'), (['quadr', 'docent', 'form', 'exclusiv', 'dou'], 'docent'), (['docent', 'insatisfeit', 'sal\xc3\xa1ri'], 'docent'), (['infraestrut', '\xc3\xb3tim'], 'infraestrut'), (['muit', 'azulej', 'quebr', 'piscin'], 'infraestrut'), (['vesti', 'p\xc3\xa9ss', 'cond'], 'infraestrut'), (['banh', 'chuv'], 'infraestrut')]
        self.aggregated_tagged_stemmed_sents1 = [(['disc', 'apresent', 'rend', 'acim', 'm\xc3\xa9d'], 'disc'), (['quadr', 'docent', 'form', 'exclusiv', 'dou'], 'docent'), (['docent', 'insatisfeit', 'sal\xc3\xa1ri'], 'docent'), (['infraestrut', '\xc3\xb3tim'], 'infraestrut'), (['muit', 'azulej', 'quebr', 'piscin'], 'infraestrut'), (['vesti', 'p\xc3\xa9ss', 'cond'], 'infraestrut'), (['banh', 'chuv'], 'infraestrut'), (['fiq', 'bol', 'agor'], 'uncategorized'), (['an\xc3\xa1lis', 'inform', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], 'uncategorized'), (['an\xc3\xa1lis', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], 'uncategorized')]
        self.percent_cat1 = '0.70'
        self.sorted_tagged_sents_by_index1 = [('A infraestrutura est\xc3\xa1 \xc3\xb3tima.', 'infraestrut', 0), ('O banheiro n\xc3\xa3o tem chuveiro.', 'infraestrut', 1), ('Fiquei bolado agora.', 'uncategorized', 2), ('O quadro de docentes \xc3\xa9 formado exclusivamente por doutores.', 'docent', 3), ('Os discentes tem apresentado rendimento acima da m\xc3\xa9dia.', 'disc', 4), ('A an\xc3\xa1lise da (informa\xc3\xa7\xc3\xa3o), de que o \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'uncategorized', 5), ('An\xc3\xa1lise do \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'uncategorized', 6), ('O vesti\xc3\xa1rio est\xc3\xa1 em p\xc3\xa9ssimas condi\xc3\xa7\xc3\xb5es.', 'infraestrut', 7), ('H\xc3\xa1 muitos azulejos quebrados na piscina.', 'infraestrut', 8), ('Os docentes est\xc3\xa3o insatisfeitos com o sal\xc3\xa1rio.', 'docent', 9)]
        self.tagged_clusters1 = [(['Os discentes tem apresentado rendimento acima da m\xc3\xa9dia.'], 'disc'), (['O quadro de docentes \xc3\xa9 formado exclusivamente por doutores.', 'Os docentes est\xc3\xa3o insatisfeitos com o sal\xc3\xa1rio.'], 'docent'), (['A infraestrutura est\xc3\xa1 \xc3\xb3tima.', 'O banheiro n\xc3\xa3o tem chuveiro.', 'O vesti\xc3\xa1rio est\xc3\xa1 em p\xc3\xa9ssimas condi\xc3\xa7\xc3\xb5es.', 'H\xc3\xa1 muitos azulejos quebrados na piscina.'], 'infraestrut'), (['Fiquei bolado agora.', 'A an\xc3\xa1lise da (informa\xc3\xa7\xc3\xa3o), de que o \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'An\xc3\xa1lise do \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.'], 'uncategorized')]
        
        self.report2 = 'relatorio_teste2.txt'
        self.sentencas_raw2 = ['A infraestrutura est\xc3\xa1 \xc3\xb3tima.', 'O quadro de docentes \xc3\xa9 formado exclusivamente por doutores.', 'Os discentes tem apresentado rendimento acima da m\xc3\xa9dia.', 'A an\xc3\xa1lise da (informa\xc3\xa7\xc3\xa3o), de que o \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'An\xc3\xa1lise do \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'O vesti\xc3\xa1rio est\xc3\xa1 em p\xc3\xa9ssimas condi\xc3\xa7\xc3\xb5es.', 'H\xc3\xa1 muitos azulejos quebrados na piscina.', 'Os docentes est\xc3\xa3o insatisfeitos com o sal\xc3\xa1rio.', 'A estrutura \xc3\xa9 satisfat\xc3\xb3ria.', 'O manguito rotador est\xc3\xa1 lesionado.', 'N\xc3\xa3o h\xc3\xa1 nenhuma rela\xc3\xa7\xc3\xa3o com o escopo nesta senten\xc3\xa7a.\n']
        self.original_report_path2 = '/home/eduardo/nltkSegmenter/reports/test/original_reports/relatorio_teste2.txt'
        self.report_of_the_time2 = 'relatorio_teste2.txt'
        self.converted_fileid2 = 'relatorio_teste2_seg.txt'
        self.encoded_text_no_punct_list2 = [['a', 'infraestrutura', 'est\xc3\xa1', '\xc3\xb3tima'], ['o', 'quadro', 'de', 'docentes', '\xc3\xa9', 'formado', 'exclusivamente', 'por', 'doutores'], ['os', 'discentes', 'tem', 'apresentado', 'rendimento', 'acima', 'da', 'm\xc3\xa9dia'], ['a', 'an\xc3\xa1lise', 'da', 'informa\xc3\xa7\xc3\xa3o', 'de', 'que', 'o', '\xc3\xa1tomo', 'do', 'cora\xc3\xa7\xc3\xa3o'], ['an\xc3\xa1lise', 'do', '\xc3\xa1tomo', 'do', 'cora\xc3\xa7\xc3\xa3o'], ['o', 'vesti\xc3\xa1rio', 'est\xc3\xa1', 'em', 'p\xc3\xa9ssimas', 'condi\xc3\xa7\xc3\xb5es'], ['h\xc3\xa1', 'muitos', 'azulejos', 'quebrados', 'na', 'piscina'], ['os', 'docentes', 'est\xc3\xa3o', 'insatisfeitos', 'com', 'o', 'sal\xc3\xa1rio'], ['a', 'estrutura', '\xc3\xa9', 'satisfat\xc3\xb3ria'], ['o', 'manguito', 'rotador', 'est\xc3\xa1', 'lesionado'], ['n\xc3\xa3o', 'h\xc3\xa1', 'nenhuma', 'rela\xc3\xa7\xc3\xa3o', 'com', 'o', 'escopo', 'nesta', 'senten\xc3\xa7a']]
        self.encoded_text_alpha_no_punct_stopword_list2 = [['infraestrutura', '\xc3\xb3tima'], ['quadro', 'docentes', 'formado', 'exclusivamente', 'doutores'], ['discentes', 'apresentado', 'rendimento', 'acima', 'm\xc3\xa9dia'], ['an\xc3\xa1lise', 'informa\xc3\xa7\xc3\xa3o', '\xc3\xa1tomo', 'cora\xc3\xa7\xc3\xa3o'], ['an\xc3\xa1lise', '\xc3\xa1tomo', 'cora\xc3\xa7\xc3\xa3o'], ['vesti\xc3\xa1rio', 'p\xc3\xa9ssimas', 'condi\xc3\xa7\xc3\xb5es'], ['muitos', 'azulejos', 'quebrados', 'piscina'], ['docentes', 'insatisfeitos', 'sal\xc3\xa1rio'], ['estrutura', 'satisfat\xc3\xb3ria'], ['manguito', 'rotador', 'lesionado'], ['nenhuma', 'rela\xc3\xa7\xc3\xa3o', 'escopo', 'nesta', 'senten\xc3\xa7a']]
        self.encoded_stemmed_list2 = [['infraestrut', '\xc3\xb3tim'], ['quadr', 'docent', 'form', 'exclusiv', 'dou'], ['disc', 'apresent', 'rend', 'acim', 'm\xc3\xa9d'], ['an\xc3\xa1lis', 'inform', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], ['an\xc3\xa1lis', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], ['vesti', 'p\xc3\xa9ss', 'cond'], ['muit', 'azulej', 'quebr', 'piscin'], ['docent', 'insatisfeit', 'sal\xc3\xa1ri'], ['estrut', 'satisfat\xc3\xb3r'], ['manguit', 'rot', 'lesion'], ['nenhum', 'rela\xc3\xa7', 'escop', 'nest', 'senten\xc3\xa7']]
        self.tagged_stemmed_sents2 = [(['disc', 'apresent', 'rend', 'acim', 'm\xc3\xa9d'], 'disc'), (['quadr', 'docent', 'form', 'exclusiv', 'dou'], 'docent'), (['docent', 'insatisfeit', 'sal\xc3\xa1ri'], 'docent'), (['infraestrut', '\xc3\xb3tim'], 'infraestrut'), (['estrut', 'satisfat\xc3\xb3r'], 'infraestrut'), (['muit', 'azulej', 'quebr', 'piscin'], 'infraestrut'), (['vesti', 'p\xc3\xa9ss', 'cond'], 'infraestrut')]
        self.aggregated_tagged_stemmed_sents2 = [(['disc', 'apresent', 'rend', 'acim', 'm\xc3\xa9d'], 'disc'), (['quadr', 'docent', 'form', 'exclusiv', 'dou'], 'docent'), (['docent', 'insatisfeit', 'sal\xc3\xa1ri'], 'docent'), (['infraestrut', '\xc3\xb3tim'], 'infraestrut'), (['estrut', 'satisfat\xc3\xb3r'], 'infraestrut'), (['muit', 'azulej', 'quebr', 'piscin'], 'infraestrut'), (['vesti', 'p\xc3\xa9ss', 'cond'], 'infraestrut'), (['an\xc3\xa1lis', 'inform', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], 'uncategorized'), (['an\xc3\xa1lis', '\xc3\xa1tom', 'cora\xc3\xa7\xc3\xa3'], 'uncategorized'), (['manguit', 'rot', 'lesion'], 'uncategorized'), (['nenhum', 'rela\xc3\xa7', 'escop', 'nest', 'senten\xc3\xa7'], 'uncategorized')]
        self.percent_cat2 = '0.64'
        self.sorted_tagged_sents_by_index2 = [('A infraestrutura est\xc3\xa1 \xc3\xb3tima.', 'infraestrut', 0), ('O quadro de docentes \xc3\xa9 formado exclusivamente por doutores.', 'docent', 1), ('Os discentes tem apresentado rendimento acima da m\xc3\xa9dia.', 'disc', 2), ('A an\xc3\xa1lise da (informa\xc3\xa7\xc3\xa3o), de que o \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'uncategorized', 3), ('An\xc3\xa1lise do \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'uncategorized', 4), ('O vesti\xc3\xa1rio est\xc3\xa1 em p\xc3\xa9ssimas condi\xc3\xa7\xc3\xb5es.', 'infraestrut', 5), ('H\xc3\xa1 muitos azulejos quebrados na piscina.', 'infraestrut', 6), ('Os docentes est\xc3\xa3o insatisfeitos com o sal\xc3\xa1rio.', 'docent', 7), ('A estrutura \xc3\xa9 satisfat\xc3\xb3ria.', 'infraestrut', 8), ('O manguito rotador est\xc3\xa1 lesionado.', 'uncategorized', 9), ('N\xc3\xa3o h\xc3\xa1 nenhuma rela\xc3\xa7\xc3\xa3o com o escopo nesta senten\xc3\xa7a.', 'uncategorized', 10)]
        self.tagged_clusters2 = [(['Os discentes tem apresentado rendimento acima da m\xc3\xa9dia.'], 'disc'), (['O quadro de docentes \xc3\xa9 formado exclusivamente por doutores.', 'Os docentes est\xc3\xa3o insatisfeitos com o sal\xc3\xa1rio.'], 'docent'), (['A infraestrutura est\xc3\xa1 \xc3\xb3tima.', 'O vesti\xc3\xa1rio est\xc3\xa1 em p\xc3\xa9ssimas condi\xc3\xa7\xc3\xb5es.', 'H\xc3\xa1 muitos azulejos quebrados na piscina.', 'A estrutura \xc3\xa9 satisfat\xc3\xb3ria.'], 'infraestrut'), (['A an\xc3\xa1lise da (informa\xc3\xa7\xc3\xa3o), de que o \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'An\xc3\xa1lise do \xc3\xa1tomo do cora\xc3\xa7\xc3\xa3o.', 'O manguito rotador est\xc3\xa1 lesionado.', 'N\xc3\xa3o h\xc3\xa1 nenhuma rela\xc3\xa7\xc3\xa3o com o escopo nesta senten\xc3\xa7a.'], 'uncategorized')]
        
