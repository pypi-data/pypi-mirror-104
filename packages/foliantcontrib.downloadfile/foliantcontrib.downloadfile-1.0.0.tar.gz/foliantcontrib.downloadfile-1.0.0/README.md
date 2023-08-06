[![](https://img.shields.io/pypi/v/foliantcontrib.downloadfile.svg)](https://pypi.org/project/foliantcontrib.downloadfile/)  [![](https://img.shields.io/github/v/tag/foliant-docs/foliantcontrib.downloadfile.svg?label=GitHub)](https://github.com/foliant-docs/foliantcontrib.downloadfile)

# DownloadFile Extension

DownloadFile is a configuration extension for Foliant which downloads external files to use in your project.

It also resolves `!download` YAML tag in the project config and inside XML-tags parameters.

## Installation

```bash
$ pip install foliantcontrib.downloadfile
```

## Usage

To configure DownloadFile add the following section to your foliant.yml file:

```yaml
downloadfile:
    queue:
        - url: https://example.com/image.png  # required
          save_to: images/img1.png
          login: john
          password: qwerty123
        - ...
```

`queue`
:   list of files to download. Each file is represented by a dictionary with the following fields:

`url`
:   **(requried)** URL to the file which should be downloaded.

`save_to`
:   path where the downloaded file should be saved, relative to the project root. If not supplied, file will be saved in the project root with the name from url.

`login`
:   login for basic authentication.

`password`
:   password for basic authentication.

> **Warning:** don't store plain text passwords in foliant.yml. Use [environment variables](https://foliant-docs.github.io/docs/config/#env).


### `!download` YAML tag

Another way to use DownloadFile is by specifying `!download` YAML tag. This is the quickest and the simplest way, but it comes with its disadvantages.

Insert the `!download` tag, followed by file URL, in any place in foliant.yml or tag parameters, where file path is expected:

```yaml
preprocessors:
    - swaggerdoc:
        spec_path: !download https://example.com/swagger.json
        mode: widdershins
```

```html
Generated template:

<template engine="jinja2" ext_context="!download https://example.com/mycontext.yml">
...
</template>
```

The downloaded file will be saved in the `.downloadfilecache` directory under a hashed name, and the `!download` tag will be replaced by absolute path to this file.

The cons of this method are that you can't change the saved file path nor other parameters. Also if you reference the same file twice with `!download` tag, it will be downloaded two times.
