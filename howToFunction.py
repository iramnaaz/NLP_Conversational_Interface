def howTo(question):
	question_words = question.split()

	search_url = 'google.com/search?q=' + '+'.join(question_words)

	return_term = 'No worries, I found a reference for you: ' + search_url

	return return_term