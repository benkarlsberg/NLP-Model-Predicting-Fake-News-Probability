![](images/title_image.png)

# Fake News Detector
**Using Modern Machine Learning Techniques to Identify False Information in Political News Articles**<br>
by Benjamin Karlsberg<br>

### Table of Contents

* [Background](#background)
* [Data](#data)
* [Model Testing](#models)
* [Results](#results)
* [Dash Web App](#app)
* [Conclusion](#conclusion)

<a name="background"></a>
## Background

### What is “Fake” News?
In a broad sense, “fake” news contains information that is false or exaggerated beyond objective facts. Fake news articles tend to contain language that is opinionated and biased towards one viewpoint in order to promote a political agenda or to generate views for advertising.

### How the Detector Works
By honing in on the language that tends to be used in “real” and “fake” news articles, the detector is able to calculate the probability of the article being from a factual source. 
*Note: this does not imply that the detector verifies actual claims in the articles. It primarily suspects the article of being biased or not.

<a name="data"></a>
## Data

The data that was used to train the model contains over 70,000 labeled articles that were sourced from “Politifact.com” (80%), “The New York Times” (10%), and “The Onion Magazine (10%).” 47% of the articles were labeled as “fake” and 53% as “true.”

[IEEEDataport - Fake News Data](https://ieee-dataport.org/documents/fake-news-data)

[Kaggle - Fake and Real](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset?select=True.csv)

[Kaggle - Onion or Not](https://www.kaggle.com/chrisfilo/onion-or-not?select=OnionOrNot.csv)

[Kaggle - All the News](https://www.kaggle.com/snapcrack/all-the-news?select=articles1.csv)

<a name="models"></a>
## Model Testing

<a name="results"></a>
## Results

<a name="app"></a>
## Dash Web App

<a name="conclusion"></a>
## Conclusion
