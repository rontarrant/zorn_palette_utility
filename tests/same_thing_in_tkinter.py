import tkinter as tk
from tkinter import messagebox

class MyApplication:
	def __init__(self, root):
		self.root = root
		self.root.title("My Application")

		# Create the main frame
		self.main_frame = tk.Frame(self.root)
		self.main_frame.pack(padx=20, pady=20)

		# Create widgets and add them to the main frame
		new_button = tk.Button(self.main_frame, text='New', command=self.on_new_button_clicked)
		new_button.pack()

		# You can add more widgets as needed

	def on_new_button_clicked(self):
		# Implement the 'New' button functionality here
		response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
		
		if response is not None:
			if response:
				self.save_data()
			else:
				self.reset_data()

	def save_data(self):
		# Implement save data logic
		messagebox.showinfo("Save", "Data saved successfully")

	def reset_data(self):
		# Implement reset data logic
		messagebox.showinfo("Reset", "Data reset")

if __name__ == '__main__':
	root = tk.Tk()
	app = MyApplication(root)
	root.mainloop()