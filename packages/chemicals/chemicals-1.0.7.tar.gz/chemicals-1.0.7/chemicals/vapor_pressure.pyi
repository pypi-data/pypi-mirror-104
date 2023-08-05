# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from pandas.core.frame import DataFrame
from typing import (
    Tuple,
    Union,
)


def Ambrose_Walton(T: float, Tc: float, Pc: float, omega: float) -> float: ...


def Antoine(T: float, A: float, B: float, C: float, base: float = ...) -> float: ...


def Antoine_AB_coeffs_from_point(T: float, Psat: float, dPsat_dT: float, base: float = ...) -> Tuple[float, float]: ...


def Antoine_coeffs_from_point(
    T: float,
    Psat: float,
    dPsat_dT: float,
    d2Psat_dT2: float,
    base: float = ...
) -> Tuple[float, float, float]: ...


def DIPPR101_ABC_coeffs_from_point(
    T: float,
    Psat: float,
    dPsat_dT: float,
    d2Psat_dT2: float
) -> Tuple[float, float, float]: ...


def Edalat(T: float, Tc: float, Pc: float, omega: float) -> float: ...


def Lee_Kesler(T: float, Tc: float, Pc: float, omega: float) -> float: ...


def Psat_IAPWS(T: float) -> float: ...


def Psub_Clapeyron(T: float, Tt: float, Pt: float, Hsub_t: float) -> float: ...


def Sanjari(T: float, Tc: float, Pc: float, omega: float) -> float: ...


def TRC_Antoine_extended(
    T: float,
    Tc: float,
    to: float,
    A: float,
    B: float,
    C: float,
    n: float,
    E: float,
    F: float
) -> float: ...


def Wagner(T: float, Tc: float, Pc: int, a: float, b: float, c: float, d: float) -> float: ...


def Wagner_original(T: float, Tc: float, Pc: float, a: float, b: float, c: float, d: float) -> float: ...


def __getattr__(name: str) -> DataFrame: ...


def boiling_critical_relation(T: float, Tb: float, Tc: float, Pc: float) -> float: ...


def dPsat_IAPWS_dT(T: float) -> float: ...


def load_vapor_pressure_dfs() -> None: ...

__all__: List[str]