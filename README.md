# Geotechnical Parameters API
Generate your own random data points for writing proof of concept big data / data science applications.

## Introduction
This simple API is used to generate random data sample points commonly used in geotechnical instrumentation and monitoring. Many times when writing big data or data science applications, it is difficult to find public datasets on geotechnical I&M results given that most large projects have tight confidentiality agreements in place. This basic API generates some random data points (with a certain amount of realism) to help with writing proof of concept applications.

## Use
There are a few endpoints for this API, as listed below. The base URL `https://geotech-api.herokuapp.com/` has not been included in the table below, so make sure you insert that in before hitting go!

| Endpoint Ref | Endpoint URL                   | Description                                                                                           |
| ------------ | ------------------------------ | ----------------------------------------------------------------------------------------------------- |
| 1            | `ping/`                        | Test your connection and if the API is working as intended.                                           |
| 2            | `params/water_standpipe/`      | Generate a random number of sampling points from multiple water standpipes.                           |
| 3            | `params/pore_pressure/`        | Generate a random number of sampling points from multiple piezometers.                                |
| 4            | `params/settlement/{x, y, z}/` | Generate a random number of sampling points from multiple settlement markers in the x/y/z directions. |
| 5            | `params/all/`                  | Generate a response with all 5 monitoring types in one response object.                               |

## Schema
The following subsections provide examples of the different structures of each request. Where `...` exists, it means that the list is continued with different instances of the same data object within the list.

### `ping/`

```json
{
    "ping": "pong!"
}
```

### `params/water_standpipe/`

```json
{
    "request_type": "water_standpipe", 
    "length": 127, 
    "units": "water level (m)", 
    "timezone": "UTC", 
    "items": [
        {
            "borehole_number": "BH-9037", 
            "surface_level": 85.4, 
            "northing": 5814941, 
            "easting": 323796, 
            "reading": 86.25, 
            "timestamp": "2022-04-15T22:01:29.078Z"
        }, 
        ...
    ]
}
```

### `params/pore_pressure/`
Pore pressure, `pwp` is measured in `kPa`.

```json
{
    "request_type": "piezometer", 
    "length": 56, 
    "units": "pressure (kPa)", 
    "timezone": "UTC", 
    "items": [
        {
            "borehole_number": "BH-9483", 
            "surface_level": 82.33, 
            "northing": 5810968, 
            "easting": 322179, 
            "reading": 113.96, 
            "timestamp": "2022-04-15T22:06:38.737Z"
        }, 
        ....
    ]
}
```

### `settlement/{x, y, z}/`
Displacement, `displacement` is measured in `mm`. Whether the `x`, `y`, or `z` endpoint is used, the resulting schema is the same - with the exception of the direction.

```json
{
    "request_type": "settlement marker (x-direction)", 
    "length": 70, 
    "units": "displacement (mm)", 
    "timezone": "UTC", 
    "items": [
        {
            "borehole_number": "BH-1405", 
            "surface_level": 77.25, 
            "northing": 5811792, 
            "easting": 317017, 
            "reading": -28.7, 
            "timestamp": "2022-04-15T22:11:16.923Z"
        }, 
        ...
    ]
}
```

### `params/all/`
This is just a collection of all monitoring points, in the same structure as their individual component objects.

```json
{
    "request_type": "all_instruments", 
    "total_length": 553, 
    "standpipe_data": 
        {
            "request_type": "water_standpipe", 
            "length": 89, 
            "units": "water level (m)", 
            "timezone": "UTC", 
            "items": [...]
        },
    "piezometer_data":
        {
            "request_type": "piezometer", 
            "length": 56, 
            "units": "pressure (kPa)", 
            "timezone": "UTC", 
            "items": [...]
        },
    "settlement_x_data":
        {
            "request_type": "settlement marker (x-direction)", 
            "length": 70, 
            "units": "displacement (mm)", 
            "timezone": "UTC", 
            "items": [...]
        },
    "settlement_y_data": {...},
    "settlement_z_data": {...}
}
```

## Design & Implementation
This API was created using `Django` and backed by a `Postgresql` database. The application was containerized using `Docker` and deployed on `Heroku`.
