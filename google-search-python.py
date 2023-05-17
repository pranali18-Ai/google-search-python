from googlesearch import search
from jinja2 import Environment, FileSystemLoader

# Input query
query = input("Enter your query: ")

# Perform the search
search_results = list(search(query, tld="com", num=10, stop=10, pause=2))

# Load the HTML template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('search_results_template.html')

# Render the template with the search results
output = template.render(search_results=search_results)

# Write the HTML file
with open('search_results.html', 'w') as file:
    file.write(output)
