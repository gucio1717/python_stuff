class Root(object):
    def draw(self):
        # the delegation chain stops here
        print "dalej nie"
   #     assert not hasattr(super(Root, self), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super(Shape, self).__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super(Shape, self).draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        print(kwds)
        super(ColoredShape, self).__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super(ColoredShape, self).draw()

cs = ColoredShape(color='blue', shapename='square')
cs.draw()



