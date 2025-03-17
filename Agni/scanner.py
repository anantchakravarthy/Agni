import os
import subprocess
import re
import csv
import smbclient
from .pii_detector import PIIDetector

class SMBScanner:
    def __init__(self, csv_file, username, password, output_folder="scanned_files"):
        self.csv_file = csv_file
        self.username = username
        self.password = password
        self.output_folder = output_folder
        self.targets = []

        os.makedirs(output_folder, exist_ok=True)
        self.load_targets()

    def load_targets(self):
        """Load target IPs and file shares from the CSV file."""
        try:
            with open(self.csv_file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if len(row) >= 2:
                        self.targets.append((row[0].strip(), row[1].strip()))
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    def list_files(self, target_ip, share):
        """List files inside an SMB share."""
        file_list = []
        try:
            result = subprocess.run(
                ["smbclient-ng", "--host", target_ip, "-u", self.username, "-p", self.password, "--list", share],
                capture_output=True,
                text=True
            )
            output = result.stdout.split("\n")

            for line in output:
                match = re.search(r"^\s*([A-Za-z0-9._-]+\.\w+)\s+", line)
                if match:
                    file_list.append(match.group(1))
        except Exception as e:
            print(f"Error listing files in share {share} on {target_ip}: {e}")

        return file_list

    def download_file(self, target_ip, share, filename):
        """Download a file from an SMB share."""
        local_path = os.path.join(self.output_folder, f"{target_ip}_{share}_{filename}")

        try:
            smbclient.ClientConfig(username=self.username, password=self.password)
            remote_path = f"\\\\{target_ip}\\{share}\\{filename}"

            with smbclient.open_file(remote_path, mode="rb") as remote_file:
                with open(local_path, "wb") as local_file:
                    local_file.write(remote_file.read())

            return local_path
        except Exception as e:
            print(f"Failed to download {filename} from {share} on {target_ip}: {e}")
            return None

    def run(self):
        """Execute the SMB scanning and PII detection process."""
        
        # 🔥 Display Epic Agni ASCII Art in Red 🔥
        print("\033[91m")  # Start Red Color
        print(r"""
                                    
                                /@@@@@@@@@@&%@@@@@@(* .(@/                                
                             (@@@@@@@@@@@@@@@@#@@@@%%     *@/                             
                           .#@@@&&&&&&%&@@@@@@@&&@@#/       .&%                           
                          ,&,*@@@@@@@@@@@@@&%&@@@%%@          .&/                         
                         (#  .@@@@@%%%%%%%&&&&&@%#%.            /&                        
                        %*  #@@@@@@@@@@@@@@%#(%@%//              .@.                      
                       %*        *#%@@@@@@@@@&%@&&                .@.                     
                      /#              @@@@@(@@@@/(,/               *@                     
                      &.                .#@@@@@@%@@*                @,                    
                     ,#                   .%@@@@@#@,                (%                    
                     (/                     &@@@@@@@@@@@@@          ,@                    
                     (*                   ,&@@@@@@@@@@@@@&          ,@                    
                     (/                 .&@@@@@%,,@@%               ,@                    
                     *#              *@@&@@@@@@.  #@@@@@@@%(,       (&                    
                      &.           (@@.   ,@@@&             *%&     &*                    
                      *(         .@@.   (@@@@@*                    ,@                     
                       (/       ,@%   /@* &&.                      @,                     
                        .(     .@%   (@/ *@,                      @/                      
                          ,*   /@.       ,%.                    .@*                       
                               (@.                             (&                         
                               .@%                           *@*                          
                                .@&                        #@*                            
                                  *@#                   (@#                               
                                     /@&/.        ./&@%.                                  
                                          .,***,..                                        
                                                                                          
                       &@,           (&*    .#&*@...,@@@@,     ..*&...*@@@..              
                      &@@&        .@@.         *@.  .% &@@#      ,%   ,@@&                
                     #./@@%      (@@#               .%  /@@@,    ,%   ,@@&                
                    (*  #@@(    .@@@,               .%    &@@#   ,%   ,@@&                
                   ,(    &@@*   ,@@@.               .%     (@@@. ,%   ,@@&                
                  .&/(((((@@@    @@@.      .,,,,,,,*.&      .&@@(,%   ,@@&                
                  @       *@@&   *@@(         *@@@  .%        (@@@%   ,@@&                
                 @         (@@%    &@,        %@@.  .%         .@@%   ,@@&                
             .#%%&%%.    *%%&&&%%(   .%%(**(%&/   (%%&%%.        #% %%%&&&%%/             
                                                                                          
        """)
        print("\033[0m")  # Reset Color
        print("🔥 Starting Agni - The SMB PII/PHI Scanner 🔥\n")

        if not self.targets:
            print("No targets loaded from CSV!")
            return

        detector = PIIDetector()
        for target_ip, share in self.targets:
            print(f"🔍 Scanning share: {share} on {target_ip}...")
            files = self.list_files(target_ip, share)

            for filename in files:
                print(f"📥 Downloading {filename} from {share} on {target_ip}...")
                file_path = self.download_file(target_ip, share, filename)

                if file_path:
                    print(f"🔎 Scanning {file_path} for PII/PHI...")
                    detector.scan_file(file_path)


# Add an entry point function to allow execution from command line
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Automated SMB Share PII/PHI Scanner")
    parser.add_argument("csv_file", help="Path to the CSV file containing target IPs and shares")
    parser.add_argument("username", help="SMB username")
    parser.add_argument("password", help="SMB password")

    args = parser.parse_args()

    scanner = SMBScanner(args.csv_file, args.username, args.password)
    scanner.run()
