# Lazy finance (lbud for "lazy budget")

This project aims to help building an easy budget solution for personal use.

For examples of data, see `example-data/`.

# Help

```
usage: lbud [-h] [-f HISTORY_FILE] [-c BUDGET_FILE] [-L LOCALE]
            [-C CURRENCY]
            {add,a,new,n,ls,now,today,list,stats,s,get} ...

positional arguments:
  {add,a,new,n,ls,now,today,list,stats,s,get}
                        whether you want to add an expense or
                        see statistics
    add (a, new, n)     add a new financial operation
    ls (now, today, list, stats, s, get)
                        list statistics

optional arguments:
  -h, --help            show this help message and exit
  -f HISTORY_FILE, --history-file HISTORY_FILE
                        history file to use (default is
                        /Users/oleksandr/Programs/lazy-
                        finance/example-data/history.csv)
  -c BUDGET_FILE, --budget-file BUDGET_FILE
                        budget file to use (default is
                        /Users/oleksandr/Programs/lazy-
                        finance/example-data/budget.yml)
  -L LOCALE, --locale LOCALE
                        locale to use (default is pl_PL)
  -C CURRENCY, --currency CURRENCY
                        default currency to use in uncertain
                        situations (default is PLN)
```
