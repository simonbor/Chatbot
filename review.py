
import csv
import spacy.en as spcy
from random import randint
from spacy.en import English

class Review(object):
    def __init__(self, review_text, stars=None):

        self.review = self.clean_text(review_text)
        self.review_sentiment = self.convert_stars(stars)

        self.top_words_in_corpus = ["good", "bad", "amazing", "disgusting", "menu"]
        self.lemmatized_review = self.lemmatize(review_text)

    def clean_text(self, review_text):
        tmp_str = review_text.replace("...\nMore", "")
        return tmp_str.decode('utf-8')

    def convert_stars(self, stars):

        if stars is None:
            return stars

        if stars >= 3:
            return 1
        else:
            return 0

    def predict_sentiment(self):

        return randint(0, 1)
        # """
        # In the future this section will use a ML model to predict negative:0 or
        #  positive:1 sentiment.
        # :return: a randomly generate a number between 0 and 1
        # """

    def store_review(self):

        with open('submitted_cafe_reviews.csv', 'ab') as csvfile:  # wb stands for write
            writer = csv.writer(csvfile)
            writer.writerow(["{0},{1}".format(self.review, self.review_sentiment)])

        # """
        # store self.review in a csv file called submitted_cafe_reviews.csv
        #
        # In the future, this section will provide extra data for a ML model!
        # """

    def lemmatize(self, review_text):

        parser = English()
        lemmas = []

        doc = parser(review_text.decode("utf-8"))

        for token in doc:
            if token.lemma_ not in spcy.STOP_WORDS:
                lemmas.append(token.lemma_)

        return lemmas

    def sentiment_feature_extraction(self, top_words):

        features = []

        for top_word in self.top_words_in_corpus:
            if top_word in self.lemmatized_review:
                features.append(1)
            else:
                features.append(0)

        return features

# Once you are done coding the above class, test it out by running it in the console
# It should print out the first 5 reviews and their sentiment (0 or 1)
#if __name__ == '__main__':
#
#    rows = []
#    with open("cafe_reviews.csv") as csvfile:
#        reader = csv.reader(csvfile)
#        for row in reader:
#            rows.append(row)
#
#    for i in rows[1:6]:
#        review = Review(i[1], int(i[2]))
#        print review.review, review.review_sentiment
#        review.store_review()
