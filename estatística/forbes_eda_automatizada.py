# EDA AUTOMATIZADA

#1. Pandas profiling -> Chamado atualmente de ydataprofiling
#2. Sweetviz
from pydataset import data

import sweetviz as sv

forbes = data('Forbes2000')
my_report = sv.analyze(forbes)

my_report.show_notebook()