# Installation
To install on Linux type into the commandline:
    
    pip install TCRnumba

It requires CUDA and is not yet tested for MacOS or Windows.

# Usage
In Python you can import

    import TCRnumba

Then, test the script, by running the additional commands  

    import TCRnumba.graph_numba as gn
    import TCRnumba.convert_pure as cp
    adjacency_sparse = gn.adjacency_matrix(['ABC', 'DEF', 'EFG', 'ABC', 'ABD', 'EEE', 'EEF', 'EFF', 'GGE', 'GAS'], N_part=2, len_xy=5, direct_output=True)
    cp.convert_pure(adjacency_sparse, 2, 5)

# Use SONIA to create files
    sonia-generate --humanTRB -n 1000000 --pre -o pre_example.txt



