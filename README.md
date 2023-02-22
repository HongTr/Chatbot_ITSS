# Chatbot for ITSS finals (beta)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#installation"> Installation </a></li>
    <li><a href="#training"> Training </a></li>
    <li><a href="#testing"> Testing </a></li>
    <li><a href="#acknowledgments"> Acknowledgments </a></li>
  </ol>
</details>

## About
* This is my project for ITSS finals exam. I created a chatbot that can response entities and intents from user's messages.
* Training data is from [lumi project](https://lumichatbot.github.io/#/), i augmented data for testing and customize action for my purpose.

## Installation
```
source env/bin/activate
pip3 install -r requirements.txt
```

## Training
```
rasa train
```

## Test chatbot (open two terminals)
```
rasa run actions
rasa shell
```

## Acknowledgments
* [Lumi Project](https://lumichatbot.github.io/#/)
* [Rasa documentation](https://rasa.com/docs/) and [Rasa tutorial](https://www.youtube.com/playlist?list=PL75e0qA87dlEjGAc9j9v3a5h1mxI2Z9fi)