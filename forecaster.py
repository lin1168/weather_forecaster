import argparse
import requests
import sys
from datetime import datetime, timedelta


def get_forecast_url(lat,lon):
    """Fetches the forecast URL for the given latitude and longitude."""
    url = f"https://api.weather.gov/points/{lat},{lon}"
    headers = {"User-Agent": "forecaster (your-email@example.com)"} # Change this email

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        city = data['properties']['relativeLocation']['properties']['city']
        state = data['properties']['relativeLocation']['properties']['state']
        forecast_url = data['properties']['forecastHourly']
        return forecast_url, f"{city}, {state}"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast URL: {e}", file=sys.stderr)
        sys.exit(1)


def get_hourly_forecast(forecast_url):
    """Fetches the hourly forecast from the given forecast URL."""
    headers = {"User-Agent": "forecaster (your-email@example.com)"} # Change this email

    try:
        response = requests.get(forecast_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['properties']['periods']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching hourly forecast: {e}", file=sys.stderr)
        sys.exit(1)


def format_forecast(forecast_data, interval, periods, location):
    """Formats and prints the forecast output."""
    print(f"Hourly forecast for {location}:\n")

    count = 0
    for i, period in enumerate(forecast_data):
        if i % interval == 0:
            time = datetime.fromisoformat(period['startTime']).strftime("%a %I %p")
            temperature = period['temperature']
            unit = period['temperatureUnit']
            description = period['shortForecast']
            print(f"{time}: {description}, {temperature}°{unit}.")
            count += 1
        if count >= periods:
            break


def main():
    parser = argparse.ArgumentParser(description="Fetch hourly weather forecasts from the National Weather Service API.")
    parser.add_argument("lat", type=float, help="Latitude of the location")
    parser.add_argument("lon", type=float, help="Longitude of the location")
    parser.add_argument("--interval", type=int, default=1, help="Interval in hours between forecasts (default: 1)")
    parser.add_argument("--periods", type=int, default=24, help="Number of forecast periods to display (default: 24)")
    args = parser.parse_args()

    forecast_url, location = get_forecast_url(args.lat, args.lon)
    forecast_data = get_hourly_forecast(forecast_url)
    format_forecast(forecast_data, args.interval, args.periods, location)


if __name__ == "__main__":
    main()
