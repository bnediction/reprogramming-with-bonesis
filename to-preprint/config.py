c = get_config()

c.NbConvertApp.notebooks = ['paper.ipynb']
c.NbConvertApp.export_format = 'latex'

c.Exporter.template_file = 'preprint.tplx'
c.Exporter.filters = {
    "md_maketitle_latex_metadata": "filters.latex_metadata",
    "md_maketitle_abstract": "filters.abstract",
    "md_maketitle_keywords": "filters.keywords",
    "citation2latex": "citation.citation2latex",
    "makesupp": "filters.sup2latex",
    "my_patch": "filters.my_patch",
}
