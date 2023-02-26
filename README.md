# RGPA-GCN: Graph Neural Networks for Rice Gene-Phenotype Association Prediction
Identifying the gene-phenotype associations (GPAs) can better improve the yield and quality of rice. However, experimentally finding the GPAs is expensive and time-consuming. The computational screening of accurate gene-phenotype associations has become a necessary tool to assist biological experiments. The GPA prediction is treated as a node classification task in this study. To solve this problem, we propose the RGPA-GCN, a new computational method based on graph convolutional networks. The topology graph is constructed in the RGPA-GCN, utilizing the k-nearest neighbor method for information aggregation. The nodes of the graph are made up of gene functional similarity and phenotype semantic similarity. We predicted not only unknown GPAs but also unknown gene and unknown phenotype under the balanced dataset. Via 5-fold cross validation, the RGPA-GCN method shows satisfactory performance, which outperforms six classical machine learning methods, the traditional GCN algorithm and three state-of-the-art models. Moreover, the case studies of the five phenotypes also performed well.
## File explanation
### data folder
* P_SSM: phenotype semantic similarity
* G_FSM: gene functional similarity
* all_gene_phenotype_pairs: positive samples (i.e. GPA)
* phenotype_name: The phenotype id and name
* gene_name: The gene id and name
### code folder
* 1_Construct GPP graph.ipynb and 2_data preprocessing to model.ipynb are the first two code need to implement before train model.
