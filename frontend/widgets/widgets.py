
# from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty
from kivy.animation import Animation
from kivy.core.window import Window

class HoverBehavior(object):
    """Hover behavior. When combined with a widget, it will
    change the background color when the mouse is over the widget.
    """

    def __init__(self, **kwargs):
        self.hovered = False
        self._background_color = None
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        if self.collide_point(*self.to_widget(*pos)):
            if not self.hovered:
                self.hovered = True
                self.on_hover()
        else:
            if self.hovered:
                self.hovered = False
                self.on_leave()

    def on_hover(self):
        """The mouse is over the widget"""
        if hasattr(self, 'bar_color'):
            self._background_color = self.bar_color
            anim = Animation(bar_color=(0.7, 0.7, 0.7, 1), d=0.2)
            anim.start(self)

    def on_leave(self):
        """The mouse is leaving the widget"""
        if self._background_color:
            anim = Animation(bar_color=self._background_color, d=0.2)
            anim.start(self)

class HoverScrollBar(ScrollView, HoverBehavior):
    normal_color = ListProperty([1, 0, 0, 0.5])
    hover_color = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bar_color = self.normal_color

    def on_enter(self):
        self.bar_color = self.hover_color

    def on_leave(self):
        self.bar_color = self.normal_color

        
class AnimatedButton(Button, HoverBehavior):
    pass

