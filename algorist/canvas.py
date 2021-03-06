from algorist import color
import cairo
import math
import re


class Canvas:
    def __init__(self, width, height):
        self.size = (width, height)
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self.ctx = cairo.Context(self.surface)
        self.frame = 1  # Used by saveFrame
        self.fillColor = color.Color(255)
        self.strokeColor = color.Color(0)

    # Options

    def fill(self, *args):
        if len(args) == 1 and type(args[0]) == color.Color:
            self.fillColor = args[0]
        else:
            self.fillColor = color.Color(*args)

    def noFill(self):
        self.fillColor = None

    def stroke(self, *args):
        if len(args) == 1 and type(args[0]) == color.Color:
            self.strokeColor = args[0]
        else:
            self.strokeColor = color.Color(*args)

    def noStroke(self):
        self.strokeColor = None

    # Shapes

    def arc(self, x, y, radius, angle1, angle2):
        self.ctx.arc(x, y, radius, angle1, angle2)
        self._blit()

    def rect(self, x, y, width, height):
        self.ctx.rectangle(x, y, width, height)
        self._blit()

    def circle(self, x, y, radius):
        self.arc(x, y, radius, 0, 2 * math.pi)

    def background(self, v1, v2=None, v3=None, a=1.0):
        self.rect(0, 0, self.size[0], self.size[1])

    def _fill(self):
        if self.fillColor is not None:
            norm = self.fillColor.normalize()
            self.ctx.set_source_rgba(*norm)
            self.ctx.fill()

    def _stroke(self):
        if self.fillColor is not None:
            norm = self.strokeColor.normalize()
            self.ctx.set_source_rgba(*norm)
            self.ctx.stroke()

    def _blit(self):
        self._fill()
        self._stroke()

    # Save

    def save(self, filename):
        self.surface.write_to_png(filename)

    def saveFrame(self, filename="screen-####.png"):
        x = re.search("#+", filename)

        if x is None:
            raise Exception("Hashtag (#) not found in filename!")
        elif self.frame > x.end() - x.start():
            raise Exception("Current frame has exceeded hashtag length!")

        frameStr = f"{self.frame:04}"
        filename_ = filename[0 : x.start()] + frameStr + filename[x.end() :]
        self.save(filename_)
        self.frame += 1
