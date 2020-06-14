from vpython import *

class planets(object):
	"""docstring for planets"""
	def new(self, canv, sun_distance, radius, rotation_axis, orbitaltime, texture, trail=True, sun_distance_scale=0.0000002, radius_scale=0.0001):
		self.canv = canv
		self.sun_distance = sun_distance
		self.radius = radius
		self.texture = texture
		self.trail = trail
		self.sun_distance_scale = sun_distance_scale
		self.radius_scale = radius_scale

		return sphere(canvas=self.canv, pos=vector(self.sun_distance*self.sun_distance_scale,0,0), radius=self.radius*self.radius_scale, texture=self.texture, make_trail=self.trail)
