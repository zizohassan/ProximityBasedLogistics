# ProximityBasedLogistics API

ProximityBasedLogistics is a Python-based API that uses the Nearest Neighbors algorithm to assign packages to drivers based on their proximity. The API is served using the CherryPy framework.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- CherryPy
- scikit-learn

You can install the necessary packages using pip:

```
pip install cherrypy scikit-learn
```

### Running the API

To start the API, navigate to the directory containing the project files and run the main Python file:

```
python main.py
```

This will start the API server at `http://0.0.0.0:8080`.

## Using the API

Send a POST request to the root route ("/") of the server with a JSON payload. The payload should have two keys: `package_locations` and `driver_locations`. The value for each key should be an array of arrays, where each subarray represents the [lat, lng] coordinates for a package or driver.

Example payload:

```json
{
  "package_locations": [[41.878113, -87.629799], [29.760427, -95.369804]],
  "driver_locations": [[40.712776, -74.005974], [34.052235, -118.243683]]
}
```

The API will return a JSON object with a single key 'result'. The value for 'result' will be an array of strings, each string indicating which driver was assigned to which package.

Example response:

```json
{
  "result": [
    "Package 1 is assigned to driver 2",
    "Package 2 is assigned to driver 1"
  ]
}
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

---

Remember to create and link a `LICENSE.md` file if you mention it in your README. If you don't want to include a license, you can remove that section.
