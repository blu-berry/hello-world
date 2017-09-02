

def changer(text, shift=3):
	output_text = ''
	
	for letter in text:
		if letter.islower():
			output_text += chr(((ord(letter) - ord("a") + shift) % 26) + ord("a"))
		else:
			output_text += chr(((ord(letter) - ord("A") + shift) % 26) + ord("A"))
	
	print(output_text)
	return
	


input_text = input()
step = input()
changer(input_text, int(step))
