def getMonths(start: str, end: str):
    start_year, start_month = map(int, start.split('-'))
    end_year, end_month = map(int, end.split('-'))

    months = []

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if year == start_year and month < start_month:
                continue
            if year == end_year and month > end_month:
                break
            months.append(f"{year}-{month:02d}")

    return months
