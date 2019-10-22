import pythreejs as three
import numpy as np
from .Colors import colors

class Drawable(object):
    
    def __init__(self, geometry, mesh_color = None):
        super(Drawable, self).__init__()
        self.geometry = geometry
        self.geometry_color = self.__initialize_geometry_color(mesh_color)
        self.drawable_mesh = self.__initialize_drawable_mesh()
        

    def __initialize_geometry_color(self, mesh_color):
        if mesh_color is None:
            return np.repeat(colors.teal,
                             self.geometry.num_faces,
                             axis=0)

    def __initialize_drawable_mesh(self):
        
        boundaries = self.geometry.boundary()[0]
        geometry_attributes = {
            'position': three.BufferAttribute(self.geometry.vertices[boundaries.flatten()], normalized=False),
            'color': three.BufferAttribute(self.geometry_color[np.repeat(self.geometry.boundary()[1], 3)], normalized=False),
            }
        drawable_geometry = three.BufferGeometry(attributes = geometry_attributes)
        drawable_geometry.exec_three_obj_method('computeVertexNormals')
        material = three.MeshLambertMaterial(
                                           polygonOffset=True,
                                           polygonOffsetFactor=1,
                                           polygonOffsetUnits=1,
                                           flatShading = True,
                                           color = "white",
                                           opacity = 1.,
                                           transparent = False,
                                           side = 'FrontSide',
                                           wireframe=False,
                                           vertexColors = 'FaceColors',
                                          )
        return three.Mesh(
            geometry=drawable_geometry,
            material=material,
            position=[0, 0, 0]
        )