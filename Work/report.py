import csv
import fileparse


def read_portfolio(filename):
    '''Returns list of dictionaries of every stock from filename'''

    with open(filename, mode='r') as file:
        portfolio = fileparse.parse_csv(file,
                                        select=['price', 'shares', 'name'],
                                        has_headers=True,
                                        types=[float, int, str],
                                        silence_errors=True)
    return portfolio


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
        buy_price = e['price']
        stock_name = e['name']
        num_of_shares = e['shares']
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


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(get_headers_string(headers))
    for name, shares, price, change in report:
        price = f"${price:.2f}"
        print(f"{name:>10s} {shares:10} {price:>10} {change:10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(
            "Usage: python report.py portfolio-file-name prices-file-name")

    portfolio_report(portfolio_filename=argv[1], prices_filename=argv[2])


if __name__ == "__main__":
    import sys
    main(sys.argv)
