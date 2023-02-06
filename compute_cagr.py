def compute_cagr(start_year, annual_rate, end_year):
    result = start_year * (1 + annual_rate) ** end_year
    return round(result, 2)

start_year = float(input("Enter start point balance: "))
annual_rate = float(input("Enter CAGR (e.g., .0375): "))
end_year = float(input("Enter end point year: "))

result = compute_cagr(start_year, annual_rate, end_year)
print('${:,.2f}'.format(result))
