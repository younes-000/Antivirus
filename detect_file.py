import os

def isfileMalicious(file_path,malicious_signatures):
    try:
        with open(file_path,'rb') as file:
            fileContent = file.read()
            if malicious_signatures in fileContent:
                return True
        return False
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return False
    
if __name__ == "__main__":
    malicious_signatures = b'MALWARE'
    file_path='example_file.txt'
    if isfileMalicious(file_path,malicious_signatures):
        print(f"File {file_path} is malicious.")
        # recuperer la ligne
        with open(file_path,'rb') as file:
            for i,line in enumerate(file):
                if malicious_signatures in line:
                    print(f"Malicious signature found on line {i+1}: {line.strip()}")
                    break
        os.remove(file_path)
                    

    else:
        print(f"File {file_path} is clean.")



