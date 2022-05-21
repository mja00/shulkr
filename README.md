# Shulkr

![Check New Commits](https://github.com/clabe45/shulkr/actions/workflows/check.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/shulkr.svg)](https://badge.fury.io/py/shulkr)

Shulkr is a tool that decompiles multiple versions of Minecraft and commits each
version to Git

**Warning: You CANNOT publish any code generated by this tool. For more info,
see the [usage guidelines].**

## No Log4j Vulnerabilities Found

The decompiler has been scanned for the recent log4j vulnerabilities, including
CVE-2021-44228, CVE-2021-45046, CVE-2021-45105, and CVE-2021-44832, and none
were present.

## Requirements

- Git
- Python 3
- JDK (>= 17 for Minecraft 1.18 and above)

## Installation

```
pip install shulkr
```

## Usage

```sh
shulkr 1.16 1.17 1.18
```

This will generate a commit with the decompiled source code for Minecraft 1.16,
1.17 and 1.18 in the current working directory:

```
204b37c (HEAD -> main, tag: 1.18) version 1.18
86dc440 (tag: 1.17) version 1.17
5d13494 (tag: 1.16) version 1.16
```

Note: It's okay to skip versions. Shulkr generates the complete source code for
each version before committing to git, so you can include as many or as little
intermediate versions as you would like.

## Version Patterns

Ranges of versions can be specified with `..` and `...`:
- `A..B` expands to all versions between `A` and `B` (inclusive), *not*
  including snapshots
- `A...B` expands to all versions between `A` and `B` (inclusive), including
  snapshots

`A` and/or `B` can be omitted, defaulting to the version after the most recent
commit and the latest supported version, respectively.

A *negative pattern* removes all matching versions that came before it. To
negate a pattern, add `-`. The following pattern expands to all versions after
`A`, up to and including `B` (the order is important):
- `A...B -A`

Note that you need to include `--` before the versions when using negative
versions, so the argument parser knows that the negative version is not an
option:

```sh
shulkr -- ...1.19 -1.19
```

## Options

### `--repo` / `-p`

By default the source code is generated in the current working directory. To
specify a different location:

```sh
shulkr --repo minecraft-sources 1.17..
```

If the directory does not exist, a new git repo will be created there.

### `--mappings`

By default, Minecraft's bytecode is deobfuscated using [yarn's] mappings. You
can also use `--mappings mojang` to use Mojang's official mappings. Yarn merges
the client and server sources into one directory, which Shulkr currently does
not support for Mojang's mappings.

If left unspecified, the mappings used to generate the previous commit are
detected.

### `--message` / `-m`

This option lets you customize the commit message format:

```sh
shulkr -m "Minecraft {}" 1.18-rc4
```

### `--no-tags` / `-T`

By default, each commit is tagged with the name of its Minecraft version. This
can be disabled with `--no-tags`.

## Experimental Options

### `--undo-renamed-vars` / `-u`

When this option is enabled, local variables that were renamed in new versions
will be reverted to their original names.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

Please make sure to update tests as appropriate.

At a high-level, shulkr does the following for each version of Minecraft
resolved from the supplied version patterns:
1. Generate the source code using [DecompilerMC]
2. Commit the version to git
3. Optionally, tag the version

## License

Licensed under the Apache License, Version 2.0.

[yarn's]: https://github.com/FabricMC/yarn
[Fork]: https://github.com/clabe45/shulkr/fork
[changelog]: https://github.com/clabe45/shulkr/blob/main/CHANGELOG.md
[usage guidelines]: https://github.com/clabe45/shulkr/blob/main/usage-guidelines.md
[DecompilerMC]: https://github.com/hube12/DecompilerMC

