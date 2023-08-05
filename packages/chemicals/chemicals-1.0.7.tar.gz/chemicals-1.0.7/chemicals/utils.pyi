# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from numpy import (
    float64,
    ndarray,
)
from typing import (
    Any,
    List,
    Optional,
    Tuple,
    Union,
)


def API_to_SG(API: float) -> float: ...


def CAS2int(i: Union[str, float, int]) -> int: ...


def Cp_minus_Cv(T: int, dP_dT: float, dP_dV: float) -> float: ...


def Joule_Thomson(T: int, V: float, Cp: float, dV_dT: Optional[float] = ..., beta: Optional[float] = ...) -> float: ...


def Parachor(MW: float, rhol: float, rhog: float, sigma: float) -> float: ...


def SG(rho: int, rho_ref: float = ...) -> float: ...


def SG_to_API(SG: float) -> float: ...


def Vfs_to_zs(Vfs: List[float], Vms: List[float]) -> List[float]: ...


def Vm_to_rho(Vm: float, MW: float) -> float: ...


def Watson_K(Tb: int, SG: float) -> float: ...


def Z(T: int, P: float, V: float) -> float: ...


def d2ns_to_dn2_partials(d2ns: List[List[float]], dns: List[float]) -> List[List[float]]: ...


def d2xs_to_d2xsn1(d2xs: List[List[float]]) -> List[List[float]]: ...


def dns_to_dn_partials(dns: List[float], F: float) -> List[float]: ...


def dxs_to_dn_partials(dxs: List[float], xs: List[float], F: float) -> List[float]: ...


def dxs_to_dns(dxs: List[float], xs: List[float]) -> List[float]: ...


def dxs_to_dxsn1(dxs: List[float]) -> List[float]: ...


def int2CAS(i: int) -> str: ...


def isentropic_exponent(Cp: float, Cv: float) -> float: ...


def isobaric_expansion(V: float, dV_dT: float) -> float: ...


def isothermal_compressibility(V: float, dV_dP: float) -> float: ...


def mix_component_flows(
    IDs1: List[str],
    IDs2: List[str],
    flow1: float,
    flow2: int,
    fractions1: List[float],
    fractions2: List[float]
) -> Tuple[List[str], List[float]]: ...


def mix_multiple_component_flows(
    IDs: List[List[str]],
    flows: List[int],
    fractions: List[List[float]]
) -> Tuple[List[str], List[float]]: ...


def mixing_logarithmic(fracs: List[float], props: List[float]) -> Optional[float]: ...


def mixing_power(fracs: List[float], props: List[float], r: int) -> float: ...


def mixing_simple(fracs: List[float], props: List[float]) -> Optional[float]: ...


def none_and_length_check(all_inputs: Any, length: Optional[int] = ...) -> bool: ...


def normalize(
    values: Union[List[float], List[Union[float, float64]], List[int], List[float]]
) -> Union[List[float64], List[float]]: ...


def os_path_join(*args) -> str: ...


def phase_identification_parameter(V: float, dP_dT: float, dP_dV: float, d2P_dV2: float, d2P_dVdT: float) -> float: ...


def phase_identification_parameter_phase(
    d2P_dVdT: float,
    V: Optional[float] = ...,
    dP_dT: Optional[float] = ...,
    dP_dV: Optional[float] = ...,
    d2P_dV2: Optional[float] = ...
) -> str: ...


def property_mass_to_molar(A_mass: float, MW: float) -> float: ...


def property_molar_to_mass(A_molar: int, MW: float) -> float: ...


def remove_zeros(
    values: Union[List[float], ndarray, List[float]],
    tol: float = ...
) -> Union[ndarray, List[float]]: ...


def rho_to_Vm(rho: float, MW: float) -> float: ...


def solve_flow_composition_mix(
    Fs: Union[List[Optional[float]], List[Optional[int]], List[float], List[Optional[float]]],
    zs: Union[List[None], List[Optional[float]]],
    ws: Union[List[Optional[float]], List[None]],
    MWs: List[float]
) -> Union[Tuple[List[float], List[float], List[float]], Tuple[List[float], List[float], List[float]]]: ...


def sorted_CAS_key(CASs: List[str]) -> Tuple[str, str, str, str]: ...


def speed_of_sound(V: float, dP_dV: float, Cp: float, Cv: float, MW: Optional[float] = ...) -> float: ...


def to_num(values: List[str]) -> Union[List[Optional[Union[str, float]]], List[Union[str, float]]]: ...


def v_molar_to_v(v_molar: float, MW: float) -> float: ...


def v_to_v_molar(v: int, MW: float) -> float: ...


def vapor_mass_quality(VF: float, MWl: int, MWg: int) -> float: ...


def ws_to_zs(ws: List[float], MWs: List[int]) -> List[float]: ...


def zs_to_Vfs(zs: List[float], Vms: List[float]) -> List[float]: ...


def zs_to_ws(zs: List[float], MWs: Union[List[int], List[float]]) -> List[float]: ...

__all__: List[str]