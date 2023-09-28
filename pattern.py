import re
import json

pattern = """
<td>{[{var}]}</td>
"""

text = """
<!DOCTYPE html>
(aaaaa)
<html>
<style>
table, th, td {
  border:1px solid black;
}
</style>
<body>

<h2>A basic HTML table</h2>

<table style="width:100%">
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>

<p>To understand the example better, we have added borders to the table.</p>

</body>
</html>
"""

pattern = pattern.strip()
text = text.strip()

pattern = re.escape(pattern)
pattern = pattern.replace('\{\[\{', '[')
pattern = pattern.replace('\}\]\}', ']')
# print(f'Given pattern is "{pattern}"')

variables = re.findall(r'\[(.*?)\]', pattern)
if not variables:
  print('Final results is []')

# print(F'Variables are {json.dumps(variables, indent=2)}')

search_pattern = re.sub(r'\[(.*?)\]', r'([a-z0-9\\s\\S]+)', pattern)
# print(f'Regex format search pattern is "{search_pattern}"')

matches = re.findall(search_pattern, text, flags=re.IGNORECASE)
final_result = []
for match in matches:
    if type(match) != tuple:
        match = match.strip()
        match = (match, )
        
    if not variables:
        continue
    
    final_result.append(dict(zip(variables, match)))
    
final_string = json.dumps(final_result, indent=2)
print(F'Final results is {final_string}')

