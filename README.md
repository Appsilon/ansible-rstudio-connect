# Ansible Role: rstudio-connect

[![CI](https://github.com/Appsilon/ansible-rstudio-connect/workflows/CI/badge.svg)](https://github.com/Appsilon/ansible-rstudio-connect/actions/workflows/ci.yml)

Set up (the latest version of) [RStudio Connect](https://www.rstudio.com/products/connect/) in Debian-like systems.

## Requirements

* `curl` (will be installed)
* `r-base` (will not be installed)

## Role Variables

* `rstudio_connect_version` [default: `1.9.0.1`]: Version to install
* `rstudio_connect_install` [default: `[]`]: Additional packages to install (e.g. `r-base`)

* `rstudio_connect_www_port` [default: `3939`]: The port you want RStudio Connect to listen on
* `rstudio_connect_www_address` [default: `0.0.0.0`]: The address you want RStudio to listen on

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
