import xml.etree.ElementTree as EL

xml_data = """
<user>
    <id>1</id>
    <first_name>AN</first_name>
    <last_name>Mironoff</last_name>
    <age>44</age>
    <email>an@mail.ru</email>
    <address>
        <street> Main street</street>
        <city>Moscow</city>
        <zip>127000</zip>
    </address>
</user>
"""

root = EL.fromstring(xml_data)

print('User ID:',root.find('id').text)
print('User name:',root.find('first_name').text)