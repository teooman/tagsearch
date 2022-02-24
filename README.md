# tagsearch
Python Script to search regex on the tags of a given URL

# Installation

`git clone https://github.com/teomanyuksel/tagsearch/`
`cd tagsearch`
`pip install -r requirements.txt`

# Usage

python3 tagsearch.py -h

will show available arguments

# Example Usage

python3 tagsearch.py --url wikipedia.org --tag strong

Output:
`[*] Tags found: 
<strong class="jsl10n localized-slogan" data-jsl10n="portal.slogan">The Free Encyclopedia</strong>
<strong>English</strong>
<strong>日本語</strong>
<strong>Русский</strong>
<strong>Deutsch</strong>
<strong>Español</strong>
<strong>Français</strong>
<strong>中文</strong>
<strong>Italiano</strong>
<strong>Polski</strong>
<strong>Português</strong>
<strong class="jsl10n" data-jsl10n="portal.app-links.title">
<a class="jsl10n" data-jsl10n="portal.app-links.url" href="https://en.wikipedia.org/wiki/List_of_Wikipedia_mobile_applications">
Download Wikipedia for Android or iOS
</a>
</strong>
`
