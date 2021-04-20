import csv
import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt  
import cv2 
import base64

def convert_to_base64(img):
    return base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()

def test_base64(img_string):
    jpg_original = base64.b64decode(img_string)

    # Write to a file to show conversion worked
    with open('test.jpg', 'wb') as f_output:
        f_output.write(jpg_original)
    
    print('File saved as test.jpg')

def parseXML(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    data = {}

    data['folder'] = root.find('folder').text
    data['filename'] = root.find('filename').text
    data['path'] = root.find('path').text
    data['segmented'] = root.find('segmented').text
    data['database'] = root.find('source/database').text
    
    size = {}
    for i in root.findall('size/*'):
        size[i.tag] = i.text
    data['size'] = size
    
    tmp = []
    for c in root.findall('object'):
        objects = {}
        name = c.find('name').text
        objects['name'] = name
        for b in c.findall('bndbox/*'):
            objects[b.tag] = int(b.text)
        tmp.append(objects) 
    data['objects'] = tmp        
    return data


def draw_rectangles(img_path,xml_data,display=False,base64=False):
    src = cv2.imread(img_path)    
    objects = xml_data['objects']
    for obj in objects:
        cv2.rectangle(src, (obj['xmin'], obj['ymin']), (obj['xmax'], obj['ymax']), (0, 0, 255), 2)
        cv2.putText(src, obj['name'], (obj['xmin'], obj['ymin']-5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    if display:
        cv2.imshow('Source',src)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    if base64:
        return convert_to_base64(src)
    
    return src

