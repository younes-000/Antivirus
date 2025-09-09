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
  
if __name__ == "__main__":
    file_path='example_file.txt'
    expected_signature = b'EXPECTED_SIGNATURE'
    if isFileCorrupt(file_path,expected_signature):
        print(f"File {file_path} is corrupt.")
    else:
        print(f"File {file_path} is clean.")
  

    



   