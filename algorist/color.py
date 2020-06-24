import numpy as np
import colorsys

RGB = "RGB"
HSB = "HSB"


class Color:
    def __init__(self, *args, max=None, colorMode=RGB):
        if max is None:
            self.max = np.array([255, 255, 255, 255], dtype=np.float32)
        else:
            self.max = np.array(max, dtype=np.float32)

        self.colorMode = colorMode

        self.setColor(*args)

    def __str__(self):
        return f"Color: {self.value[0]:.2f} {self.value[1]:.2f} {self.value[2]:.2f} {self.value[3]:.2f}"

    def setColor(self, *args):
        args = list(args)
        lenargs = len(args)
        if lenargs > 4 or lenargs == 0:
            raise TypeError(f"Color() takes 1 to 4 arguments but {lenargs} were given")

        if lenargs == 1:  # Grayscale
            self.value = np.array([args[0], args[0], args[0], self.max[3]], dtype=np.float32)
        elif lenargs == 2:  # Grayscale with alpha
            self.value = np.array([args[0], args[0], args[0], args[1]], dtype=np.float32)
        elif lenargs == 3:  # Color
            self.value = np.array([args[0], args[1], args[2], self.max[3]], dtype=np.float32)
        else:  # Color with alpha
            self.value = np.array([args[0], args[1], args[2], args[3]], dtype=np.float32)

        np.clip(self.value, 0.0, self.max, out=self.value)

        if self.colorMode == HSB:
            norm = self.normalize()
            rgb = colorsys.hsv_to_rgb(norm[0], norm[1], norm[2])
            self.value[0:-1] = np.array(rgb, dtype=np.float32) * self.max[0:-1]

    def normalize(self):
        return self.value / self.max
