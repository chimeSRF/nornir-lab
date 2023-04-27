from getpass import getpass
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_rich.functions import print_result
from nornir_netmiko.tasks.netmiko_send_command import netmiko_send_command

def ping(task: Task) -> Result:
    show_interface = task.run(
        netmiko_send_command,command_string="sh ip interface gi1 | inc Routing/Forwarding",
    )
    vrf = show_interface.result.split('"')[1]
    result = task.run(netmiko_send_command, command_string=f"ping vrf {vrf} 1.1.1.1")
    success = "!!!!" in result.result
    return Result(host=task.host, result=f"{vrf=}\n{success=}", failed=not success)

nr = InitNornir(config_file="config.yaml")
nr.inventory.defaults.password = getpass("Password: ")
result = nr.filter(platform="ios").run(ping)
print_result(result)