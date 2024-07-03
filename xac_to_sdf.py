import subprocess
import sys
import os
import xml.etree.ElementTree as ET

def convert_xacro_to_sdf(xacro_file, world_name):
    # Define output file names
    urdf_file = "tmp.urdf"
    sdf_file = os.path.splitext(xacro_file)[0] + ".sdf"
    
    try:
        # Step 1: Convert xacro to urdf
        xacro_cmd = ["xacro", xacro_file, "-o", urdf_file]
        subprocess.run(xacro_cmd, check=True)
        
        # Step 2: Convert urdf to sdf
        sdf_cmd = ["ign", "sdf", "-p", urdf_file]
        sdf_output = subprocess.check_output(sdf_cmd, stderr=subprocess.STDOUT).decode()
        
        # Step 3: Process SDF output
        sdf_root = ET.fromstring(sdf_output)
        
        # Create SDF root element
        sdf_elem = ET.Element("sdf", version="1.7")
        
        # Add XML version as the first line
        xml_declaration = '<?xml version="1.0"?>'
        sdf_elem.text = xml_declaration + "\n"
        
        # Create world element with name attribute
        world_elem = ET.SubElement(sdf_elem, "world", name=world_name)
        world_elem.text = "\n  "  # Indentation for readability
        
        # Append children from sdf_root to world_elem
        for child in sdf_root:
            world_elem.append(child)
        
        # Write SDF to file
        sdf_tree = ET.ElementTree(sdf_elem)
        sdf_tree.write(sdf_file, xml_declaration=True, encoding='utf-8', method="xml")
        
        # Step 4: Remove tmp.urdf
        os.remove(urdf_file)
        
        print(f"Conversion successful. SDF file generated: {sdf_file}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error: Conversion failed with return code {e.returncode}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Required command not found. Make sure 'xacro' and 'ign' are installed and in PATH.")
        sys.exit(1)
    except ET.ParseError as e:
        print(f"Error parsing SDF output: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_xacro_to_sdf.py <xacro_file> <world_name>")
        sys.exit(1)
    
    xacro_file = sys.argv[1]
    world_name = sys.argv[2]
    convert_xacro_to_sdf(xacro_file, world_name)

