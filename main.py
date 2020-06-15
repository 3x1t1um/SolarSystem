from vpython import *
import platform
import json
import src.informations as infos
import src.planets as planets
import os
import time

class SolarSystem(object):
	"""docstring for SolarSystem"""
	def __init__(self):
		self.mercury_data = json.loads(infos.mercury)
		self.venus_data = json.loads(infos.venus)
		self.earth_data = json.loads(infos.earth)
		self.mars_data = json.loads(infos.mars)
		self.jupiter_data = json.loads(infos.jupiter)
		self.saturn_data = json.loads(infos.saturn)
		self.uranus_data = json.loads(infos.uranus)
		self.neptune_data = json.loads(infos.neptune)

		self.banner()
		self.run()

	def banner(self):
		if 'Windows' in platform.platform():
			os.system('cls')
		else:
			os.system('clear')

		print()
		print("""                     .::.
                  .:'  .:
        ,0000000.:'   .:'
       00000000000  .:'
      0000000000000:'
      0000000000000		   SOLAR SYSTEM
    .:0000000000000				
  .:'  00000000000		      	   by AskaD
.:'   .:'0000000'
:'  .:'
'::' 								""")
		print()

	def run(self):
		self.createscene()
		self.createsun()

		self.mercury = planets.planets().new(scene, self.mercury_data["distance"], self.mercury_data["radius"], self.mercury_data["texture"])
		self.venus = planets.planets().new(scene, self.venus_data["distance"], self.venus_data["radius"], self.venus_data["texture"])
		self.earth = planets.planets().new(scene, self.earth_data["distance"], self.earth_data["radius"], self.earth_data["texture"])
		self.mars = planets.planets().new(scene, self.mars_data["distance"], self.mars_data["radius"], self.mars_data["texture"])
		self.jupiter = planets.planets().new(scene, self.jupiter_data["distance"], self.jupiter_data["radius"], self.jupiter_data["texture"])
		self.saturn = planets.planets().new(scene, self.saturn_data["distance"], self.saturn_data["radius"], self.saturn_data["texture"])
		self.uranus = planets.planets().new(scene, self.uranus_data["distance"], self.uranus_data["radius"], self.uranus_data["texture"])
		self.neptune = planets.planets().new(scene, self.neptune_data["distance"], self.neptune_data["radius"], self.neptune_data["texture"])

		self.scene.camera.follow(self.sun)
		time.sleep(5)
		self.rotation()

	def rotation(self):
		while (True):
			self.mercury.rotate(angle=(2*pi/(self.mercury_data["speed"] * 86400)* 3600 / 300), axis=vector(0, 1, 0), origin=self.sun.pos)
			self.venus.rotate(angle=(2*pi/(self.venus_data["speed"] * 86400)* 3600 / 300), axis=vector(0, 1, 0), origin=self.sun.pos)
			self.earth.rotate(angle=(2*pi/(self.earth_data["speed"] * 86400)* 3600/ 300), axis=vector(0, 1, 0), origin=self.sun.pos)
			self.mars.rotate(angle=(2*pi/(self.mars_data["speed"] * 86400)* 3600/ 300), axis=vector(0, 1, 0), origin=self.sun.pos)
			self.jupiter.rotate(angle=(2*pi/(self.jupiter_data["speed"] * 86400)* 3600/ 300), axis=vector(0, 1, 0), origin=self.sun.pos)
			self.saturn.rotate(angle=(2*pi/(self.saturn_data["speed"] * 86400)* 3600/ 300), axis=vector(0, 1, 0), origin=self.sun.pos)
			self.uranus.rotate(angle=(2*pi/(self.uranus_data["speed"] * 86400)* 3600/ 300), axis=vector(0, 1, 0), origin=self.sun.pos)
			self.neptune.rotate(angle=(2*pi/(self.neptune_data["speed"] * 86400)* 3600/ 300), axis=vector(0, 1, 0), origin=self.sun.pos)

			# to be reviewed at the next update
			
			self.mercury.rotate(angle = radians(57/self.mercury_data["speed"]/300), axis = vector(0, 1, 0))
			self.venus.rotate(angle = radians(243/self.venus_data["speed"]/300), axis = vector(0, 1, 0))
			self.earth.rotate(angle=radians(self.earth_data["speed"]/self.earth_data["speed"]/300), axis=vector(0, 1, 0))
			self.mars.rotate(angle=radians(self.mars_data["speed"]/self.mars_data["speed"]/300), axis=vector(0, 1, 0))
			self.jupiter.rotate(angle=radians(self.jupiter_data["speed"]/self.jupiter_data["speed"]/300), axis=vector(0, 1, 0))
			self.saturn.rotate(angle=radians(self.saturn_data["speed"]/self.saturn_data["speed"]/300), axis=vector(0, 1, 0))
			self.uranus.rotate(angle=radians(self.uranus_data["speed"]/self.uranus_data["speed"]/300), axis=vector(0, 1, 0))
			self.neptune.rotate(angle=radians(self.neptune_data["speed"]/self.neptune_data["speed"]/300), axis=vector(0, 1, 0))

			# the satellites will arrive later
 
	def createscene(self):
		# to be reviewed at the next update
		
		self.scene = scene
		self.scene.autoscale = False
		self.scene.lights = []

	def createsun(self):
		self.sun = sphere(canvas=scene, pos=vector(0,0,0), radius=696340*1e-05, texture="./img/sun.jpg", mass=2e30, emissive=True, opacity=1)
		self.sunlight = local_light(pos=self.sun.pos, color=color.white)

SolarSystem()
