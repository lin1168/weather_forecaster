# Weather Forecaster

This script fetches and displays hourly weather forecasts from the National Weather Service API.

## Features
- Retrieves hourly forecasts based on latitude and longitude.
- Displays temperature, forecast description, and timing.
- Allows customization of forecast intervals and number of periods to display.

## Prerequisites
- Python 3.x
- `requests` library (install via `pip install requests`)

## Installation
Clone the repository and navigate to the project directory:

```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

## Usage

Run the script with the required latitude and longitude:
```bash
python forecast.py <latitude> <longitude> [--interval INTERVAL] [--periods PERIODS]
```

Example:
```bash
python forecast.py 40.4406 -79.9959 --interval 2 --periods 12
```
This fetches a 12-hour forecast for Pittsburgh, PA with a 2-hour interval between each entry.

## Arguments
| Argument       | Description                                      | Default |
|---------------|--------------------------------------------------|---------|
| `lat`         | Latitude of the location                        | N/A     |
| `lon`         | Longitude of the location                       | N/A     |
| `--interval`  | Interval in hours between forecasts             | 1       |
| `--periods`   | Number of forecast periods to display           | 24      |


## Example Output 
```
Hourly forecast for Pittsburgh, PA:

Mon 08 AM: Cloudy, 32°F.
Mon 10 AM: Partly Sunny, 34°F.
Mon 12 PM: Mostly Sunny, 36°F.
...
```

## API Information
This script uses the National Weather Service API (https://www.weather.gov/documentation/services-web-api). A custom User-Agent header is required to comply with API guidelines.

### Important: Update the User-Agent Header
Before using the script, update the `User-Agent` header with your own email in `forecast.py`:

```python
headers = {"User-Agent": "forecaster (your-email@example.com)"}  # Change this email
```

## Error Handling
* If the API request fails, an error message is displayed and the script exits.
* Invalid latitude/longitude values will result in an API error.
