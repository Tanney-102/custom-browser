import tkinter
import packages.request as request

DEFAULT_WIDTH, DEFAULT_HEIGHT = 800, 600

class Browser:
  def __init__(self):
    self.window = tkinter.TK()
    self.canvas = tkinter.Canvas(
      self.window,
      width = DEFAULT_WIDTH,
      height = DEFAULT_HEIGHT,
    )
    self.canvas.pack()

  def run(self):
    tkinter.mainloop()

  def loadPage(self, url):
    response = request.get(url)

    self.canvas.create_rectangle(10, 20, 400, 300)
    self.canvas.create_oval(100, 100, 150, 150)
    self.canvas.create_text(200, 150, text='hey')