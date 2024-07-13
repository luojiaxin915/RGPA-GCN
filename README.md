# RGPA-GCN: Graph Neural Networks for Rice Gene-Phenotype Association Prediction
Identifying the gene-phenotype associations (GPAs) can better improve the yield and quality of rice. However, experimentally finding the GPAs is expensive and time-consuming. The computational screening of accurate gene-phenotype associations has become a necessary tool to assist biological experiments. The GPA prediction is treated as a node classification task in this study. To solve this problem, we propose the RGPA-GCN, a new computational method based on graph convolutional networks. The topology graph is constructed in the RGPA-GCN, utilizing the k-nearest neighbor method for information aggregation. The nodes of the graph are made up of gene functional similarity and phenotype semantic similarity. We predicted not only unknown GPAs but also unknown genes and unknown phenotypes under the balanced dataset. Via 5-fold cross-validation, the RGPA-GCN method shows satisfactory performance, which outperforms six classical machine learning methods, the traditional GCN algorithm, and three state-of-the-art models. Moreover, the case studies of the five phenotypes also performed well.
## File explanation
### 0_data folder
* The 2_Construct GPP graph.ipynb processes the generated data
### gene_peco_data folder
* The 3_data preprocessing to model.ipynb processes part of the generated data, is the data needed for the experiment of five neighbors in the Tp.
### data folder
* all_gpe_pairs: relationship pairs of genes and phenotypes
* phenotype_name: the phenotype id and name
* gene_name_def: the gene id and name
* peco_def: the phenotype id and name
* GPmat: the Matrix of relationships between genes and phenotypes, used in compared method DMA
* known_associations: positive samples (i.e. GPA)
### code folder
* 1_Similarity matrix calculation.ipynb, 2_Construct GPP graph.ipynb and 3_data preprocessing to model.ipynb are the first three codes that need to implement before training the model.
* parameters.yml is the RGPA-GCN parameters configuration file.
* compared methods: The implementation of DNN, GBDT, GNB, LR, MLP, SGD, and GAMEDA It is worth noting that the DNN is implemented through Keras.
### graphsaint folder: It contains the Pytorch code for RGPA-GCN.
### Case study folder
* *.ipynb: Do the case study
# Run the RGPA-GCN
1. pip install -r RGPA-GCN_requirements.txt
2. 1_Similarity matrix calculation.ipynb
3. 2_Construct GPP graph.ipynb
4. 3_data preprocessing to model.ipynb
5. Train and test, for example, python -m graphsaint.pytorch_version.train_saveys -data_prefix gene_peco_data/task_Tp__testlabel0_5knn_edge_fold0  --train_config code/parameters.yml
# Citation
Jiaxin Luo, Yujia Gao, Xiaosong Wang, Qian Zhou, and Zhenyu Yue*,RGPA-GCN: Graph Neural Networks for Rice Gene-Phenotype Association Prediction, 2023, Submitted.
# Contact
Please feel free to contact us if you need any help: zhenyuyue@ahau.edu.cn
