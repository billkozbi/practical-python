import fileparse
import stock

def portfolio_cost(filename):
    '''
    Function for calculating portfolio cost
    filename - argument which provide path to the filename which is used to calculate portfolio cost
    '''
    with open(filename, mode='r') as file:
        portfolio = fileparse.parse_csv(
            file, types=[str, int, float], has_headers=True, select=['name', 'shares', 'price'])
    
    list_of_stocks = [ stock.Stock(name=e['name'], shares=e['shares'], price=e['price']) for e in portfolio ]

    return sum(r.cost() for r in list_of_stocks)


def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "/workspaces/practical-python/Work/Data/portfolio.csv"

    cost = portfolio_cost(filename)
    print(f'Total cost {cost:.2f}')


if __name__ == 'main':
    import sys
    main(sys.argv)
