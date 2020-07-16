# counting phylogenetic ancestors.
# unrooted binary tree: is defined as :all internal nodes have degree 3.
# rooted binary tree: only the root has the degree 2, 
                    # all other internal nodes have degree 3.

# the number of leaves is n:
n = 4
print "the number of internal nodes is:", n-2
print "the total number of the tree nodes is:", 2*n-2
print "the edges of the tree is:", n-1
