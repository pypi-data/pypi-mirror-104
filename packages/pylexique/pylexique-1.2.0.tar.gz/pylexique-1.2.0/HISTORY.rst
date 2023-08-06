=======
History
=======

1.2.0 (2021-04-30)
------------------

* Added a new method to the class Lexique383. The method is Lexique383.get_lex() .
* This new method accepts either a single word as a string or an iterable of strings and will return the asked lexical information.
* Expanded sample usage of the software in the docs.
* Substantial update to the code and docs.
* Removed unneeded dependencies as I reimplement some functionality myself.

1.1.1 (2021-04-28)
------------------

* Added a new method to the class LexItem. The method is LexItem.to_dict() .
* This new method allows the LexItem objects to be converted into dicts with key/value pairs corresponding to the LexItem.
* This method allows easy display or serialization of the LexItem objects.
* Lexical Items having the same orthography are stored in a list at the word's orthography key to the LEXIQUE dict.
* Expanded sample usage of the software in the docs.
* Substantial update to the code and docs.

1.1.0 (2021-04-28)
------------------

* Drastically reduced dependencies by ditching HDF5 and bolcs as the package is now smaller, faster an easier to build.
* Lexical Items having the same orthography are stored in a list at the word's orthography key to the LEXIQUE dict.
* Implemented the "FlyWheel" pattern for light Lexical entries rsiding entirely in memory at run time.
* Added sample usage of the software in the docs.
* General update to the code and docs.

1.0.7 (2021-04-27)
------------------

* First release on PyPI.
