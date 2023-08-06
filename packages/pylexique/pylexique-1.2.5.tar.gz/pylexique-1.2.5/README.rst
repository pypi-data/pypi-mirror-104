=========
pylexique
=========


.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
        :target: https://GitHub.com/SekouDiaoNlp/pylexique/graphs/commit-activity
        :alt: Package Maintenance Status

.. image:: https://img.shields.io/badge/maintainer-SekouDiaoNlp-blue
        :target: https://GitHub.com/SekouDiaoNlp/pylexique
        :alt: Package Maintainer

.. image:: https://img.shields.io/github/checks-status/SekouDiaoNlp/pylexique/master?label=Build%20status%20on%20Windows%2C%20MacOs%20and%20Linux
        :target: https://img.shields.io/github/checks-status/SekouDiaoNlp/pylexique/master
        :alt: GitHub branch checks state

.. image:: https://img.shields.io/pypi/v/pylexique.svg
        :target: https://pypi.python.org/pypi/pylexique
        :alt: Python Package Index

.. image:: https://anaconda.org/conda-forge/pylexique/badges/version.svg
        :target: https://anaconda.org/conda-forge/pylexique
        :alt: Anaconda Package Index Status

.. image:: https://img.shields.io/pypi/pyversions/pylexique
        :target: https://pypi.python.org/pypi/pylexique
        :alt: Compatible Python versions

.. image:: https://img.shields.io/conda/pn/conda-forge/pylexique?color=dark%20green&label=Supported%20platforms
        :target: https://anaconda.org/conda-forge/pylexique
        :alt: Supported platforms

.. image:: https://readthedocs.org/projects/pylexique/badge/?version=latest
        :target: https://pylexique.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/SekouDiaoNlp/pylexique/shield.svg
     :target: https://pyup.io/repos/github/SekouDiaoNlp/pylexique/
     :alt: Updates



Pylexique is a Python wrapper around Lexique83_.

It allows to extract lexical information from more than 140 000 French words in an Object Oriented way.

Each lexical item is represented in a LexItem having the following LexEntryType:

.. code-block:: python

        class LexEntryTypes:
        """
        Type information about all the lexical attributes in a LexItem object.

        """
        ortho: str
        phon: str
        lemme: str
        cgram: str
        genre: str
        nombre: str
        freqlemfilms2: float
        freqlemlivres: float
        freqfilms2: float
        freqlivres: float
        infover: str
        nbhomogr: int
        nbhomoph: int
        islem: bool
        nblettres: int
        nbphons: int
        cvcv: str
        p_cvcv: str
        voisorth: int
        voisphon: int
        puorth: int
        puphon: int
        syll: str
        nbsyll: int
        cv_cv: str
        orthrenv: str
        phonrenv: str
        orthosyll: str
        cgramortho: str
        deflem: float
        defobs: int
        old20: float
        pld20: float
        morphoder: str
        nbmorph: int

The meanings of the attributes of this object are as follow:

* ortho: the word
* phon: the phonological forms of the word
* lemme: the lemmas of this word
* cgram: the grammatical categories of this word
* genre: the gender
* nombre: the number
* freqlemfilms: the frequency of the lemma according to the corpus of subtitles (per million occurrences)
* freqlemlivres: the frequency of the lemma according to the body of books (per million occurrences)
* freqfilms: the frequency of the word according to the corpus of subtitles (per million occurrences)
* freqbooks: the frequency of the word according to the body of books (per million occurrences)
* infover: modes, tenses, and possible people for verbs
* nbhomogr: number of homographs
* nbhomoph: number of homophones
* islem: indicates if it is a lemma or not
* nbletters: the number of letters
* nbphons: number of phonemes
* cvcv: the orthographic structure
* p-cvcv: the phonological structure
* voisorth: number of orthographic neighbors
* voisphon: number of phonological neighbors
* puorth: point of spelling uniqueness
* puphon: point of phonological uniqueness
* syll: syllable phonological form
* nbsyll: number of syllables
* cv-cv: syllable phonological structure
* orthrenv: reverse orthographic form
* phonrenv: reversed phonological form
* orthosyll: syllable orthographic form


You can find all the relevant information in the `official documentation of Lexique83`_

* Free software: MIT license
* Documentation: https://pylexique.readthedocs.io.


Features
--------

* Extract all lexical information from a French  word.
* Easy to use Api.
* Easily integrate pylexique in your own projects as an imported library.
* Can be used as a command line tool.

Credits
-------

Main developer SekouDiaoNlp_.

Lexical corpus: Lexique83_

About Lexique383:
=================

Lexique3
========

Lexique 3.83 est une base de données lexicales du français qui fournit
pour ~140000 mots du français: les représentations orthographiques et
phonémiques, les lemmes associés, la syllabation, la catégorie
grammaticale, le genre et le nombre, les fréquences dans un corpus de
livres et dans un corpus de sous-titres de filems, etc.

Table: `Lexique383.zip`_

Web site: http://www.lexique.org

Online: http://www.lexique.org/shiny/lexique

Publications
------------

-  New, Boris, Christophe Pallier, Marc Brysbaert, and Ludovic Ferrand.
   2004. "Lexique 2: A New French Lexical Database." *Behavior Research
   Methods, Instruments, & Computers* 36 (3): 516--524. `pdf`_

-  New, Boris, Christophe Pallier, Ludovic Ferrand, and Rafael Matos.
   2001. "Une Base de Données Lexicales Du Français Contemporain Sur
   Internet: LEXIQUE" *L'Année Psychologique* 101 (3): 447--462.
   `pdf <New%20et%20al.%20-%202001%20-%20Une%20base%20de%20données%20lexicales%20du%20français%20contempo.pdf>`__

-  Boris New, Marc Brysbaert, Jean Veronis, and Christophe Pallier.
   2007. "The Use of Film Subtitles to Estimate Word Frequencies."
   Applied Psycholinguistics 28 (4): 661--77.
   https://doi.org/10.1017/S014271640707035X.
   (`pdf <New.Brysbaert.Veronis.Pallier.2007.APU.pdf>`__)

Contributors
------------

-  Boris New & Christophe Pallier
-  Ronald Peereman
-  Sophie Dufour
-  Christian Lachaud
-  and many others... (contact us to be listed)

License
-------

`CC BY SA40.0`_

.. _Lexique383.zip: http://www.lexique.org/databases/Lexique382/Lexique383.zip
.. _pdf: New%20et%20al.%20-%202004%20-%20Lexique%202%20A%20new%20French%20lexical%20database.pdf
.. _CC BY SA40.0: LICENSE-CC-BY-SA4.0.txt


BibTex Entry to cite publications about Lexique383:


.. code:: bibtex

    @article{npbf04,
    author = {New, B. and Pallier, C. and Brysbaert, M. and Ferrand, L.},
    journal = {ehavior Research Methods, Instruments, & Computers},
    number = {3},
    pages = {516-524},
    title = {Lexique 2 : A New French Lexical Database},
    volume = {36},
    year = {2004},
    eprint = {http://www.lexique.org/?page_id=294},
    }

.. code:: bibtex

    @article{npfm01,
    author = {New, B. and Pallier, C. and Ferrand, L. and Matos, R.},
    journal = {L'Ann{\'e}e Pschologique},
    number = {447-462},
    pages = {1396-2},
    title = {Une base de donn{\'e}es lexicales du fran\c{c}ais contemporain sur internet: LEXIQUE},
    volume = {101},
    year = {2001},
    }

.. code:: bibtex

    @article{new_brysbaert_veronis_pallier_2007,
    author={NEW, BORIS and BRYSBAERT, MARC and VERONIS, JEAN and PALLIER, CHRISTOPHE},
    title={The use of film subtitles to estimate word frequencies},
    volume={28}, DOI={10.1017/S014271640707035X},
    number={4}, journal={Applied Psycholinguistics},
    publisher={Cambridge University Press},
    year={2007},
    pages={661–677}}

.. _Lexique83: http://www.lexique.org/
.. _SekouDiaoNlp: https://github.com/SekouDiaoNlp
.. _`official documentation of Lexique83`: http://lexique.org/_documentation/Manuel_Lexique.3.2.pdf
