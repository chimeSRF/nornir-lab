from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_title, print_result

nr = InitNornir(config_file="config.yaml", dry_run=True)

def vrf_configuration(task):
    r = task.run(task=template_file,
                 name="VRF Configuration",
                 template="vrf.j2",
                 path=f"templates/")

    task.host["config"] = r.result

    task.run(task=napalm_configure,
             name="Loading VRF Configurations on the device",
             replace=False,
             configuration=task.host["config"])

def interface_configuration(task):
    r = task.run(task=template_file,
                 name="Interface Configuration",
                 template="interfaces.j2",
                 path=f"templates/")

    task.host["config"] = r.result

    if task.host["config"]:
        task.run(task=napalm_configure,
                name="Loading Interface Configurations on the device",
                replace=False,
                configuration=task.host["config"])

def bgp_configuration(task):
    r = task.run(task=template_file,
                 name="BGP Configuration",
                 template="bgp.j2",
                 path=f"templates/")

    task.host["config"] = r.result

    if task.host["config"]:
        task.run(task=napalm_configure,
                name="Loading Interface Configurations on the device",
                replace=False,
                configuration=task.host["config"])

nr.data.dry_run = False
print_title("RUNNING VRF CONFIGURATIONS")
vrf_result = nr.run(task=vrf_configuration)
print_result(vrf_result)
print("\n\n")
print_title("RUNNING INTERFACE CONFIGURATIONS")
interface_result = nr.run(task=interface_configuration)
print_result(interface_result)
print("\n\n")
print_title("RUNNING BGP CONFIGURATIONS")
bgp_result = nr.run(task=bgp_configuration)
print_result(bgp_result)
