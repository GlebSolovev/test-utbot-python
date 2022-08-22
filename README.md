# UTBot-Python testing

This repository contains the code for testing [UTBot-Python](https://github.com/UnitTestBot/UTBotJava/tree/utbot-python).
Unfortunately, it has to be done manually: i.e. run the product on each file / project and check the quality of the
result.

## Synthetic examples

Synthetic examples are created manually to test specific cases. You can find them in `synthetic` folder.

* In the `functional` subdirectory, you can find tests that check the support for all kinds of types.
* The `type_inference` subdirectory contains code that can be used to check the correctness and power of type inference
  when there are no annotations ot they are insufficient or complex.
* In the `fuzzing` subdirectory, you can check the quality of fuzzing, namely, how varied and covering values it
  manages to provide.

## Real projects

Real projects allow you to evaluate the quality of the product for the target audience.

### Beginners

Directory `beginners` contains programs that cover basic algorithms, utility functions, work with collections and
files &mdash; that is, what beginners most often look for on the Internet and practice writing. Also, the code is poorly
written and not annotated, just in line with the scenario. Examples are taken
from [here](https://www.geeksforgeeks.org/python-programming-examples/).

### Machine Learning

* [Text-Multi-Style-Transfer-Through-Activation-Maximization](https://github.com/GlebSolovev/Text-Multi-Style-Transfer-Through-Activation-Maximization):
  a deep learning educational project that uses a large number of repositories with serious classifiers.
* [How-Positive-Are-You-Text-Style-Transfer-using-Adaptive-Style-Embedding](https://github.com/kinggodhj/How-Positive-Are-You-Text-Style-Transfer-using-Adaptive-Style-Embedding):
  one of the classifiers that is used in the project from above. Contains a lot of errors!

### Web

* [web-2021](https://github.com/GlebSolovev/web-2021): an educational `FastAPI` project that uses a variety of
  technologies (for example: `GraphQL`, `SQLite`). The complexity of the code can be adjusted depending on the branch.
  In
  addition, the project is already well covered with the tests.

### Amateur

* [Python-2022](https://github.com/GlebSolovev/Python-2022): a homework repository for the advanced Python course. It
  covers topics ranging from AST parsing to inter-process communication and scrapping.

### Science

* [Annotator-for-Antibody-Sequences](https://github.com/GlebSolovev/Annotator-for-Antibody-Sequences): a school
  bioinformatics project with very simple and bad code &mdash; perfectly simulates the case of a non-programming
  scientist.
* [2-svd-GlebSolovev](https://github.com/cs-compmath-2022/2-svd-GlebSolovev): a tutorial project on implementing various
  SVD decomposition methods. It actively uses mathematical libraries. Unfortunately, it is private and can only be used
  by the author.
