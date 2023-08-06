# Lazy finance (lbud for "lazy budget")

[![PyPI version](https://badge.fury.io/py/lazy-budget.svg)](https://badge.fury.io/py/lazy-budget)

`lbud` aims to help building an easy, data-driven budget solution for personal use.

For examples of data, see `example-data/`.

## Setup

```bash
python3.9 -m pip install lazy-budget
```

## Files

To start using `lbud` to manage your budget,
you will need to create and
maintain at least 2 files. They are:

- `history.csv` - a CSV file that lists all of your financial operations. You may have one history file for all your budgets, history is filtered by budget period when performing calculations;
- `budget.yml` - a YAML file that describes a single budgeting period. It is advised to keep the period short, but i am sure `lbud` can handle however long budgets.

## Example usage

`budget.yaml`:

```yaml
total: 2000 # total amount of money to use
# the part of the total
# that you aim to keep this month
keep: 1500

# budgeting period
start: 2021-04-25
end: 2021-05-10

# currency is optional
# USD is the default and
# the operations themselves can
# specify the currency (lbud add "-10 CAD" taxi), as well
# as the config file and CLI options
currency: USD
```

`history.csv`:

```csv
-10,food,2021-04-26T00:00:00
-1.95,bubblegum,2021-04-27T17:20:31
-9.95,hot dog,2021-04-27T00:00:00
```

```bash
$ lbud ls
           today : 2021-05-02
      total days : 16
       days left : 8
 available / day : 31,25 USD
 CAN spend today : 228,10 USD
     spent today : 0,00 USD
 avg spent / day : 2,74 USD
            kept : 1 728,10 USD

$ lbud add -200 "club night"

$ cat history.csv  # added operation to history file
-10,food,2021-04-26T00:00:00
-1.95,bubblegum,2021-04-27T17:20:31
-9.95,hot dog,2021-04-27T00:00:00
-200,club night,2021-05-01T11:37:37.946058

$ lbud ls
                today : 2021-05-01
           total days : 16
            days left : 9
 days until can spend : 1
      available / day : 31,25 USD
   CANNOT spend today : 3,15 USD
          spent today : 200,00 USD
      avg spent / day : 31,70 USD
                 kept : 1 496,85 USD
```

## CLI help

**Note**: all the defaults can be pulled from a config file at `~/.lbudrc.yml`.
To override the location, specify `LBUDRC` environment variable.

```
usage: lbud [-h] [-f HISTORY_FILE] [-c BUDGET_FILE] [-L LOCALE] [-C CURRENCY]
            {add,a,new,n,ls,now,today,list,stats,s,get} ...

positional arguments:
  {add,a,new,n,ls,now,today,list,stats,s,get}
                        whether you want to add an expense or see statistics
    add (a, new, n)     add a new financial operation
    ls (now, today, list, stats, s, get)
                        list statistics

optional arguments:
  -h, --help            show this help message and exit
  -f HISTORY_FILE, --history-file HISTORY_FILE
                        history file to use (default is
                        ./history.csv)
  -c BUDGET_FILE, --budget-file BUDGET_FILE
                        budget file to use (default is
                        ./budget.yml)
  -L LOCALE, --locale LOCALE
                        locale to use (default is system locale)
  -C CURRENCY, --currency CURRENCY
                        default currency to use in uncertain situations (default is USD)
```

# My Usage

I have added a lot of configuration options to `lbud`
(CLI arguments, config file, the defaults) and since I am using it
in a very specific way, it might not work for you. Feel free to [submit a ticket](https://gitlab.com/oleksandr.zelentsov/lazy-finance/-/issues/new) or a pull request
(idk if it works, i'm new to this, post a ticket about it too).

Now I'm posting the way I'm using it for clarity:

- budget/history files at `~/finances/`
- config file at `~/.lbudrc.yml`:
  ```
  history_file: /Users/oleksandr/finances/history.csv
  budget_file: /Users/oleksandr/finances/budget.yml
  locale: pl_PL
  currency: PLN
  ```
- `lbud ls` or `lbud add` anywhere
