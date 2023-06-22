# airline_delays

Calculate the percentage of security-caused flight delays for the United States by calendar year (e.g., 2004).

## Setup
### asdf
* Install [asdf](https://asdf-vm.com/guide/getting-started.html)
* Install python plugin for asdf
  * `asdf plugin add python`
* Install poetry plugin for asdf
  * `asdf plugin add poetry`

### poetry
* Install poetry
  * `asdf install poetry 1.4.2`

### python
* Install python 3.11.4
  * `asdf install python 3.11.4`
* Install virtual environment
    ```bash
    # virtual environment in the project directory
    poetry config virtualenvs.in-project true

    # create virtual environment
    poetry install
    ```

## Quickstart
```bash
# activate virtual environment
poetry shell

# run script
λ python main.py 
airlines.json already exists
Available years:
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
Enter a year: 2004
Average percentage of delayed flights: 7.93%
Average minutes delayed: 42.59 minutes

# force quit script if necessary
ctrl-c              # ^C

# deactivate virtual environment
deactivate
```

## Further Reading
[Airline Dataset](https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json)
