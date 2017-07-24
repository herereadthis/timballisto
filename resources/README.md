# Resources

## File Templates

Put these files in your `~` home directory

```bash
cd ~
```

* [.bash_aliases](https://github.com/herereadthis/lutra/blob/master/resources/.bash_aliases) - aliases and shortcuts for terminal
* [.pypirc](https://github.com/herereadthis/lutra/blob/master/resources/.pypirc) - authentication for distributing packages to PyPi
* Remember to lock down the `.pypirc` file.

```bash
chmod 600 ~/.pypirc
```

## Configuration Files

* /etc/[modules](https://github.com/herereadthis/lutra/blob/master/resources/modules) - loading kernal drivers (enables I2C, SPI, etc.)

## Other Useful files

* [secret.json](https://github.com/herereadthis/lutra/blob/master/resources/secret.json) - provides all authentication for Lutra projects
* Remember to store `secret.json` one level above this repository. Never store keys in directories with version control.