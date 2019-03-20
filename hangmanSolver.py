from pprint import pprint

dict_words = {}
with open("words2.txt", "r") as f:
	for line in f:
		num_chars = len(line.strip())


		if num_chars not in dict_words:
			dict_words[num_chars] = [line.strip()]
		else:
			dict_words[num_chars].append(line.strip())





num_characters = input("Enter the number of characters: ")





def findMostcommonLetter(array, list_of_chars):
	dict_temp = {}
	for word in new_array:
		for character in word:
			
			if character in dict_temp:
				dict_temp[character] = dict_temp[character] + 1
			else:
				dict_temp[character] = 1
	return dict_temp

array = dict_words[int(num_characters)]



list_of_chars = "abcdefghijklmnopqrstuvwxyz"

while (1):
	k = input("Enter position of letter and character (a 3):")
	letter = k.split(" ")[0]
	position = int(k.split(" ")[1])
	list_of_chars.replace(letter, "")
	
	new_array = []
	if position == -1:
		for word in array:
			if letter not in word:
				new_array.append(word)


	else:
		for word in array:
			if word[position] == letter:
				new_array.append(word)

	

	pprint(new_array)
	pprint(findMostcommonLetter(new_array, list_of_chars))


	array = new_array