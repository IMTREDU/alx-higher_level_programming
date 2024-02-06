#!/usr/bin/python3
"""
Module to generate Pascal's triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle of n

    Args:
        n (int)

    Returns:
        list
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
