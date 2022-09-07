# Ansible Role: rstudio-connect

[![CI](https://github.com/Appsilon/ansible-rstudio-connect/workflows/CI/badge.svg)](https://github.com/Appsilon/ansible-rstudio-connect/actions/workflows/ci.yml)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-appsilon.rstudio_connect-blue.svg)](https://galaxy.ansible.com/appsilon/rstudio_connect/)

Set up (the latest version of) [RStudio Connect](https://www.rstudio.com/products/connect/) in Debian-like systems.

## Requirements

* `curl` (will be installed)
* `r-base` (will not be installed)

## Role Variables

* `rstudio_connect_version` [default: `1.9.0.1`]: Version to install
* `rstudio_connect_install` [default: `[]`]: Additional packages to install (e.g. `r-base`)
* `rstudio_connect_www_port` [default: `3939`]: The port you want RStudio Connect to listen on
* `rstudio_connect_config`: A map of maps containing RStudio Connect configuration. Gets converted into Golang's configuration file (GCFG) and is writted on down to `rstudio-connect.gcfg`. See [default](./defaults/main.yml) for an example.
* `rstudio_connect_config_override` [default: `""`]: If you know what you're doing, you can override whole `rstudio-connect.gcfg` config.
* `rstudio_connect_license`: If specified, RStudio Connect will attempt to activate the supplied license key.
* `rstudio_connect_enable_python` [default: `false`]: If specified, the configuration file will contain Python section with Enabled set to `true`.
* `rstudio_connect_python_executables` [default: `[]`]: List of paths to Python executables (e.g. `[/opt/python/3.10.6/bin/python3]`). Additional Python versions can be installed with [ansible-python-install role](https://github.com/Appsilon/ansible-python-install). If this list is empty, the role will search for Python executables in `python_main_directory`. Result of the searching can be filtered with `python_versions` (only matching versions will be configured).

For the rest of the default variables, see
[./defaults/main.yml](./defaults/main.yml).

## Dependencies

None

## Example

Basic configuration:

```yaml
---
- hosts: all
  roles:
    - appsilon.rstudio_connect
```

Playbook for installing additional Python versions with  [ansible-python-install](https://github.com/Appsilon/ansible-python-install) and configuring RStudio Connect to use them:

```yaml
---
- hosts: all
  become: true
  vars:
    python_versions:
      - 3.10.6
      - 3.7.8
      - 3.8.6
    rstudio_connect_enable_python: true
    rstudio_connect_install:
      - r-base
  roles:
    - appsilon.python_install
    - appsilon.rstudio_connect
```

## License

MIT

## Author Information

Oleksandr Ponomarov. Inspired by (aka shamelessly stolen from) [ansible-rstudio-server](https://github.com/Oefenweb/ansible-rstudio-server).
