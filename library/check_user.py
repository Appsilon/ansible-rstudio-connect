#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import subprocess


def main():
    module_args = dict(
        name=dict(type='str', required=True),
        uid=dict(type='int', required=True),
        gid=dict(type='int', required=True),
    )

    module = AnsibleModule(argument_spec=module_args)

    name = module.params['name']
    uid = module.params['uid']
    gid = module.params['gid']

    try:
        command = ["getent", "passwd", name]
        result = subprocess.run(command, capture_output=True, text=True)
        stdout = result.stdout.strip()

        if result.returncode != 0:
            module.fail_json(msg="User not found")

        uid_from_passwd = int(stdout.split(":")[2])
        gid_from_passwd = int(stdout.split(":")[3])

        if uid_from_passwd != uid and gid_from_passwd != gid:
            module.fail_json(msg="UID and GID don't match")
        elif uid_from_passwd != uid:
            module.fail_json(msg="UID doesn't match")
        elif gid_from_passwd != gid:
            module.fail_json(msg="GID doesn't match")

        module.exit_json(msg="UID is valid")
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == '__main__':
    main()
