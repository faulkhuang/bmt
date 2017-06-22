# encoding: utf-8

from gi.repository import gtk


window = gtk.get_default_root_window()
x, y, width, height = window.get_geometry()

print("The size of the root window is {} x {}".format(width, height))

pb = gtk.pixbuf_get_from_window(window, x, y, width, height)

if pb:
    pb.savev("svreenshot.png", "png", (), ())
    print("Screenshot saved to screenshot.png.")
else:
    print("Unable to get the screenshot.")