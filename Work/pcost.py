import sys
import fileparse

def portfolio_cost(filename):
    '''
    Function for calculating portfolio cost
    filename - argument which provide path to the filename which is used to calculate portfolio cost
    '''

    portfolio = fileparse.parse_csv(filename, types=[int, float], has_headers=True, select=['shares', 'price'])

    return sum(r['shares'] * r['price'] for r in portfolio)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "/workspaces/practical-python/Work/Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')