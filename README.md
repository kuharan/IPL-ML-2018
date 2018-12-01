# Indian Premier League Predictions - 2018

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://shields.io/)
[![GitHub forks](https://img.shields.io/github/forks/kuharan/IPL-ML-2018.svg)](https://github.com/kuharan/IPL-ML-2018/network)
[![GitHub license](https://img.shields.io/github/license/kuharan/IPL-ML-2018.svg)](https://github.com/kuharan/IPL-ML-2018/blob/master/LICENSE)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/kuharan/IPL-ML-2018/.svg?style=social)](https://twitter.com/intent/tweet?text=Wow!&nbsp;This&nbsp;is&nbsp;so&nbsp;Cool:&url=https%3A%2F%2Fgithub.com%2Fkuharan%2FIPL-ML-2018%2F)



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
Allow installation of apps from unknown sources.

[Android App Link](https://drive.google.com/file/d/1y27A_qlN9aEUUejGptflbxLCdof73srs/view?usp=sharing)

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
_List of all the packages that have been used in this project is frozen into [requirements.txt](requirements.txt) file._

## Dataset 
The dataset that we use in this project is IPL (Indian Premier League) Dataset posted on Kaggle Datasets sourced from cricsheet. And calculated Team data based on player EF scores. 

#### EFscore: 
The eigenfactor score, a metric used for ranking teams in different formats of the game. This is an alternative way of ranking teams in international Cricket, by taking into account the relative strengths of the teams. A victory against a relatively stronger team will lead to a higher EFscore as compared to a victory against a relatively weaker team.

The advantage of this method is that it is a non-parametric way of ranking teams, that is we do not give any additional parameters to the algorithm for computing the team rankings.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Deployment
Click on this button to set up a live system on Heroku Cloud!

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Contributing  [![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

Please submit a pull request to this repo or open an issue.

## Authors 
[![Maintainers Wanted](https://img.shields.io/badge/maintainers-wanted-red.svg)](https://github.com/pickhardt/maintainers-wanted)
* **Vishal Yadav** - [Vishal Yadav](https://github.com/vishal-kr-yadav)
* **Kuharan Bhowmik** - [Kuharan Bhowmik](https://github.com/kuharan)

## Security Update
#### CVE-2018-18074 Detail [![NATIONAL VULNERABILITY DATABASE](https://nvd.nist.gov/vuln/detail/CVE-2018-18074)]
The Requests package before 2.20.0 for Python sends an HTTP Authorization header to an http URI upon receiving a same-hostname https-to-http redirect, which makes it easier for remote attackers to discover credentials by sniffing the network. This project now uses requests 2.20.0.

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE.md](LICENSE) file for details.

