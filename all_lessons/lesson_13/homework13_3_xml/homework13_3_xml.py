import xml.etree.ElementTree as ET
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def groups_number(file, num):
    tree = ET.parse(file)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number')

        if number is None or not number.text:
            logging.info(f"This group has no 'number' element or it is empty.")

        elif number.text == str(num):
            timing_exbytes = group.find('timingExbytes')

            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')

                if incoming is not None:
                    logging.info(f"Group: number:{number.text}, incoming: {incoming.text}")

                else:
                    logging.info(f"Group: number:{number.text} has no 'incoming' element in 'timingExbytes'")
            else:
                logging.info(f"Group: number:{number.text} has no 'timingExbytes' element")


groups_number('groups.xml', 5)




