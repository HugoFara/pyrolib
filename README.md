![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Aurel31/pyrolib)
[![GitHub issues](https://img.shields.io/github/issues/Aurel31/pyrolib)](https://github.com/Aurel31/pyrolib/issues)
[![Documentation Status](https://readthedocs.org/projects/pyrolib/badge/?version=latest)](https://pyrolib.readthedocs.io/en/latest/?badge=latest)
[![GitHub license](https://img.shields.io/github/license/Aurel31/pyrolib)](https://github.com/Aurel31/pyrolib/blob/main/LICENSE)


# `pyrolib`


`pyrolib` is a tool library for the [`Méso-NH/Blaze`](https://src.koda.cnrs.fr/mesonh/mesonh-code) model.
`pyrolib` provides python tools for the following purposes:

- Generation of the `FuelMap.nc` file by using a `Méso-NH` namelist and the initialisation file of a `Méso-NH/Blaze` run.
- FireFlux I exeprimental fire data processing.
- Development of numerical methods for the `Blaze fire model`.


## Installation

`pyrolib` requires Python `3.10` or newer. Install it from PyPI:

```bash
pip install pyrolib
```

Some operations on the fire mesh can be accelerated with `numba`, which is optional:

```bash
pip install pyrolib[numba]
```

## Usage

`pyrolib` is separated into several sub-libraries for each of the objectives mentioned above, respectively:

- `pyrolib.fuelmap`
- `pyrolib.data_processing`
- `pyrolib.blaze`

### Fuel database

`pyrolib` relies on a fuel container object called a `FuelDatabase`. A `FuelDatabase` is a 2 level nested dictionary-like class. The first level corresponds to an explicit fuel name (like "tall_grass"). This fuel can be described by several methods that are related to a rate of spread model (for example `Rothermel` or `Balbi`). Each description is related to a `Fuel class` (`RothermelFuel` or `BalbiFuel`) and constitutes the second level of the database.

The`FireFluxI` `FuelDatabase` contains for example the following:
```
* FireFluxI
    < tall_grass > available for:
      - BalbiFuel fuel class
```

The list of `FuelDatabase` contained in `pyrolib` can be accessed through the cli `pyrolib-fm list-fuel-databases`.

A user database can be saved in a `.yml` file. See example `examples/fuel_database`.

## `Méso-NH` compliance

The current version of `pyrolib` is compliant with `Méso-NH` from version `5.6.0` to version `6.1.0`.
The default is `6.1.0`; to target an older release, pass the version explicitly:

```python
FuelMap(fuel_db=my_db, MesoNHversion="5.6.0")
```

`Méso-NH` sources are hosted at <https://src.koda.cnrs.fr/mesonh/mesonh-code>.

## Acknowledgements

This library is part of the `ANR FireCaster` project (2017-2021, `ANR-16-CE04-0006, FIRECASTER`).
