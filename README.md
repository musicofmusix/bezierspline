# bezierspline
*A Python implementation of a relaxed cubic spline curve*

The **relaxed cubic spline curve** implemented here is best described in section 5 of the UCLA Math 149 Cubic Spline Curves document. This was created as part of the process of procedurally generating curves in another Unity project.

The document can be accessed [here](https://www.math.ucla.edu/~baker/149.1.02w/handouts/dd_splines.pdf).

## Features
- The script takes two or more user-defined 2D coordinates and interpolates intermediate points using the Bernstein polynomial form of cubic Bezier curves.
- All curves are connected smoothly, through the matching of first (tangent) and second (curvature) derivatives
- The number of intermediate draw points can be manually set by the user
