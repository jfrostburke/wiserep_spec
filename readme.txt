Details of wiserep submission here:
https://wiserep.weizmann.ac.il/spectra/uploadset

This script collects LCO spectra and sends them to wiserep.
It creates two files:
        A tarball of the spectra
        A metadata spreadsheet (.tsv)

Right now it doesn't actually do the emailing part, so email them to:
wiserep@weizmann.ac.il

------------------------------------------------

To use, you first have to create a conda evironment
so the sql queries can run. To do that:

conda env create -f wiserep.yml

(Will probably take a few minutes). Then activate it with:

source activate wiserep

After that, run the script to create the files, e.g.

get_spec.py -n SN2016bkv --all
