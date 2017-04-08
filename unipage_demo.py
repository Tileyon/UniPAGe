# -----------------------------------------------------------------------------
# Name:        UniPaGe
# Purpose:     Adaptable Graphic User Interface for Python
#
# Author:      Ti Leyon
#
# Created:     04/04/2017
# Copyright:   (c) Ti Leyon 2017
# Licence:     K E
# -----------------------------------------------------------------------------


class unipage(object):
    def __init__(self, kivy, screen_size):
        self.kivy = kivy
        self.screen_size = screen_size
        self.unibuttons = []
        self.unitexts = []
        self.unilabels = []
        self.unimages = []
        self.uniframes = []

    def setscreen(self):
        if self.kivy:
            from kivy.uix.floatlayout import FloatLayout
            from kivy.core.window import Window
            self.root = FloatLayout()
            Window.size = self.screen_size
        else:
            import ui
            self.root = ui.View(frame=(0, 0,
                                       self.screen_size[0],
                                       self.screen_size[1]))

    def unibutton(self, params):
        x, y, w, h, text = params[:5]
        xratio = self.screen_size[0] / 800.0
        yratio = self.screen_size[1] / 600.0
        self.unibuttons.append([])
        function = params[5] if len(params) == 6 else nofunction
        if self.kivy:
            from kivy.uix.button import Button
            self.unibuttons[-1] = Button(text=text, size_hint_y=None,
                                         size_hint_x=None,
                                         height=h * yratio,
                                         width=w * xratio,
                                         pos=(x * xratio, y * yratio),
                                         on_press=function)
            self.root.add_widget(self.unibuttons[-1])
        else:
            import ui
            self.unibuttons[-1] = ui.Button(frame=(x * xratio,
                                                   (600 - y - h) * yratio,
                                                   w * xratio, h * yratio),
                                            title=text)
            last_unibutton = self.unibuttons[-1]
            last_unibutton.background_color = (0.4, 0.4, 0.4)
            last_unibutton.action = function
            last_unibutton.height = h * xratio
            last_unibutton.width = w * yratio
            last_unibutton.tint_color = 'white'
            self.root.add_subview(last_unibutton)

    def unitext(self, params):
        x, y, w, h, text = params[:5]
        xratio = self.screen_size[0] / 800.0
        yratio = self.screen_size[1] / 600.0
        self.unitexts.append([])
        if self.kivy:
            from kivy.uix.textinput import TextInput
            self.unitexts[-1] = TextInput(
                id='text' + str(len(self.unitexts) - 1),
                size_hint_y=None,
                size_hint_x=None,
                height=h * yratio,
                width=w * xratio,
                text=text,
                multiline=True,
                pos=(x * xratio, y * yratio))
            self.root.add_widget(self.unitexts[-1])
        else:
            import ui
            self.unitexts[-1] = ui.TextField(
                frame=(x * xratio, (600 - y - h) * yratio,
                       w * xratio, h * yratio))
            last_unitext = self.unitexts[-1]
            last_unitext.bordered = False
            last_unitext.background_color = 'white'
            last_unitext.font = ('<system>', 23 * xratio)
            last_unitext.text = text
            self.root.add_subview(last_unitext)

    def unilabel(self, params):
        x, y, w, h, text = params[:5]
        xratio = self.screen_size[0] / 800.0
        yratio = self.screen_size[1] / 600.0
        self.unilabels.append([])
        if self.kivy:
            from kivy.uix.label import Label
            self.unilabels[-1] = Label(pos=(x * xratio, y * yratio),
                                       size_hint=(1.0, 1.0), halign="left",
                                       valign="bottom", text=text)
            last_unilabel = self.unilabels[-1]
            last_unilabel.bind(size=last_unilabel.setter('text_size'))
            self.root.add_widget(last_unilabel)
        else:
            import ui
            self.unilabels[-1] = ui.Label(frame=(x * xratio,
                                                 (600 - y - h) * yratio,
                                                 w * xratio, h * yratio))
            last_unilabel = self.unilabels[-1]
            last_unilabel.text = text
            last_unilabel.text_color = 'white'
            last_unilabel.alignment = ALIGN_LEFT = True  # TODO: ???
            last_unilabel.font = ('<system>', 18 * xratio)
            self.root.add_subview(last_unilabel)

    def unimage(self, params):
        x, y, w, h, source = params[:5]
        xratio = self.screen_size[0] / 800.0
        yratio = self.screen_size[1] / 600.0
        self.unimages.append([])
        if self.kivy:
            from kivy.uix.image import Image
            self.unimages[-1] = Image(source=source, allow_stretch=True,
                                      size_hint=(None, None),
                                      size=(w * xratio, h * yratio),
                                      pos=(x * xratio, y * yratio))
            self.root.add_widget(self.unimages[-1])
        else:
            import ui
            self.unimages[-1] = ui.ImageView(name='Image',
                                             frame=(x * xratio,
                                                    (600 - y - h) * yratio,
                                                    w * xratio, h * yratio))
            self.root.add_subview(self.unimages[-1])
            self.unimages[-1].image = ui.Image.named(source)

    def uniframe(self, params):
        x, y, w, h, color = params[:5]
        xratio = self.screen_size[0] / 800.0
        yratio = self.screen_size[1] / 600.0
        if self.kivy:
            from kivy.graphics import Color
            from kivy.graphics import Rectangle
            self.root.canvas.add(Color(color[0], color[1], color[2]))
            self.root.canvas.add(Rectangle(pos=(x * xratio, y * yratio),
                                           size=(w * xratio, h * yratio)))
        else:
            import ui
            xratio = self.screen_size[0] / 800.0
            yratio = self.screen_size[1] / 600.0
            self.uniframes.append([])
            self.uniframes[-1] = ui.View(frame=(x * xratio,
                                                (600 - y - h) * yratio,
                                                w * xratio, h * yratio))
            self.uniframes[-1].background_color = (color[0], color[1],
                                                   color[2], 1.0)
            self.root.add_subview(self.uniframes[-1])

    def showpage(self):
        if self.kivy:
            from kivy.base import runTouchApp
            runTouchApp(self.root)
        else:
            self.root.present('sheet')


class uniscreen(unipage):
    screendef = []

    def __init__(self, screendef):
        try:
            from kivy.uix.floatlayout import FloatLayout
            kivy = True
        except:
            import ui
            kivy = False
        unipage.__init__(self, kivy, screendef[0])
        self.setscreen()
        self.screendef = screendef

    def setpage(self):
        for k in range(1, len(self.screendef)):
            self.screendef[k][0](self, self.screendef[k][1])


def closepage(sender):
    if mypage.kivy:
        from kivy.utils import platform as core_platform
        from kivy.core.window import Window
        import sys

        if core_platform == 'android':
            sys.exit()
        else:
            Window.close()
    else:
        mypage.root.close()


def function_1(sender):
    mypage.unitexts[0].text = 'Oh! You clicked my button.'


def nofunction(sender):
    pass


if __name__ == '__main__':
    unilabel = unipage.unilabel
    uniframe = unipage.uniframe
    unitext = unipage.unitext
    unibutton = unipage.unibutton
    unimage = unipage.unimage
    widgets = [(600, 450),
               (uniframe, (0, 0, 600, 450, (.6, .6, .6))),
               (unilabel, (80, 10, 240, 20, 'Hey I am just a simple label.')),
               (unibutton, (40, 40, 100, 40, 'Click me', function_1)),
               (unibutton, (460, 40, 100, 40, 'Close me', closepage)),
               (unitext, (40, 120, 300, 40, 'I am a text field')),
               (unimage, (460, 310, 100, 100, 'insidelogo.png'))]
    mypage = uniscreen(widgets)
    mypage.setpage()
    mypage.showpage()
