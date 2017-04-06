# coding=utf-8
# imports here
import csv
from random import randint

class Review(object):
    def __init__(self, review_text, stars=None):
        """
        The Review class will include all the functionality we need for analyzing reviews.
        :param review_text: str
        :param stars: int
        """

        # self.review is a class attribute & should store what the clean_text method returns
        self.review = self.clean_text(review_text)

        # self.review_sentiment is a class attribute & should store what the convert_stars method returns
        self.review_sentiment = self.convert_stars(stars)


    def clean_text(self, review_text):
        """
        This method should replace the string “...\nMore” if it appears in the review_text & replace it with a blank
        string. Then fix the encoding.

        Strings have two useful methods:
            1)   .replace(unwanted_str, wanted_str)
            2)   .decode('utf-8')

        :param review_text: str
        :return: str cleaned of junk
        """

        return review_text.replace("...\nMore", "").decode('utf-8')

    def convert_stars(self, stars):
        """
        This method should implement the following logic:
            if the stars variable isn’t None  & if stars is greater than or equal to 3, return an integer 1
            if the stars variable isn’t None  & if stars is less than 3, return an integer 0
            otherwise, return None

        :param stars: int
        :return: int or None
        """

        if stars is not None:
            if stars >= 3:
                return 1
            else:
                return 0
        else:
            return None


    def predict_sentiment(self):
        """
        If a review comes from one of our users & therefore does not have a
        star rating, we will use this method to predict if it was positive
        or negative sentiment using NLP & ML.
        
        In the future this section will use a ML model to predict 0 for
        negative sentiment, 1 for positive sentiment.
        
        In the Basic Bot section: randomly generate a number between 0 and 1
        :return: int
        """
        sentiment = randint(0, 1)

        return sentiment


    def store_review(self):
        """
        store self.review in a csv file called submitted_cafe_reviews.csv

        In the future, this section will provide extra data for a ML model!
        """
        file_location = 'submitted_cafe_reviews.csv'

        with open(file_location, 'ab') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.review])


# Once you are done coding the above class, test it out by running it in the console
# It should print out the first 5 reviews and their sentiment (0 or 1)
# When it passes this test, please delete these comments and this main section below :)
if __name__ == '__main__':

    rows = []
    with open("cafe_reviews.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)

    for i in rows[1:5]:
        review = Review(i[1], int(i[2]))
        print review.review, review.review_sentiment