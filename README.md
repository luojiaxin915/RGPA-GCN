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
* parameters.yml is the GNN parameters configuration file.
#### compared methods folder
The implementation of DNN, GBDT, GNB, LR, MLP, SGD, GAMEDA It is worthy to note that the DNN is implemented through Keras.
### case study folder
* *.ipynb: Do the case study
### graphsaint folder
It contains the pytorch code for RGPA-GCN.
# Run the MDA-GKNN
1. pip install -r RGPA-GCN_requirements.txt
2. 1_Construct GPP graph.ipynb
3. 2_data preprocessing to model.ipynb
4. Train and test, for example: python -m graphsaint.pytorch_version.train_saveys --data_prefix gene_peco_data/task_Tpe__testlabel0_1knn_edge_fold0  --train_config code/parameters.yml > 20221020_Tpe_1knn_lr0.01_weight10_fold0.out
