import xml.etree.ElementTree as etree
import json

tree = etree.parse('Scene.dae')
root = tree.getroot()
namespace = '{http://www.collada.org/2005/11/COLLADASchema}'

renderablesRoot = root.find(namespace + 'library_visual_scenes')[0]

def toFloat(string): return float(string)
def rotationNodeToOrientation(node): return toFloat(node.text.split(" ")[-1])

renderables = []
for renderable in renderablesRoot:
	renderableJson = {}
	# Name
	renderableJson['name'] = renderable.attrib['name']
	# Mesh
	renderableJson['mesh'] =  renderable.find(namespace + 'instance_geometry').attrib['url'].replace("#", "").replace("-mesh", "")
	# Geometry
	renderableJson['geometry'] = {}
	# # Position
	renderableJson['geometry']['position'] = map(toFloat, renderable.find(namespace + 'translate').text.split(" "))
	# # Orientation
	renderableJson['geometry']['orientation'] = map(rotationNodeToOrientation, renderable.findall(namespace + 'rotate'))
	# # Material
	renderableJson['material'] = renderable.find( './/' + namespace + 'instance_material' ).attrib['symbol'].replace("#", "").replace("-material", "")
	renderables.append(renderableJson)


json = {}
json['renderables'] = renderables
print(json)