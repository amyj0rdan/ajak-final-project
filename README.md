# Ajak Final Project

[![Build Status](https://travis-ci.com/jpalmerr/ajak-final-project.svg?branch=master)](https://travis-ci.com/jpalmerr/ajak-final-project)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)

This is [our](#authors) final project at Makers Academy, presented at Demo Day on Friday 24 May 2019.

Visit our web app [on Heroku](https://ajak-doodler.herokuapp.com/)!

[Getting started](#getting-started) | [Project description](#project-description) | [Technologies](#technologies) | [Manifesto](#manifesto) |  [Learning documentation](#learning-documentation) | [Authors](#authors) | [Acknowledgements](#acknowledgements)

## Getting started

```bash
git clone https://github.com/amyj0rdan/ajak-final-project
pip3 install -r requirements.txt # to install python dependencies
npm install # to install node dependencies
```

#### To download data

Download `Crown`, `Camera` and `Rabbit` from [Google QuickDraw Dataset](https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap) in numpy-bitmap format and save to `/data` folder in the project under `crowns.npy`, `cameras.npy` and `rabbits.npy`.

#### To train model

```bash
python3 model_config/train.py
```

When prompted by running the above command, save the model as `cameras_rabbits_crowns_model`.
Move the saved model to the `/models` folder.

#### To see model predict random image from test data

```bash
python3 model_config/predict_on_command_line.py
```

#### To run tests

The `pytest` framework is used for unit testing.

To run tests:     
```bash
pytest
```

To run test coverage:     
```bash
pytest --cov=lib
```

#### To run linter

```bash
pylint [options] module_or_package
```
For example:
```bash
pylint lib
```

## Project description

Our project is pictionary played against a model trained to recognise three drawings:
- crown
- camera
- rabbit

A user draws on a canvas against a timer. The model then predicts which of the above the user has drawn and the prediction is displayed to the user.

<img width="750" alt="Screenshot 2019-05-23 at 20 19 56" src="https://user-images.githubusercontent.com/45539085/58560022-2bf9d800-821c-11e9-94a7-326033112b24.png">

## Technologies

**Backend**
- Python3
- Flask

**Testing**
- Pytest
- Splinter

**Machine learning libraries and data**
- Scikit-learn
- Keras
- TensorFlow
- Google QuickDraw Dataset

**Frontend**
- JavaScript
- jQuery
- Fabric JS

**Deployment**
- Travis CI
- Heroku

## Manifesto

Our project [manifesto](https://github.com/amyj0rdan/ajak-final-project/blob/master/manifesto.md) has individual and team project goals, and our ways of working.

Our [Trello board](https://trello.com/b/SAOvMM1v/ajak).

Our [presentation](https://docs.google.com/presentation/d/1GTJL6hVxDfipjO8MemxPloK68e03wOtJmxCWNDJeYpY/edit?usp=sharing) from Demo Day at Makers Academy on Friday 24 May 2019.

## Learning documentation

See our [wiki](https://github.com/jpalmerr/ajak-final-project/wiki).

## Authors

[Alex Chen](https://github.com/alexanderchen6), [Amy Jordan](https://github.com/amyj0rdan), [James Palmer](https://github.com/jpalmerr), [Kim Diep](https://github.com/kimdiep).

## Acknowledgements

Makers Academy
