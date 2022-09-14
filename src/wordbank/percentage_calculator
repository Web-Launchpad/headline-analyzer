def percentage_calculator(words: list[tuple]) -> dict:
	bucket_listing = []
	[bucket_listing.append(word[1]) for word in words]
	unique_listing = list(set(bucket_listing))
	word_percentage_share = {}
	for unique_word in unique_listing:
		word_percentage_share[unique_word] = (bucket_listing.count(unique_word) / len(words)) * 100

	return word_percentage_share