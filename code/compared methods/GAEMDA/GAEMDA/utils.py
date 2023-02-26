import numpy as np
import pandas as pd
import mxnet as mx
from mxnet import ndarray as nd
import dgl
import torch


def load_data(directory):
    GSSM = np.loadtxt(directory + '\GSSM.txt',dtype=np.float32)
    PESSM = np.loadtxt(directory + '\PSSM.txt',dtype=np.float32,delimiter='\t')

    IPE = pd.DataFrame(PESSM).reset_index()
    IG = pd.DataFrame(GSSM).reset_index()
    IPE.rename(columns = {'index':'id'}, inplace = True)
    IG.rename(columns = {'index':'id'}, inplace = True)
    IPE['id'] = IPE['id']
    IG['id'] = IG['id']
    
    return IPE, IG


def sample(directory, random_seed):
    all_associations = pd.read_csv(directory + '/all_gpe_pairs.csv')
    known_associations = all_associations.loc[all_associations['label'] == 1]
    unknown_associations = all_associations.loc[all_associations['label'] == 0]
    random_negative = unknown_associations.sample(n=known_associations.shape[0], random_state=random_seed, axis=0)

    sample_df = known_associations.append(random_negative)
    sample_df.reset_index(drop=True, inplace=True)

    return sample_df.values


def build_graph(directory, random_seed, ctx):
    # dgl.load_backend('mxnet')
    IPE, IG = load_data(directory)
    samples = sample(directory, random_seed)

    print('Building graph ...')
    g = dgl.DGLGraph(multigraph=True)
    g.add_nodes(IPE.shape[0] + IG.shape[0])
    node_type = np.zeros(g.number_of_nodes(), dtype='float32')
    node_type[:IPE.shape[0]] = 1
    g.ndata['type'] = node_type

    print('Adding peco features ...')
    pe_data = nd.zeros(shape=(g.number_of_nodes(), IPE.shape[1]), dtype='float32')
    print(pe_data)
    pe_data[: IPE.shape[0], :] = nd.from_numpy(IPE)
    print(pe_data)
    g.ndata['d_features'] = pe_data

    print('Adding gene features ...')
    ge_data = nd.zeros(shape=(g.number_of_nodes(), IG.shape[1]), dtype='float32')
    ge_data[IPE.shape[0]: IPE.shape[0]+IG.shape[0], :] = nd.from_numpy(IG)
    g.ndata['m_features'] = ge_data
    
    print('Adding edges ...')
    peco_ids = list(range(1, IPE.shape[0] + 1))
    gene_ids = list(range(1, IG.shape[0] + 1))

    peco_ids_invmap = {id_: i for i, id_ in enumerate(peco_ids)}
    gene_ids_invmap = {id_: i for i, id_ in enumerate(gene_ids)}

    sample_peco_vertices = [peco_ids_invmap[id_] for id_ in samples[:, 1]]
    sample_gene_vertices = [gene_ids_invmap[id_] + IPE.shape[0] for id_ in samples[:, 0]]

    g.add_edges(sample_peco_vertices, sample_gene_vertices,
                data={'inv': nd.zeros(samples.shape[0], dtype='int32', ctx=ctx),
                      'rating': nd.from_numpy(samples[:, 2].astype('float32')).copyto(ctx)})
    g.add_edges(sample_gene_vertices, sample_peco_vertices,
                data={'inv': nd.zeros(samples.shape[0], dtype='int32', ctx=ctx),
                      'rating': nd.from_numpy(samples[:, 2].astype('float32')).copyto(ctx)})
    g.readonly()
    print('Successfully build graph !!')

    return g, peco_ids_invmap, gene_ids_invmap