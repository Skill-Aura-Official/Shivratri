from sketchpy import canvas
from turtle import Screen
# -------- Function: Draw Sketch Using sketchpy --------
s=Screen()
s.bgcolor("Black")

ab=canvas.sketch_from_svg("Mahashivratri.svg",scale=45)
ab.draw()