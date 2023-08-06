<div align="center">
    <a href="https://pypi.org/project/kolore/" target="_blank" rel="noopener noreferrer">
        <img width="200" src="https://gitlab.com/AlvarBer/kolore/-/raw/master/radical_180.png" alt="Logo">
    </a>
</div>

# Kolore

Your tiny swiss-army knife for color palettes.

![Krita palette](https://gitlab.com/AlvarBer/kolore/-/raw/master/palette_demo.png)

## Install

`pip install kolore`

## Usage

Convert between various palette files, such as krita to unity

`kolore --in palette.colors --out palette.kpl`

To create a palette png from a krita palette file

`kolore --in palette.kpl --out palette.png`

You can also set the size of the generated image

`kolore --in palette.colors --out result.png --width 200 --height 100`

Get general help with

`kolore --help`

## Supported formats

### Input

* Krita palette files (`.kpl`)
* Unity color preset library (`.colors`)

### Output

* Krita palette files (`.kpl`)
* Unity color preset library (`.colors`)
* PNG images (`.png`)

## Pitfalls

HDR colors from unity are not supported!

This is just a prototype, please report any bugs.
