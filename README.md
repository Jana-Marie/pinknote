# pinknote

---

pinknote is a simple Markdown to HTML renderer, that includes simple CSS and JS templates to render a web-page, ready for deployment from just a markdown file.

![awa](assets/pinknote.png)

#### why?

because I enjoyed it! :3 There are probably hundreds of such projects out there, but doing it myself was fun!

## Demo

This projects description is hosted at [pinknote.janamarie.dev](https://pinknote.janamarie.dev), compiled by pinknote!


## Usage

To generate a web-page you just need a Markdown file, render it via

    ./generate.py <Markdown>

With no additional paramets the HTML file will be put into `www/` and your assets into `www/assets/`. You can change this by passing the `-o <output-path>` parameter.

### Themes

To choose a different theme, a different CSS file you can use the option `-css static/css/<theme>.css`, thee following are currently inlcuded.

[TODO, put theme screenshots here :p]

I would love to see more themes contributed! :3

## Files

```
  ./ 
    assets/         - Contains the Image files for this repo
    static/
      assets/       - Put your assets in here
      css/          - Themes, stylesheets
      index.js      - The light-dark theme selector, put your additional JS in here
    temlates/       - index.html template
  generate.py       - The generator itself, run this to render your Markdown file
  README.md         - This file
```

## Todo

 - [ ] Set proper website title and meta var
 - [ ] Make JS package optional
