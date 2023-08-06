Mkdocs Asy (for Python 3)
=======================================

Inspired by

* [Rodrigo SCHWENCKE > mkdocs-graphviz](https://gitlab.com/rodrigo.schwencke/mkdocs-graphviz)

in order to get it work with pip for python 3 (pip3). No version for Python2.

A Python Markdown extension for Mkdocs, that renders inline Asy definitions with inline SVGs or PNGs out of the box !

Why render the graphs inline? No configuration! Works with any
Python-Markdown-based static site generator, such as [MkDocs](http://www.mkdocs.org/), [Pelican](http://blog.getpelican.com/), and
[Nikola](https://getnikola.com/) out of the box without configuring an output directory.

# Installation

1. You **must** have the **Asymptote binaries** installed in your machine.

e.g. in Manjaro Linux:

```bash
$ sudo pacman -S asymptote
$ sudo pacman -S pyqt5
$ sudo pacman -S python-cson
```

Then,

2. `$ pip install mkdocs-asy`

# Usage

Activate the `mkdocs_asy` extension. For example, with **Mkdocs**, you add a
stanza to `mkdocs.yml`:

```yaml
markdown_extensions:
    - mkdocs_asy
```

To use it in your Markdown doc, 

with SVG output:

    ```asy
    import math;
    import markers;

    size(6cm, 0);

    // Définition de styles de points
    marker croix = marker(scale(3)*cross(4),
                        1bp+gray);

    add(grid(6, 6, .8lightgray));

    pair pA = (1, 1), pB = (5, 5), pC = (2, 4);

    draw(pA--pB--pC--cycle);
    draw("$A$", pA, SW,blue, croix);  
    draw("$B$", pB, SE,blue, croix);  
    draw("$C$", pC, NW, croix);

    draw(pA--pC, StickIntervalMarker(1, 2, size=8, angle=-45, red));
    draw(pB--pC, StickIntervalMarker(1, 2, size=8, angle=-45, red));
    ```

or with PNG:

    ```asy png
    import math;
    import markers;

    size(6cm, 0);

    // Définition de styles de points
    marker croix = marker(scale(3)*cross(4),
                        1bp+gray);

    add(grid(6, 6, .8lightgray));

    pair pA = (1, 1), pB = (5, 5), pC = (2, 4);

    draw(pA--pB--pC--cycle);
    draw("$A$", pA, SW,blue, croix);  
    draw("$B$", pB, SE,blue, croix);  
    draw("$C$", pC, NW, croix);

    draw(pA--pC, StickIntervalMarker(1, 2, size=8, angle=-45, red));
    draw(pB--pC, StickIntervalMarker(1, 2, size=8, angle=-45, red));
    ```

# Credits

[Rodrigo SCHWENCKE](https://gitlab.com/rodrigo.schwencke/mkdocs-asy)

# License

[GPL3](https://opensource.org/licenses/GPL-3.0)
