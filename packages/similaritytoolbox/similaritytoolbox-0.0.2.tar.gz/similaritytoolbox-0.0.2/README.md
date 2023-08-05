# Similarity toolbox

## Intro

    Toolbox that can be used to find similar setences

Tecnologies used
    * Contrastive tension   https://github.com/FreddeFrallan/Contrastive-Tension
    * Faiss                 https://github.com/facebookresearch/faiss
    * (Transformers/BERT)

## Version history

0.0.1   Draft



## Installation

pip install similaritytoolbox



## Usage

    toolbox = SimilarityToolbox()
    toolbox.add_sentence("kaka")
    toolbox.print_similar("bulle",limit = 5)



## Release

    rm -Rf dist/
    Step up version in setup.py
    python3 setup.py sdist bdist_wheel
    python3 -m twine upload dist/*
    Username: horndahl