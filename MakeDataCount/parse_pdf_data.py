__version__ = "0.1.0"
__auther__ =  "sachin verma"
__email__ = "verma.sachin.ds@gmail.com"


import os 
import re
import pandas as pd
import pymupdf
import logging

@staticmethod
def setup_logger(log_file_path="log_output.txt"):
    """Setup logger to save logs to a text file and console."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler(log_file_path, mode='w', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
setup_logger("logger.txt")

class AcademicDocParser:
    """Class to parse academic documents and extract data"""

    def __init__(self):
        self.input_dir = None
        self.output_dir = None
        

    def parse_pdf(self, file_path):
        """Parse a PDF file and extract data"""
        if not os.path.exists(file_path):
            logging.info(f"File {file_path} does not exist")
            return None
        
        # Use docling to parse the PDF
        
        extracted_text = ""
        doc = pymupdf.open(file_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # or doc[page_num]
            text = page.get_text()
            extracted_text = extracted_text + text
            cleaned_text = self.clean_text(extracted_text)
        

        return cleaned_text 
        
        # Extract data using regex
    
    def clean_text(self, text):
        """Clean the extracted text"""
        # Remove extra spaces and newlines
        cleaned_text = re.sub(r'\s+', ' ', text)
        cleaned_text = cleaned_text.strip()
        return cleaned_text
        
    
    def main(self, input_dir, output_dir):
        """Main method to parse all PDF files in the input directory"""
        self.input_dir = input_dir
        self.output_dir = output_dir
        
        if not os.path.exists(self.output_dir):
            logging.info(f"Creating output directory: {self.output_dir}")
            os.makedirs(self.output_dir)
        
        for file_name in os.listdir(self.input_dir):
            logging.info(f"Processing file: {file_name}")
            if file_name.endswith('.pdf'):
                file_path = os.path.join(self.input_dir, file_name)
                parsed_text = self.parse_pdf(file_path)

                # Save the parsed data to output directory
                output_file_path = os.path.join(self.output_dir, f"{os.path.splitext(file_name)[0]}.txt")
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(parsed_text)
                logging.info(f"Parsed {file_name} successfully")
        
        ## save logging info to txt filr
        logging.info(f"Number of files to be parsed: {len(os.listdir(self.input_dir))}")
        logging.info(f"Number of files parsed successfully: {len(os.listdir(self.output_dir))}")
        logging.info(f"Output saved to {self.output_dir}")


