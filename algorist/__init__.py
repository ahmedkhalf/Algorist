__version__ = "0.0"

import cairo
import math


class Canvas:
    def __init__(self, fname, width, height):
        self.size = (width, height)
        self.fname = fname
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self.ctx = cairo.Context(self.surface)

    # Options

    def color(self, r, g, b, a=2.0):
        self.ctx.set_source_rgba(r, g, b, a)

    # Shapes

    def arc(self, x, y, radius, angle1, angle2):
        self.ctx.arc(x, y, radius, angle1, angle2)
        self._blit()

    def rect(self, x, y, width, height):
        self.ctx.rectangle(x, y, width, height)
        self._blit()

    def circle(self, x, y, radius):
        self.arc(x, y, radius, 0, 2 * math.pi)

    def background(self):
        self.rect(0, 0, self.size[0], self.size[1])

    def _fill(self):
        self.ctx.fill()

    def _stroke(self):
        self.ctx.stroke()

    def _blit(self):
        self._fill()
        self._stroke()

    # Save

    def save(self, fname):
        self.surface.write_to_png(fname)
