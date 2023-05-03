# Repository README.md
This repository contains a network automation project using Nornir and Jinja2 to configure various network devices. The project automates the configuration of VRFs, interfaces, and BGP across multiple network devices.

## TODOs
- Currently not editing vrfs (delete not implemented)

## Table of Contents
[Initial Setup](#initial-setup) \
[File Structure](#file-structure) \
[Usage](#usage)

## Initial Setup
To get started with this project, follow these steps to set up your environment on a fresh Linux distribution:

1. Install Python (version 3.6 or higher is recommended):
```sh
sudo apt update
sudo apt install python3 python3-pip
```

2. Clone the repository:
```sh
git clone https://gitlab.ost.ch/ins-stud/NetAut/fs23/group04/lab-1-nornir.git
cd your-repo-folder
```

3. Install the required Python packages:
```sh
pip3 install -r requirements.txt
```

4. Update the inventory files in the inventory folder with your network devices and credentials.

## File Structure
The repository is organized as follows:
```sh
├── README.md
├── config.yaml
├── inventory
│   ├── defaults.yaml
│   ├── groups.yaml
│   └── hosts.yaml
├── nornir_magic.py
├── requirements.txt
├── services.yaml
└── templates
    ├── bgp.j2
    ├── interfaces.j2
    └── vrf.j2
```
- `config.yaml` - The Nornir configuration file.
- `inventory` - The folder containing the inventory files.
    - `defaults.yaml` - The file containing default values for the inventory.
    - `groups.yaml` - The file containing the definition of device groups.
    - `hosts.yaml` - The file containing the definition of devices.
- `nornir_magic.py` - The main Python script that uses Nornir to generate and push configurations.
- `requirements.txt` - The list of Python packages required for the project.
- `services.yaml` - The file containing service definitions.
- `templates` - The folder containing Jinja2 templates for generating configurations.
    - `bgp.j2` - The template for generating BGP configurations.
    - `interfaces.j2` - The template for generating interface configurations.
    - `vrf.j2` - The template for generating VRF configurations.

## Usage
1. Update the inventory files (`hosts.yaml` and `groups.yaml`) in the inventory folder with the appropriate network devices and credentials.

2. Edit the Jinja2 templates (`bgp.j2`, `interfaces.j2`, and `vrf.j2`) in the templates folder to match your network requirements.

3. Run the `nornir_magic.py` script to generate and push the configurations to your network devices:

```py
python3 nornir_magic.py
```
The script will execute each task (VRF, interface, and BGP configurations) sequentially and display the results.