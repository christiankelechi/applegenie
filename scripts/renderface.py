import bpy

# Create a new mesh
mesh = bpy.data.meshes.new("FaceMesh")

# Create the vertices
verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
mesh.from_pydata(verts, [], [])

# Create the edges
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 5), (2, 6), (3, 7)]
mesh.from_pydata(verts, edges, [])

# Update the mesh
mesh.update()

# Create a new object
obj = bpy.data.objects.new("FaceObject", mesh)

# Add the object to the scene
scene = bpy.context.scene
scene.objects.link(obj)

# Select the object
bpy.context.scene.objects.active = obj