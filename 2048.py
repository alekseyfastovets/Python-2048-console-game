from tkinter import Frame, Label, CENTER
import main as logic

class game2048(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.grid()
		self.master.title('2048')
		#self.master.bind("<Key>", self.key_down)
		# self.commands = {c.KEY_UP: logic.up, c.KEY_DOWN: logic.down,
  #                        c.KEY_LEFT: logic.left, c.KEY_RIGHT: logic.right,
  #                        c.KEY_UP_ALT: logic.up, c.KEY_DOWN_ALT: logic.down,
  #                        c.KEY_LEFT_ALT: logic.left, c.KEY_RIGHT_ALT: logic.right,
  #                        c.KEY_H: logic.left, c.KEY_L: logic.right,
  #                        c.KEY_K: logic.up, c.KEY_J: logic.down}
  		self.grid_cells = []
  		self.init_grid()
  		
		self.mainloop()





game2048()