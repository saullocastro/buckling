# Linear buckling of shells with general boundary conditions

## Linear buckling of cylindrical shells under compression and torsion

Under pure compression, the shell buckles into an axisymmetric or diamond-shaped pattern (Yoshimura pattern), whereas under pure torsion, the shell deforms into a diagonal-shaped pattern with spiral wrinkles. Castro et al. [@Castro2014] and Lu et al. [@Lu2025ShellPostBuckling] explores how these modes interact under combined loads, such as compression with pre-torsion or torsion with pre-compression. The interaction of axial and torsional loads creates a rich variety of behaviors:


```{table} Post-Buckling Characteristics for Various Loading Conditions
:label: tab:buckling_patterns

| Loading Type | Post-Buckling Pattern | Stability/Behavior |
| :--- | :--- | :--- |
| **Pure Compression** | Diamond-shaped | Highly unstable; snapping occurs with decreasing $N$. |
| **Pure Torsion** | Diagonal-shaped | Smooth path; load carrying capacity usually decreases. |
| **Torsion + Pre-tension** | Diagonal-shaped | Pre-tension increases the critical load and stabilizes the path. |
| **Torsion + Pre-compression** | Twisted Diamond | Large pre-compression triggers snapping and complex pattern transitions. |
```

The next sections will discuss different implementations of this shell buckling problem.
 
