import xml.etree.ElementTree as etree
import json

tree = etree.parse('Scene.dae')
root = tree.getroot()
renderablesRoot = root[6][0]

def toFloat(string): return float(string)

renderables = []
for renderable in renderablesRoot:
	renderableJson = {}
	# Name
	renderableJson['name'] = renderable.attrib['name']
	# Mesh
	renderableJson['mesh'] = renderable[5].attrib['url'].replace("#", "").replace("-mesh", "")
	# Geometry
	renderableJson['geometry'] = {}
	# Position
	renderableJson['geometry']['position'] = map(toFloat, renderable[0].text.split(" "))
	# Orientation
	renderableJson['geometry']['orientation'] = map(toFloat, [renderable[1].text.split(" ")[-1], renderable[2].text.split(" ")[-1], renderable[3].text.split(" ")[-1]])
	# Material
	renderableJson['material'] = renderable[5][0][0][0].attrib['symbol'].replace("#", "").replace("-material", "")
	renderables.append(renderableJson)


json = {}
json['renderables'] = renderables
print(json)