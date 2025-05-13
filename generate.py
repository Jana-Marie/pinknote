#!/usr/bin/env python
import sys, argparse, pathlib
import markdown2
from jinja2 import Environment, FileSystemLoader

def render_markdown_to_html(source, template, css, js, favicon, target):
  pathlib.Path(target).mkdir(parents=True, exist_ok=True)

  print(target, template)

  templateEnv = Environment(loader=FileSystemLoader(''))
  templateFile = templateEnv.get_template(template)

  with open(str(target) + '/index.html', 'w') as f:
    print(templateFile.render(), file = f)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Pinknote, Markdown to HTML templater/renderer')
  
  parser.add_argument('-t', '--template', type=str, nargs='?', 
      default='templates/index.html', help='HTML template [default: templates/index.html]')
  parser.add_argument('-c', '--css', type=argparse.FileType('r'), nargs='?', 
      default='static/css/style.css', help='Stylesheet [default: static/css/style.css]')
  parser.add_argument('-j', '--js', type=argparse.FileType('r'), nargs='?', 
      default='static/index.js', help='JS Sources [default: static/index.js]')
  parser.add_argument('-f', '--favicon', type=str, nargs='?', 
      default='static/assets/favicon.png', help='Favicon (default: static/assets/favicon.png]')
  parser.add_argument('-o', '--output-path', type=pathlib.Path, nargs='?', 
      default='www', help='Output path [default: static/assets/favicon.png]')
  parser.add_argument('source', type=argparse.FileType('r'), help='Markdown file to process')

  args = parser.parse_args()

  render_markdown_to_html(args.source, args.template, args.css, args.js, args.favicon, args.output_path)