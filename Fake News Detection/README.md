# Fake News Detection
  This NLP project is still in initial stage. I've completed the EDA part of the project and working on it.
  
# Overview
  News media has gotten to be a channel to pass on the data of what’s happening within the world to the individuals living. Regularly people perceive anything passed on within the news to be genuine. There were circumstances where even the news channels recognized that their news isn't genuine as they composed. But a few news incorporates a noteworthy affect not as it were on the individuals or government but too on the economy.
  
  The data science community has reacted by taking activity to battle the issue. There’s a Kaggle-style competition called the “Fake News” and numerous social media platform using AI to channel fake news stories out of users’ nourishes.

# Problem Statement
  One news can move the bends up and down depending on the feelings of individuals and political situation. The issue isn't as it were programmers, going into accounts, and sending untrue data. The greater issue here is what we call “Fake News”. A fake are those news stories that are wrong: the story itself is manufactured, with no unquestionable realities, sources, or cites.
  
# Objectives:
  1.	Our sole objective is to classify the news from the dataset as fake or true news.
  2.	 Extensive EDA of news.
  3.	Selecting and building a powerful model.
  4.	Using the model to classify the news.

# Data Set Source
  * https://www.kaggle.com/c/fake-news/data

# Files overview
  * FakeNewsClassifier_Capstone_Project_whole_text.ipynb
    * EDA has been performed on the dataset till now.
  * detectTheLanguageAndAppendInCSV.ipynb
    * After generating word cloud we found that english is not the only language used in the dataset, so we wrote a code to detect the language used and diversify the dataset. For this we added one column named 'Language' in the dataset and set it by default to 'e'. Now we used nltk library - more specifically TextCat - to identify the language and replaced the newly created column values.

# Liberaries used in the project
  * ScikitLearn (https://github.com/scikit-learn/scikit-learn)
  * MatplotLib (https://github.com/matplotlib/matplotlib)
  * NumPy (https://github.com/numpy/numpy)
  * wordcloud (https://github.com/amueller/word_cloud)
  * nltk (https://github.com/nltk/nltk)
