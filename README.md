# Indian Premier League Predictions - 2018
The Indian Premier League, officially Vivo Indian Premier League (_for sponsorship reasons_), is a professional Twenty20 cricket league in India contested during April and May of every year by teams representing Indian cities and some states.

This project is an attempt to predict the winner of T20 cricket matches. The objective is to predict the result (winner) of every IPL match. The project also predicts the ultimate winner of the tournament. It does not impose a specific development philosophy or framework, so you're free to clone, modify and architect your code in the way that you want and add your contribution to this repository.

## We are Live on Heroku!
* [Link1](https://ipl2018prediction.herokuapp.com/)
* [Link2](https://iplprediction2018.herokuapp.com/)

## Download for Android
If you’re greeted with, "Install blocked. For security, your phone is set to block installation of applications not obtained from Play Store" message as you try to install, follow this steps:

Navigate to Setting > Security.
Check the option "Unknown sources".
Tap OK on the prompt message.
Allow installation of aps from unknown sources.

[Android App Link](https://a2.files.diawi.com/app-file/2XAH2mIXkofeXPvYjdux.apk)

### Features
Minimum OS version - Jelly Bean 4.1, 4.1.1
Target OS version - Marshmallow 6.0
Size - 4.69 MB

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* **PyCharm**
* _Any Web Browser_

#### PyCharm Packages Used
```
Pandas, sklearn, sklearn.tree, model_selection, DecisionTreeClassifier, csv, Flask, BeautifulSoup, requests, json 
```
_List of all the packages that have been used in this project are freezed into [requirements.txt](requirements.txt) file._

## Dataset 
The dataset that we use in this project is IPL (Indian Premier League) Dataset posted on Kaggle Datasets sourced from cricsheet. And calculated Team data based on player EF scores. 

#### EFscore: 
The eigenfactor score, a metric used for ranking teams in different formats of the game. This is an alternative way of ranking teams in international Cricket, by taking into account the relative strengths of the teams. A victory against a relatively stronger team will lead to a higher EFscore as compared to a victory against a relatively weaker team.

The advantage of this method is that it is a non-parametric way of ranking teams, that is we do not give any additional parameters to the algorithm for computing the team rankings.

## Cloning/Forking
See [Forking](https://help.github.com/articles/fork-a-repo/) for details.

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE used for Machine Learning Model and Scraping Websites
* [WebStorm](https://www.jetbrains.com/webstorm/) - IDE used for the Web Application UI

## Contributing

Please submit a pull request to this repo or open an issue.

## Deployment
Click on this button to setup a live system on Heroku Cloud!

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Authors

* **Vishal Yadav** - [Vishal Yadav](https://github.com/vishal-kr-yadav)
* **Kuharan Bhowmik** - [Kuharan Bhowmik](https://github.com/kuharan)

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE.md](LICENSE) file for details.
