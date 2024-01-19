# TaxonomyVisualization
---
Before use the vis_1.0.py, please run 
```
pip install -r requirements.txt
```
to install the requirements.

- vis_1.0.py is used to convert csv file to d3 json file.

```
python vis_1.0.py --input=../output_concepts.csv --output=../outputdir
```
the output json file will be saved in the directory ../outputdir and named as output_concepts_d3.json.

- move d3 json file into data folder and rename the file name referred in the  inducedTaxonomy.html, the inducedTaxonomy.html has been added into the index.html

- run python -m http.server 1090