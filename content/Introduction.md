---
abstract: |
    In this demo, we demonstrate how Jupyter Book can be used to create and publish a content rich paper that includes 
    interactive elements such as code cells, visualizations, and multimedia. We will walk through the process of setting 
    up a Jupyter Book, adding content, and deploying the final product online.
---

# Introduction

Analytical and semi-analytical methods for buckling and post-buckling analysis.

In aerospace engineering, maximizing structural efficiency while minimizing
weight is paramount. This has led to the use of thin-walled, lightweight
structures that are susceptible to buckling. While historically buckling was
seen as failure, modern engineering recognizes the postbuckling reserve of
stiffened panels. These panels can withstand loads significantly exceeding
their initial buckling threshold by allowing local buckling of the skin while stiffeners maintain global integrity.

This is a Jupyter Book built using the MyST engine [@Jupyter2025], which allows to export content in multiple output formats including HTML, PDF and docx.

The full documentation for this project is available online at:
[https://saullocastro.github.io/buckling/](https://saullocastro.github.io/buckling/)


## Background
Some background information about Jupyter Book and its features, like exporting to multiple formats as indicated in {numref}`fig-diagram`.

```{figure} ../figures/diagram.*
:label: fig-diagram
:alt: Some figure

Some figure
```


+++{"no-pdf":true}
```{figure} ../figures/delft.*
:label: fig-delft
:alt: picture of the TUD

A figure that is in the website but not in the PDF version.
```
+++
