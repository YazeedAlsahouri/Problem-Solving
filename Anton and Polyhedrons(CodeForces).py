n=int(input())
polyhedrons={
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20
    }
count_faces=0
for i in range(n):
    figure=input()
    count_faces+=polyhedrons[figure]
print(count_faces)