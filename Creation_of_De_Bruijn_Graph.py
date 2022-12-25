import random
import toyplot
def get_kmer_count_from_sequence(sequence, k=3, cyclic=True):
    # dict to store kmers
    kmers = {}
    # count how many times each occurred in this sequence (treated as cyclic)
    for i in range(0, len(sequence)):
        kmer = sequence[i:i + k]
        # for cyclic sequence get kmers that wrap from end to beginning
        length = len(kmer)
        if cyclic:
            if len(kmer) != k:
                kmer += sequence[:(k - length)]
        # if not cyclic then skip kmers at end of sequence
        else:
            if len(kmer) != k:
                continue
        # count occurrence of this kmer in sequence
        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1
    return kmers
    def get_debruijn_edges_from_kmers(kmers):
    # store edges as tuples in a set
    edges = set()
    # compare each (k-1)mer
    for k1 in kmers:
        for k2 in kmers:
            if k1 != k2:            
                # if they overlap then add to edges
                if k1[1:] == k2[:-1]:
                    edges.add((k1[:-1], k2[:-1]))
                if k1[:-1] == k2[1:]:
                    edges.add((k2[:-1], k1[:-1]))
    return edges
    def plot_debruijn_graph(edges, width=500, height=500):
    "returns a toyplot graph from an input of edges"
    graph = toyplot.graph(
        [i[0] for i in edges],
        [i[1] for i in edges],
        width=width,
        height=height,
        tmarker=">", 
        vsize=25,
        vstyle={"stroke": "black", "stroke-width": 2, "fill": "none"},
        vlstyle={"font-size": "11px"},
        estyle={"stroke": "black", "stroke-width": 2},
        layout=toyplot.layout.FruchtermanReingold(edges=toyplot.layout.CurvedEdges()))
    return graph
    
