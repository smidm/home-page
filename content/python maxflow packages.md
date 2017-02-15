Date: 2013-07-23
Title: Python Packages for Graph Cuts on Images
Tags: python
Summary: Review of python packages for performing graph cuts on images.

Graph for a small image of 512x512 pixels has 261144 nodes and 523264 edges in the [4-connected pixels](http://en.wikipedia.org/wiki/Pixel_connectivity) case. Graphs in this scale require a fast construction interface. I reviewed a few python packages mainly from this perspective. The comparison is by no means exhaustive and fair!

# Based on Kolmogorov min-cut / max-flow C++ library 
- original Kolmogorov's code: <http://vision.csd.uwo.ca/code/#Max-flow.2Fmin-cut>
- as of version 3.01 restricts usage only for research purposes
- version 2.21 can be [commercially licensed](http://www.e-lucid.com/i/software/optimisation_software/maxflow_computervision.html)

## PyMaxflow
- <https://github.com/pmneila/PyMaxflow>
- Cython based python interface
- well documented at <http://pmneila.github.io/PyMaxflow/>
- α-β-swap and α-expansion algorithms for multi-label optimization
- **shortcomings**:
    - missing batch addition of edges other than with constant weight
    
## pymaxflow    
- <https://github.com/Rhoana/pymaxflow>
- Cython based python interface
- supports batch addition of edges from numpy arrays
    - edges are added one by one on the cython part of the interface, but it seems to be fast enough
- **shortcomings**:
    - not documented (but the package is so simple that it is not a big deal)
    - no algorithms for multi-label segmentation

Example of batch node and edge addition:

    im = ...
    g = pymaxflow.PyGraph()   
    g.add_node(im.size)
    
    # linear indices of pixels arranged in image like matrix
    indices = np.arange(im.shape[0]*im.shape[1]).reshape(im.shape[0:2]).astype(np.int32)
    # compute differences between neighbouring pixels
    diffs = np.abs(im[:, 1:] - im[:, :-1]).ravel() + eps
    # indices of the neighbouring pixels
    e1 = indices[:, :-1].ravel()
    e2 = indices[:, 1:].ravel()
    g.add_edge_vectorized(e1, e2, diffs, diffs)
    
API:

    class PyGraph:
        __cinit__(self, int node_num_max, int edge_num_max)
        add_node(self, int num=1)
        add_edge(self, int i, int j, float cap, float rev_cap)
        add_tweights(self, int i, float cap_source, float cap_sink)
        maxflow(self)
        what_segment(self, int i)
        add_edge_vectorized(self,
                                np.ndarray[dtype=np.int32_t, ndim=1, negative_indices=False] i,
                                np.ndarray[dtype=np.int32_t, ndim=1, negative_indices=False] j,
                                np.ndarray[dtype=np.float32_t, ndim=1, negative_indices=False] cap,
                                np.ndarray[dtype=np.float32_t, ndim=1, negative_indices=False] rev_cap)
        add_tweights_vectorized(self,
                                np.ndarray[dtype=np.int32_t, ndim=1, negative_indices=False] i,
                                np.ndarray[dtype=np.float32_t, ndim=1, negative_indices=False] cap_source,
                                np.ndarray[dtype=np.float32_t, ndim=1, negative_indices=False] cap_sink)
        what_segment_vectorized(self)
        
## pygco
- based on Kolmogorov maxflow library and [gco library](http://vision.csd.uwo.ca/code/#Multi-label_optimization)
- source: <https://github.com/amueller/gco_python>
- introductory article written by the author: <http://peekaboo-vision.blogspot.cz/2012/05/graphcuts-for-python-pygco.html>
- cython based python interface
- well documented
- α-β-swap and α-expansion algorithms for multi-label segmentation
- supports only multi-label segmentation
- **shortcomings**:
    - no direct access to a low level functionality as the max-flow algorithm itself      

## pygraphcut
- <http://tfinley.net/software/pygraphcut/>
- Python C API based interface
- **shortcomings**:
    - not actively developed
    - no public repository
    - no batch addition of nodes and edges
    - Python C API is hard to maintain
- I have not tested this package.

# Packages Based on Other Max-flow Implementations

## graph-tool library
- <http://projects.skewed.de/graph-tool/>
- perfectly documented and feature rich general graph algorithms package
- based on [Boost Graph](http://www.boost.org/doc/libs/1_54_0/libs/graph/doc/) library
- GPL license
- various max-flow algorithms including Kolmogorov's
- **shortcomings**:
    - *no batch addition of nodes and edges* - this shortcoming should be fixed now, see comment (22.10.2014)

One by one addition of nodes and edges implemented in Python is extremely slow for graphs in a scale suitable for images. In my experience ~100x slower than the *pymaxflow* package due to the graph construction.

## MedPy
- <https://pypi.python.org/pypi/MedPy/0.1.0>
- 3d graphcuts on voxels
- I have not tested this package.

# Conclusions

I picked the [pymaxflow](https://github.com/Rhoana/pymaxflow) package for my purposes. It's just simple but quick wrapper for the Kolmogorov min-cut / max-flow C++ library. The wrapper fairly minimalistic and is written in [Cython](https://en.wikipedia.org/wiki/Cython) that makes the bindings easy to understand and modify.
