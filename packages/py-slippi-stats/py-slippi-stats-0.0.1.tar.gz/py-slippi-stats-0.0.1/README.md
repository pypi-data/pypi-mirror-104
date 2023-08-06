# py-slippi-stats

This program is an attempt at recreating the Slippi [stats](https://github.com/project-slippi/slippi-js/tree/master/src/stats) module of the original Slippi javascript package using [py-slippi](https://github.com/hohav/py-slippi). Most of it is just a translation of the slippi-js to python.

## Installation

1. Install the packages in requirements.txt with pip

        pip install -r requirements.txt

2. That's all!

## Usage

Here is a basic case of usage:

    import slippi
    import slippistats

    game = slippi.Game('mygame.slp')
    stats = slippistats.overall.getGameStats(game)

    print(stats)