
import csv
from random import randint
from review import Review

##### User Message Processing ############################################################

def swear_words(user_msg):
    swears = ["fuck", "dick", "fucker", "shit", 'asshole', 'bitch', 'whore', 'slut']
    words = user_msg.split(" ")
    for word in words:
        for swear in swears:
            if word == swear:
                return True

def recommendation_request(user_msg):
    if user_msg.lower() == "recommend me":
        return True

##### Reply #############################################################################

def recommendation():

    data = []
    with open('cafes.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    randomRow = randint(1, len(data))
    return data[randomRow]

def review(user_msg):

    review = Review(user_msg)
    review.sentiment = review.predict_sentiment()
    review.store_review()

    return review.lemmatized_review
    
 #   if review.sentiment == 1:
 #       return "Thanks for positive review"
 #   else:
 #       return "Sorry, we'll try to improve"
    
	#"""
	#This function analyzes the users review of a cafe

	#:param user_msg: string
	#:return: a string responding to the review
	#"""

##### Chatbot Functionality ##############################################################

def index():
	pass  # don't write anything here yet


def chat():
    user_msg = raw_input("")

    if swear_words(user_msg) is True:
        print "Please choose appropriated words"
    elif recommendation_request(user_msg) is True:
        print recommendation()
    else:
        response_msg = review(user_msg)
        print response_msg


def static_file(path):
	pass  # don't write anything here yet


if __name__ == '__main__':

	print "Hello! My name is Tel Aviv Cafebot. I am a chatbot designed to recommend cafes in Tel Aviv!"
	print "For a recommendation, please write: recommend me"

	while True:

		chat()