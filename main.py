from bs4 import BeautifulSoup, Comment
from selenium import webdriver
import re

def calculate_dom_size(html):

  soup = BeautifulSoup(html, "html.parser")
  return len(soup.findAll())


def reduce_dom(html):

  soup = BeautifulSoup(html, "html.parser")


  for element in soup.findAll(["meta"]):
    element.extract()

  for element in soup.findAll(text=lambda text: isinstance(text, Comment)):
    element.extract()

  for element in soup.findAll():
    if not element.contents:
      element.extract()

  for element in soup.findAll(style="display: none"):
    element.extract()

  for element in soup.findAll():
    element.attrs = {}

  for element in soup.findAll():
    if element.has_attr("role"):
      element.name = element["role"]

  for element in soup.findAll(["input", "textarea"]):
    element.name = "i"

  for element in soup.findAll(["script", "style"]):
    element.extract()


  return soup.decode()


with open("input.html", "r") as f:
  html = f.read()

html= re.sub(r'\n+', '\n', html)

reduced_html = reduce_dom(html)
reduced_html = re.sub(r'\n+', '\n', reduced_html)

with open("output.html", "w") as f:
  f.write(reduced_html)

dom_size_before = calculate_dom_size(html)
dom_size_after = calculate_dom_size(reduced_html)
percentage_reduction = (dom_size_before - dom_size_after) / dom_size_before * 100

print(dom_size_after,dom_size_before, percentage_reduction)