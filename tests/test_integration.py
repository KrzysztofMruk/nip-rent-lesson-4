from src.models import Apartment
from src.manager import Manager
from src.models import Parameters


def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key


def test_all_tenants_from_json_are_loaded():
    parameters = Parameters()
    manager = Manager(parameters)
    tenant_names = [
        "Jan Nowak",
        "Adam Kowalski",
        "Ewa Adamska",
    ]
    manager_tenant_names = [tenant.name for tenant in manager.tenants.values()]

    for tenant_name in tenant_names:
        assert tenant_name in manager_tenant_names
