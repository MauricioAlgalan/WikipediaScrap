# WikipediaScrap

Scrap Wikipedia article.

Download the article content of a entry in wikipedia with link of the entry

## What I need

You need the folowing librarys instaled via pip:

requests
validators

## Also need:

lxml with html

## Usage:

python wikipedia.py \<Wikipedia article link\>

### Whit name only

If you use a *\*nix system* make executable and ruin it.

chmod +x sep.py

./wikipedia.py \<Wikipedia article link\>

## Results:

The script puts the content of the article in a sigle file named out.html. Is html raw without header or body content, only the \<div\> section with the article alone.

### Example:

python wikipedia.py https://en.wikipedia.org/wiki/Infinitesimal

pandoc -t latex --latex-engine=xelatex -f html -o Descartes.pdf out.html

## What I cand do with this?

You can convert the html file to other formats vìa <b>pandoc</b>. Nice results with pdf latex output format. If you can't convert use xelatex engine.
