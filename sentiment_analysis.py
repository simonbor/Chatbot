class SentimentAnalysis(object):

    # main section 
    def __init__(self):

        # list (random.shuffle) of Review objects of the first 300 positive and first 300 negative reviews
        self.training_reviews = [] 

        # list of Review objects of the remaining positive and remaining negative reviews
        self.testing_reviews = []

        # list of the top 3000 most frequently seen words in all the lemmatized_reviews of all Review objects in training_reviews
        self.top_words = []

        # a pandas Dataframe, data = the output of the sentiment_feature_extraction method of all the Review objects in training_reviews, use top_words as your column names
        self.training_features = []

        # a pandas Series, data = the values stored in review_sentiment of all the Review objects in training_reviews
        self.training_labels = []

        # a pandas Dataframe, data = the output of the sentiment_feature_extraction method of all the Review objects in testing_reviews, use top_words as your column names
        self.testing_features = []

        # a pandas Series, data = the values stored in review_sentiment of all the Review objects in testing_reviews
        self.testing_labels = []

    pass

    # functions

if __name__ == '__main__':
    
    sentimentAnalysis = SentimentAnalysis()

