import csv
from review import Review
import pandas
import collections
import random
import numpy as np
from sklearn import svm
from spacy.en import English

# class SentimentAnalysis(object):

#     def __init__(self, training_reviews, testing_reviews, lemmatize_words, review_sentiment):

#         # list (random.shuffle) of Review objects of the first 300 positive and first 300 negative reviews
#         self.training_reviews = training_reviews_shuffle(training_reviews) 

#         # list of Review objects of the remaining positive and remaining negative reviews
#         self.testing_reviews = testing_reviews

#         # list of the top 3000 most frequently seen words in all the lemmatized_reviews of all Review objects 
#         # in training_reviews
#         self.top_words = find_top_words(training_reviews, lemmatize_words)

#         # a pandas Dataframe, data = the output of the sentiment_feature_extraction method of all the Review objects in 
#         # training_reviews, use top_words as your column names
#         self.training_features = pd.DataFrame(data=sentiment_feature_extraction(training_reviews), columns=top_words)

#         # a pandas Series, data = the values stored in review_sentiment of all the Review objects in training_reviews
#         self.training_labels = [] # ???

#         # a pandas Dataframe, data = the output of the sentiment_feature_extraction method of all the Review objects 
#         # in testing_reviews, use top_words as your column names
#         self.testing_features = pd.DataFrame(data=sentiment_feature_extraction(testing_reviews), columns=top_words)

#         # a pandas Series, data = the values stored in review_sentiment of all the Review objects in testing_reviews
#         self.testing_labels = [] # ???

#     pass

# --------------------------------------
# functions
# --------------------------------------

def open_csv(file_location):
	"""
	:param file_location: string
	:return: list of Review objects
	"""

	review_objs = []

	with open(file_location) as csvfile:
		reader = csv.reader(csvfile)
		reader.next()  # skip the header

		for row in reader:
            parser = English()
			review = Review(row[1], parser, stars=int(row[2]))  # create Review object and store it in a list
			review_objs.append(review)

	return review_objs

def sentiment_feature_extraction(reviews):

    return reviews

# random shuffle reviews
def training_reviews_shuffle(reviews):

    return random.shuffle(reviews)

def find_top_words(review_objs):

    # # TODO: 3000 most frequently seen words in all the lemmatized_reviews of all Review objects in training_reviews
    # list_of_all_words = "" # ???
    # word_counts = collections.Counter(list_of_all_words)
    # word_counts.most_common(3000)

    # return []

    """
    :param review_objs: list of Review objects
    :return: list of the top 3000 words used
    """

    all_words = []
    for review_obj in review_objs:
        all_words.extend(review_obj.lemmatized_review)  # extend combines 2 lists

    word_counts = collections.Counter(all_words)  # counter object counts occurances of the words

    return [w[0] for w in word_counts.most_common(3000)]

def find_features(review_objs, top_words):
    """

    :param review_objs: list of Review objects
    :param top_words: list of top words
    :return:
    """

    all_features = []

    # iterates through review objects and uses the sentiment_feature_extraction method
    for review_obj in review_objs:
        features = review_obj.sentiment_feature_extraction(top_words)
        all_features.append(features)  # all_features becomes a list of lists

    df = pandas.DataFrame(data=np.array(all_features), columns=top_words)
    return df


def find_labels(review_objs):

    all_labels = []

    # iterate through review objects and pull out the label (review sentiment)
    for review_obj in review_objs:
        label = review_obj.review_sentiment
        all_labels.append(label)

    sr = pandas.Series(data=np.array(all_labels))  # put labels into pandas data series
    return sr

# --------------------------------------
# main section 
# --------------------------------------

if __name__ == '__main__':
    

	# get review data from csv file
	review_objs = open_csv("cafe_reviews.csv")

	# separate into positive and negative, allocate correctly for training/testing
	positive_reviews, negative_reviews = sort_reviews(review_objs)
	training_reviews = positive_reviews[:300] + negative_reviews[:300]  # training always must have equal positive/negative
	testing_reviews = positive_reviews[300:] + negative_reviews[300:]

    # training_reviews = []
    # testing_reviews = []
    # pos = 0
    # neg = 0
    # max = 300

    # with open("cafe_reviews.csv") as csvfile:
    #     rows = csv.reader(csvfile)
    #     for row in rows:
    #         if row[2]>3 and pos < max:
    #             trainig_reviews.append(row)
    #             pos+=1
    #         elif row[2]<4 and neg < max:
    #             trainig_reviews.append(row)
    #             neg+=1
    #         else:
    #             testing_reviews.append(row)

    #sentimentAnalysis = SentimentAnalysis(training_reviews, testing_reviews)

	# get the top words used in the TRAINING REVIEWS, always use this list!!!!
	top_words = find_top_words(training_reviews)

	random.shuffle(training_reviews)  # shuffle :)

	# make the dataframes
	training_features = find_features(training_reviews, top_words)
	training_labels = find_labels(training_reviews)

   	# make the dataframes
	testing_features = find_features(testing_reviews, top_words)
	testing_labels = find_labels(testing_reviews)

    # ==================================================
    # Intelligent Bot Exercise 1
    # ==================================================
    # 1) Initiate the SVC classifier
	clf = svm.SVC()

    # 2) Fit the model with the training data
	clf.fit(training_features, training_labels)

    # 3) Print out the accuracy with the testing data
	accuracy = clf.score(testing_features, testing_labels)
	print accuracy

    # positive_text = "This restaurant was the best! I loved the pizza and the service was fast.”
    # negative_text = "This restaurant was awful. The food was so bad and the service was slow. Never going again!"

    # print clf.predict(real_time_features)
