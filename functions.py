import re

def separate_data_and_info(input_string):
    data_info_array = []
    pattern = r'(\d+)\.\s*(.*?)\s*:\s*(https?://\S+)'    
    matches = re.findall(pattern, input_string)
    
    for match in matches:
        data_info_array.append((int(match[0]), match[1], match[2]))
    
    return data_info_array

# Example usage:

input_string = """1. American Museum of Natural History Dinosaur Database: https://www.amnh.org/explore/dinosaurs-and-extinct-creatures
2. Smithsonian Institution’s National Museum of Natural History’s Dinosaurs: https://naturalhistory.si.edu/dinosaurs
3. National Geographic’s Dinosaurs: https://www.nationalgeographic.com/science/prehistoric-world/dinosaurs/"""
result = separate_data_and_info(input_string)
print(result)
