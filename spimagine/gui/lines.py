class Lines(object):

    def __init__(self,
                 vertices=[[0, 0, 0], [1, 0, 0], [1, 1, 0]],
                 linecolor=(1., 1., 1.),
                 alpha=.6,
                 width=1.0):

        self.vertices = vertices
        self.linecolor = linecolor
        self.alpha = alpha
        self.width = width
