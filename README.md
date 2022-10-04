# bezierspline
*A Python implementation of the relaxed cubic spline curve*

The **relaxed cubic spline curve** is best described in section 5 of the UCLA Math 149 Cubic Spline Curves document. This was created as part of the process of procedurally generating curves in a separate Unity project.

The reference document can be accessed [here](https://www.math.ucla.edu/~baker/149.1.02w/handouts/dd_splines.pdf).

## Features
- The script takes two or more user-defined 2D coordinates and interpolates intermediate points using the Bernstein polynomial form of cubic Bezier curves
- All curves are connected smoothly, through the matching of first (tangent) and second (curvature) derivatives
- The number of intermediate draw points can be manually set by the user

![bezierspline_demo](https://user-images.githubusercontent.com/18087232/193771521-f12f9a47-1bb2-4e25-b1d5-f00ab320a079.png)
