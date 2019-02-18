from OpenGL.GLUT import GLUT_BITMAP_9_BY_15

class Text(object):

    def __init__(self,
                 text,
                 pos=(0., 0., 0.),
                 color=(1., 1., 1.),
                 alpha=.6,
                 font=GLUT_BITMAP_9_BY_15):

        self.text = text
        self.position = tuple(pos)
        self.color = color
        self.alpha = alpha
        self.font = font

