# MILLI-Hamilton

- <b>M</b>arkus' and
- <b>I</b>rena's
- <b>L</b>emmings
- <b>L</b>evel
- <b>I</b>nstantiator
- for <b>Hamilton</b>ian cycles

# Introduction

Generalized Lemmings is NP-hard, as shown by Cormode  in [1]. Note, that his claim that Lemmings is also NP-complete was challenged by Forišek in [2], who shows how to build levels with exponentially long solutions in polynomial space. Later, Viglietta actually showed that Lemmings is PSPACE-complete [3]. 

In any case, it is possible to reduce any problem in NP to generalized lemmings. We picked the directed Hamiltonian cycle problem, i.e. given a directed graph we can construct Lemmings levels that are solvable iff the graph has a directed Hamiltonian cycle. Since the original Lemmings is proprietary software and has severe restrictions on the level size, we actually use the free and open source clone Pingus [4] to demonstrate our reduction. This repository contains the script that generates Pingus levels from directed graphs. Pingus is not an exact clone, but we do not use any features it introduces over Lemmings.

The reduction basically looks like this (for the complete graph with 3 vertices):

![Reduction](../master/level3.png?raw=true)

# Requirements

 - Python 2.7
 - Pingus, tested with version 0.7.6 [4]

# Usage

The program takes a graph as argument and outputs a Pingus level to a file, as well as printing an ASCII representation of the level to stdout. 
```
python millihamilton.py [<graph>|<filename>]
```
The graph may be one of 4 things:
 - "C n", where "n" is any integer > 0: This will result in the cycle graph with "n" vertices
 - "K n", where "n" is any integer > 0: This will result in the complete graph with "n" vertices
 - "R n", where "n" is any integer > 0: This will result in a random graph (edges inserted with 0.5 probability). Note that this graphs are not always connected (in fact, the probability of them being connected tends to 0 as "n" tends to infinity)
 - An adjacency matrix: Rows are separated by semicolons, entries within the rows by blanks, e.g. "0 1 1; 1 0 1; 1 1 0" is the complete graph on 3 vertices
 
If a file name is used instead of a graph, the file must contain a graph in one of these 4 formats (blank lines and lines starting with # are ignored). The level is then written to a file that is named n_<hash>.pingus, where "n" is the number of vertices and "hash" is the md5 hash of a string representation of the adjacency matrix. The script will tell you the name of the file.


# References

[1] Cormode, Graham. "The hardness of the Lemmings game, or Oh no, more NP-completeness proofs." Proceedings of FUN. Vol. 4. 2004.

[2] Forišek, Michal. "Computational complexity of two-dimensional platform games." Fun with Algorithms. Springer Berlin Heidelberg, 2010.

[3] Viglietta, Giovanni. "Lemmings is PSPACE-complete." Fun with Algorithms. Springer International Publishing, 2014.

[4] http://pingus.seul.org/
