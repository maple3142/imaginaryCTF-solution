from xml.dom import minidom
import xml.etree.ElementTree as gfg


def test(username):
    root = gfg.Element("root")
    m1 = gfg.Element("data")
    root.append(m1)
    b1 = gfg.SubElement(m1, "username")
    b1.text = username
    b3 = gfg.SubElement(m1, "isAdmin")
    b3.text = "no"
    tree = gfg.ElementTree(root)
    tree = tree.getroot()
    xml_str = gfg.tostring(tree).decode().replace("&lt;", "<").replace("&gt;", ">")
    print(xml_str)
    xml_str = minidom.parseString(xml_str).toprettyxml(indent="    ")
    print(xml_str)
    parse_root = gfg.fromstring(xml_str)
    for child in parse_root:
        for childd in child:
            if childd.tag == "username":
                parse_username = "Welcome " + childd.text
            if childd.tag == "isAdmin":
                if childd.text == "no":
                    is_admin = "(employee)!"
                else:
                    is_admin = "(admin)! Your flag is <REDACTED>"
                print(is_admin)


test("admin</username><isAdmin>yes</isAdmin><username>asd")

# jctf{cl0s1ng_t4gs_4nd_0p3n1ng_t4gs_1n_xml} and go to /nextstep
