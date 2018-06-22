from mcpi.minecraft import Minecraft
from mcpi import block	  

#mc = Minecraft.create("10.183.0.13", 4711)
mc = Minecraft.create("10.183.13.13", 4711)
while True:             
	P = mc.player.getPos()
	print(P)
