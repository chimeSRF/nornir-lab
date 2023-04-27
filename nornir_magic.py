from nornir import InitNornir
from getpass import getpass
from nornir_netmiko import netmiko_send_config
from nornir_utils.plugins.functions import print_result
import yaml

def configure_vrf(task, vrf):
    vrf_config = [
        f"vrf definition {vrf['name']}",
        f"  rd {vrf['id']}:0",
        f"  route-target export {vrf['route_export'][0]}",
        f"  route-target import {vrf['route_import'][0]}",
        "  address-family ipv4",
        "    exit-address-family",
        "  exit",
    ]

    commands = "\n".join(vrf_config)
    result = task.run(
        task=netmiko_send_config,
        config_commands=commands,
    )
    return result

def main():
    nr = InitNornir(config_file="config.yaml")
    nr.inventory.defaults.password = getpass("Password: ")

    with open("services.yaml", "r") as file:
        services = yaml.safe_load(file)["services"]

    for service in services:
        vrf = {
            "name": service["name"],
            "id": service["id"],
            "route_import": service["route_import"],
            "route_export": service["route_export"],
        }

        task = nr.run(task=configure_vrf, vrf=vrf)
        print_result(task)

if __name__ == "__main__":
    main()
