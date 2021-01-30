import subprocess

class Notify:
	@staticmethod
	def anounce(text):
		subprocess.run(["notify-send", "-i", "face-wink", text])
