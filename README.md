# Ansible Role: rstudio-connect

[![CI](https://github.com/Appsilon/ansible-rstudio-connect/workflows/CI/badge.svg)](https://github.com/Appsilon/ansible-rstudio-connect/actions/workflows/ci.yml)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-shmileee.rstudio_connect-blue.svg)](https://galaxy.ansible.com/shmileee/rstudio_connect/)

Set up (the latest version of) [RStudio Connect](https://www.rstudio.com/products/connect/) in Debian-like systems.

## Requirements

* `curl` (will be installed)
* `r-base` (will not be installed)

## Role Variables

* `rstudio_connect_version` [default: `1.9.0.1`]: Version to install
* `rstudio_connect_install` [default: `[]`]: Additional packages to install (e.g. `r-base`)
* `rstudio_connect_www_port` [default: `3939`]: The port you want RStudio Connect to listen on
* `rstudio_connect_config_override` [default: `""`]: If you know what you're doing, you can override or add to any of `rstudio-connect.gcfg` config options.
* `rstudio_connect_license`: If specified, RStudio Connect will attempt to activate the supplied license key.

For the rest of the default variables, see
[./defaults/main.yml](./defaults/main.yml).

## Dependencies

None

## Example

```yaml
---
- hosts: all
  roles:
    - rstudio-connect
```

## License

MIT

## Author Information

Oleksandr Ponomarov. Inspired by (aka shamelessly stolen from) [ansible-rstudio-server](https://github.com/Oefenweb/ansible-rstudio-server).
