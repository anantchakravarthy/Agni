# 🔥 Agni - The SMB PII/PHI Scanner 🔥

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
                                                                                

🌟 **Om Agnaye Namah** (ॐ अग्नये नमः) — Salutations to Agni, God of fire! 🔥

---

## 📌 **Overview**

**Agni** is a powerful **SMB Share Scanner** designed to **detect PII (Personally Identifiable Information) and PHI (Protected Health Information)** across **Windows SMB shares**.  

✔ **Automates SMB Share Enumeration & File Downloading**  
✔ **Scans for Emails, SSNs, IPs, Credit Cards, Names, and more!**  
✔ **Generates Detailed Reports for Each File Scanned**  
✔ **CLI with Fire ASCII Art 🔥**  

---

## 📌 **Installation**

1️⃣ Clone the Repository

git clone https://github.com/anantchakravarthy/Agni.git
cd Agni

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Download SpaCy NLP Model

python -m spacy download en_core_web_trf
📌 Usage
Prepare Your targets.csv File
The targets.csv file should contain IP addresses & SMB share names:


IP Address,Share Name
192.168.1.10,Public
192.168.1.15,Documents
192.168.1.20,Finance

Run the Scanner

python -m agni.scanner targets.csv username password
✔ targets.csv → List of SMB shares
✔ username → SMB username
✔ password → SMB password

📌 Example Output

🔥 Starting Agni - The SMB PII/PHI Scanner 🔥

🔍 Scanning share: Public on 192.168.1.10...
📥 Downloading confidential_report.txt from Public on 192.168.1.10...
🔎 Scanning confidential_report.txt for PII/PHI...
✅ Scan Complete! Results saved in confidential_report_results.txt

🔍 Scanning share: Documents on 192.168.1.15...
📥 Downloading finance_records.xlsx from Documents on 192.168.1.15...
🔎 Scanning finance_records.xlsx for PII/PHI...
✅ Scan Complete! Results saved in finance_records_results.txt

📌 Features
✔ Automated SMB Share Enumeration
✔ Downloads Files from SMB Shares
✔ Scans Files for PII/PHI using Regex + NLP
✔ Identifies Emails, SSNs, IPs, UUIDs, and More!
✔ Detailed Results in <filename>_results.txt

📌 License
This project is licensed under the MIT License. See the LICENSE file for details.

📌 Acknowledgments
🙏 Thanks to:

The SpaCy NLP Library for Name Entity Recognition.
The SMBMap & smbclient-ng tools for SMB operations.
ASCII Art Creators for inspiring the Agni flame.

🚀 Developed with 🔥 by Achakra7

🙏 May Agni Purify Your Data!

🔥 Next Steps

Would you like to add: ✔ Silent Mode to Disable ASCII Art for Automation?
✔ Multithreading for Faster SMB Scans?
✔ Option to Exclude Certain File Types?

Let me know, and I'll implement them! or even better we'll implement them!!🚀🔥