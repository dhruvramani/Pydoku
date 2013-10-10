Pydoku
======

A simple Python Package that solves a Sudoku via the command line;

Features
--------

- [x] Parsing command-line arguments;
- [x] Reading sudoku from:-
  - [x] terminal as:-
    - [x] formatted;
    - [x] letting you backspace (every 3 chars);
    - [ ] on Windows <http://stackoverflow.com/questions/3523174/raw-input-in-python-without-pressing-enter>;
  - [x] file (unformatted):-
    - [x] unformatted;
    - [ ] file as stdin;
  - [ ] internet source;
  - [ ] generating;
- [ ] Interacting with user;
- [x] Solving by:-
  - [x] Logic:-
    - [x] Reducing;
    - [x] Promoting;
  - [ ] Guessing;
  - [x] Finishing when done;
  - [x] using iteration instead of tail-recursion;
  - [ ] tracking time taken;
- Displaying:-
  - [x] through:-
    - [x] terminal;
    - [x] file;
    - [ ] GUI;
  - [x] as:-
    - [ ] formatted;
    - [ ] unformatted;
- [ ] Testing;
  - [ ] using function annotations (check syntax for iterable etc.);
  - [ ] Unit Tests;