import os

def isFileCorrupt(file_path,expected_signature):
  try:
     with open(file_path,'rb') as file:
        actual_signature = file.read(len(expected_signature))
        return actual_signature != expected_signature
  except FileNotFoundError:
        print(f"File {file_path} not found.")
        return False
  except Exception as e: # Catch any other exceptions
        print(f"An error occurred: {e}") # Log the error
        return False 
  
def scanfiles(directory,expected_signature):
    for root,_,files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root,file)
            print(f"Scanning file: {file_path}")
            isFileCorrupt(file_path,expected_signature)
            if isFileCorrupt(file_path,expected_signature):
                print(f"File {file_path} is not corrupt.")
            else:
                print(f"File {file_path} is corrupt.")


if __name__ == "__main__":
    directory = '.'  # repertoire actuel
    expected_signature = b'EXPECTED_SIGNATURE'
    scanfiles(directory,expected_signature)