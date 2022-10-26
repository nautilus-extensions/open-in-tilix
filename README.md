<h1 align="center">
  Open In Tilix
</h1>

<p align="center">
  <strong>Open Tilix from Nautilus</strong>
</p>



<br>

<p align="center">
  <a href="https://hosted.weblate.org/engage/open-in-tilix">
    <img alt="Translation status" src="https://hosted.weblate.org/widgets/open-in-tilix/-/svg-badge.svg"/>
  </a>
  <a href="https://github.com/nautilus-extensions/open-in-tilix/actions/workflows/ci.yml">
    <img alt="CI status" src="https://github.com/nautilus-extensions/open-in-tilix/actions/workflows/ci.yml/badge.svg"/>
  </a>
  <a href="https://repology.org/project/open-in-tilix/versions">
    <img alt="Packaging status" src="https://repology.org/badge/tiny-repos/open-in-tilix.svg">
  </a>
</p>

<p align="center">
  <a href="https://matrix.to/#/#open-in-tilix:envs.net">
    <img alt="Chat on Matrix" src="https://img.shields.io/matrix/open-in-tilix:envs.net?label=matrix&logo=matrix"/>
  </a>
  <a href="https://discord.gg/jx23evUheB">
    <img alt="Chat on Discord" src="https://img.shields.io/discord/1034468191931465821?label=discord&logo=discord&logoColor=white"/>
  </a>
</p>


Open In Tilix is a simple Python extension for the Nautilus file manager that
add the ability to open tilix from the context menu.

This is inspired by the extension in the tilix repo but since tilix is unmaintained, the extension still using the old Nautilus API and it's not compatible with the latest version of Nautilus, I decided to create a new extension.

## 📦️ Installation

### Fedora (And derivatives) 

> **Warning**
> Not available yet.

### Debian (And derivates)

> **Warning**
> Not available yet.

### AUR 

open-in-tilix is available on AUR:

Using [Paru](https://github.com/morganamilo/paru):
    
```shell
paru -S open-in-tilix
```

For latest changes:

```shell
paru -S open-in-tilix-git
```

<details>
  <summary>🪛️ Without AUR helpers</summary>

```shell
git clone https://aur.archlinux.org/open-in-tilix.git
cd open-in-tilix
makepkg -sic
```

For latest changes:

```shell
git clone https://aur.archlinux.org/open-in-tilix-git.git
cd open-in-tilix-git
makepkg -sic
```

</details>


## 🏗️ Building from source

### Meson

#### Prerequisites

The following packages are required to build open-in-tilix:

- Python 3 `python`
- PyGObject `python-gobject`
- Python-Nautilus `python-nautilus`
- Nautilus `nautilus`
- Meson `meson`
- Ninja `ninja-build`

#### Build Instruction

##### Global installation

```shell
git clone https://github.com/nautilus-extensions/open-in-tilix.git
cd open-in-tilix
meson builddir --prefix=/usr/local
sudo ninja -C builddir install
```

##### Local build (for testing and development purposes)

```shell
git clone https://github.com/nautilus-extensions/open-in-tilix.git
cd open-in-tilix
./install.sh
```

> **Note** 
> During testing and developement, as a convenience, you can use the `install.sh` script to quickly rebuild local builds.


## 🙌 Contribute to Open In Tilix 

### Code

Fork this repository, then create a push request when you're done adding features or fixing bugs.

### Localization 

You can help open-in-tilix translate into your native language. If you found any typos
or think you can improve a translation, you can use the [Weblate](https://hosted.weblate.org/engage/open-in-tilix) platform.

[![Translations](https://hosted.weblate.org/widgets/open-in-tilix/-/open-in-tilix/287x66-white.png)](https://hosted.weblate.org/engage/open-in-tilix/)

## ✨️ Contributors

[![Contributors](https://contrib.rocks/image?repo=open-in-tilix/open-in-tilix)](https://github.com/nautilus-extensions/open-in-tilix/graphs/contributors)


## 💝 Acknowledgment

Special thanks to:

- Tilix team for the original extension
- [Weblate](https://weblate.org) for providing translation platform


## 📜 License

Open In Tilix is licensed under the [GNU General Public License v3.0](LICENSE)

