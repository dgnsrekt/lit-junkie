# lit-junkie
The first step is admitting you have an addiction to reading.

```
         ,..........   ..........,
     ,..,'          '.'          ',..,
    ,' ,'            :            ', ',
   ,' ,'             :             ', ',
  ,' ,'              :              ', ',
 ,' ,'............., : ,.............', ',
,'  '............   '.'   ............'  ',
 '''''''''''''''''';''';''''''''''''''''''
                    '''
```

## Application Requirements 
- [x] Type in a query and display a list of **5** books matching that query.
- [x] Each item in the list should include the book's **author**, **title**, and **publishing company**.
- [x] A **user** should be able to select a book from the **five** displayed to **save** to a “Reading List”
- [x] View a “Reading List” with all the books the user has selected from their queries.
- [x] **Reading List** is a local reading list and not tied to Google Books’s account features.
- [x] Feel free to use a library (or not) for the Google Books call or JSON parsing.

## Application Improvements
- [] Correct application error when no match is found on the Google Books API. Example 'dafbohdfb'. Add tests.
- [] Remove 'CTRL-C'. Add UI Friendly graceful exit.

## Watch it run
[![asciicast](https://asciinema.org/a/457883.svg)](https://asciinema.org/a/457883)

## Install and run with Poetry

```bash
git clone https://github.com/dgnsrekt/lit-junkie.git

cd lit-junkie

poetry install

poetry run python3 runner.py
```

## Run tests with pytest
```bash
pytest

```

## Install and run in a Virtual Env without Poetry
```bash
git clone https://github.com/dgnsrekt/lit-junkie.git

cd lit-junkie

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 runner.py
```

