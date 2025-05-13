#!/usr/bin/env python
import sys, argparse, pathlib
import markdown2, base64
import shutil
from jinja2 import Environment, FileSystemLoader

def render_markdown_to_html(source, template, css, js, favicon, assets, target):
  pathlib.Path(target).mkdir(parents=True, exist_ok=True)

  templateEnv = Environment(loader=FileSystemLoader(''))
  templateFile = templateEnv.get_template(template)

  with open(str(target) + '/index.html', 'w') as f:
    f.write(
      templateFile.render( \
        md=markdown2.markdown(source.read(), extras=["fenced-code-blocks"]),
        css=css.read(),
        js=js.read(),
        favicon=base64.b64encode(favicon.read()).decode('ascii')
      )
    )
    f.close()

    shutil.copytree(assets, str(target) + '/assets', dirs_exist_ok=True)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Pinknote, Markdown to HTML templater/renderer')
  
  parser.add_argument('-t', '--template', type=str, nargs='?', 
      default='templates/index.html', help='HTML template [default: templates/index.html]')
  parser.add_argument('-c', '--css', type=argparse.FileType('r'), nargs='?', 
      default='static/css/pinknote.css', help='Stylesheet [default: static/css/pinknote.css]')
  parser.add_argument('-j', '--js', type=argparse.FileType('r'), nargs='?', 
      default='static/index.js', help='JS Sources [default: static/index.js]')
  parser.add_argument('-f', '--favicon', type=argparse.FileType('rb'), nargs='?', 
      default='assets/favicon.png', help='Favicon (default: static/assets/favicon.png]')
  parser.add_argument('-a', '--assets', type=pathlib.Path, nargs='?', 
      default='static/assets/', help='Assets to copy to target (default: static/assets]')
  parser.add_argument('-o', '--output-path', type=pathlib.Path, nargs='?', 
      default='www', help='Output path [default: static/assets/favicon.png]')
  parser.add_argument('source', type=argparse.FileType('r'), help='Markdown file to process')

  args = parser.parse_args()

  render_markdown_to_html(args.source, args.template, args.css, args.js, args.favicon, args.assets, args.output_path)