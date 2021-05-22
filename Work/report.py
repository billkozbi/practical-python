import fileparse
import stock
import tableformat

def read_portfolio(filename):
    '''Returns list of Stock objects from filename'''

    with open(filename, mode='r') as file:
        portfolio = fileparse.parse_csv(file,
                                        select=['price', 'shares', 'name'],
                                        has_headers=True,
                                        types=[float, int, str],
                                        silence_errors=True)

    list_of_stocks = [ stock.Stock(name=e['name'], shares=e['shares'], price=e['price']) for e in portfolio ]
    return list_of_stocks


def read_prices(filename):
    '''Returns dictionary of {company, price} read from filename'''

    with open(filename, mode='r') as file:
        prices_list = fileparse.parse_csv(file,
                                        has_headers=False,
                                        types=[str, float],
                                        silence_errors=True)
    return dict(prices_list)


def make_report(portfolio, prices):
    report = []
    for e in portfolio:
        buy_price = e.price
        stock_name = e.name
        num_of_shares = e.shares
        current_price = prices[stock_name]
        change = (current_price - buy_price)
        row = (stock_name, num_of_shares, current_price, change)
        report.append(row)
    return report


def get_headers_string(headers):
    first_row = ""
    second_row = ""
    width = 10
    for h in headers:
        first_row += f"{h:>{width}} "
        second_row += "_"*width + " "
    return "\n".join((first_row, second_row))


def print_report(report, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'${price:.2f}', f'{change:.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''

    # read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # create a report
    report = make_report(portfolio, prices)

    # print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    num_of_args = len(argv) 
    if num_of_args < 3 or num_of_args > 4:
        raise SystemExit(
            "Usage: python report.py portfolio-file-name prices-file-name [format(txt, html, csv)]")

    if num_of_args == 3:
        portfolio_report(portfolio_filename=argv[1], prices_filename=argv[2])
    if num_of_args == 4:
        portfolio_report(portfolio_filename=argv[1], prices_filename=argv[2], fmt=argv[3])


if __name__ == "__main__":
    import sys
    main(sys.argv)
