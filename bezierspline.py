# This script is a demo of multiple Bezier curves which pass through user-defined checkpoints
# All curves connected smoothly through the matching of their first and second derivatives at endpoints
# This code is best understood when accompanied by the very useful notes on Cubic Splines from UCLA Math 149

import matplotlib.pyplot as plt
import numpy as np

# S does not contain all control points required for drawing the curves
# These are CHECKPOINTS which the curve must pass - additional control points need to be generated
S = np.array([  # Should be len > 1
    [200, 400],
    [300, 1000],
    [500, 700],
    [800, 850],
    [1600, 100],
    [1900, 1000]
    ])

# Number of intermediate draw points between each checkpoint
iterations = 50

# Interpolate using the Bernstein polynomial form
# Each control point is a 2D vector
def bernstein(control_points, t):
    t3, t2 = t ** 3, t ** 2
    p0, p1, p2, p3 = (control_points[0], control_points[1],
                        control_points[2], control_points[3])

    return p0 * (-t3 + 3 * t2 - 3 * t + 1) + p1 * (3 * t3 - 6 * t2 + 3
            * t) + p2 * (-3 * t3 + 3 * t2) + p3 * t3


Sx = np.array([point[0] for point in S])
Sy = np.array([point[1] for point in S])

# There are n + 1 points
n = len(S) - 1

# Generate coefficient matrix M
M = np.empty((n - 1, n - 1))

for i in range(1, n):
    row = np.zeros(n - 1)

    if i - 2 >= 0:
        row[i - 2] = 1
    row[i - 1] = 4
    if i <= n - 2:
        row[i] = 1

    M[i - 1] = row

# Generate constant matrix C needed for solving the system of equations later
# Two (n-1) row x 1 col matrices for each Sx and Sy values
Cx = np.empty((n - 1, 1))
Cy = np.empty((n - 1, 1))

for i in range(1, n):
    cx = 6 * Sx[i]
    cy = 6 * Sy[i]
    if i == 1:
        cx -= Sx[0]
        cy -= Sy[0]
    if i == n - 1:
        cx -= Sx[n]
        cy -= Sy[n]

    Cx[i - 1] = cx
    Cy[i - 1] = cy

# Generate solution matrix/array B, the collection of points needed to calculate all control points
Bx = np.linalg.solve(M, Cx)
By = np.linalg.solve(M, Cy)
B_between = np.array([np.concatenate((Bx[i], By[i])) for i in range(n - 1)])

B = np.empty((n + 1, 2))

# B in its current state do not contain first and last points (= first and last points of S)
for i in range(n - 1):
    B[i + 1] = B_between[i]

B[0] = S[0]
B[n] = S[n]

x, y = [], []

# Draw Bezier curves using each checkpoint in S and two intermediate points between each B point
for i in range(n):
    # First control point
    p0 = S[i]

    # Calculate two intermediate points between two neighbouring B points
    p1 = 2 / 3 * B[i] + 1 / 3 * B[i + 1]
    p2 = 1 / 3 * B[i] + 2 / 3 * B[i + 1]

    # Last control point
    p3 = S[i + 1]

    # Add screen coords for drawing
    for iter in range(iterations):
        bezier = bernstein(np.array([p0, p1, p2, p3]), iter
                           / iterations)
        x.append(bezier[0])
        y.append(bezier[1])

plt.plot(x, y, 'bo')

# Draw the actual checkpoints in red
x2, y2 = [], []

for s in S:
    x2.append(s[0])
    y2.append(s[1])

plt.plot(x2, y2, 'rs')

# Plot settings
plt.xlim([0, 2000])
plt.ylim([0, 1200])
plt.show()
