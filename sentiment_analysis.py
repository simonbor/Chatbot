import pandas as pd

class SentimentAnalysis(object):

    def __init__(self, training_reviews, testing_reviews, lemmatize_words, review_sentiment):

        # list (random.shuffle) of Review objects of the first 300 positive and first 300 negative reviews
        self.training_reviews = training_reviews_shuffle(training_reviews) 

        # list of Review objects of the remaining positive and remaining negative reviews
        self.testing_reviews = testing_reviews

        # list of the top 3000 most frequently seen words in all the lemmatized_reviews of all Review objects 
        # in training_reviews
        self.top_words = top_words(training_reviews, lemmatize_words)

        # a pandas Dataframe, data = the output of the sentiment_feature_extraction method of all the Review objects in 
        # training_reviews, use top_words as your column names
        self.training_features = pd.DataFrame(data=sentiment_feature_extraction(training_reviews), columns=top_words)

        # a pandas Series, data = the values stored in review_sentiment of all the Review objects in training_reviews
        self.training_labels = [] # ???

        # a pandas Dataframe, data = the output of the sentiment_feature_extraction method of all the Review objects 
        # in testing_reviews, use top_words as your column names
        self.testing_features = pd.DataFrame(data=sentiment_feature_extraction(testing_reviews), columns=top_words)

        # a pandas Series, data = the values stored in review_sentiment of all the Review objects in testing_reviews
        self.testing_labels = [] # ???

    pass

    # --------------------------------------
    # functions
    # --------------------------------------

    def sentiment_feature_extraction(reviews):

        return reviews

    def training_reviews_shuffle(reviews):

        # TODO: random shuffle reviews

        return reviews

    def top_words(lemmatized_reviews, training_reviews):

        # TODO: 3000 most frequently seen words in all the lemmatized_reviews of all Review objects in training_reviews

        return []

# --------------------------------------
# main section 
# --------------------------------------

if __name__ == '__main__':
    
    training_reviews = []
    testing_reviews = []
    pos = 0
    neg = 0
    max = 300

    with open("cafe_reviews.csv") as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            if row[2]>3 and pos < max:
                trainig_reviews.append(row)
                pos+=1
            elif row[2]<4 and neg < max:
                trainig_reviews.append(row)
                neg+=1
            else:
                testing_reviews.append(row)

    sentimentAnalysis = SentimentAnalysis(training_reviews, testing_reviews)

