from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_title, print_result

nr = InitNornir(config_file="config.yaml", dry_run=True)

def run_configuration_task(task, task_name, template_name):
    r = task.run(task=template_file,
                 name=task_name,
                 template=template_name,
                 path=f"templates/")

    task.host["config"] = r.result

    if task.host["config"]:
        task.run(task=napalm_configure,
                name=f"Loading {task_name} on the device",
                replace=False,
                configuration=task.host["config"])

def vrf_configuration(task):
    run_configuration_task(task, "VRF Configuration", "vrf.j2")

def interface_configuration(task):
    run_configuration_task(task, "Interface Configuration", "interfaces.j2")

def bgp_configuration(task):
    run_configuration_task(task, "BGP Configuration", "bgp.j2")

nr.data.dry_run = False

for task_name, task_func in [("RUNNING VRF CONFIGURATIONS", vrf_configuration),
                             ("RUNNING INTERFACE CONFIGURATIONS", interface_configuration),
                             ("RUNNING BGP CONFIGURATIONS", bgp_configuration)]:
    print_title(task_name)
    result = nr.run(task=task_func)
    print_result(result)
    print("\n\n")
