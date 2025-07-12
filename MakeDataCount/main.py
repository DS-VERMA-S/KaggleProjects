__author__ = "Sachin Verma"
__email__ = "verma.sachin.ds@gmail.com"
__description__ = "This is the main script for the project"


#---------- importing libraries -------------

## User defined imports
from MakeDataCount.parse_pdf_data import AcademicDocParser
from MakeDataCount.utils import setup_logger

## python imports
import os
from dotenv import load_dotenv
load_dotenv()


## setup logger
setup_logger("logger.txt")

## Extract data from PDF files
extracter = AcademicDocParser()
input_dir = os.getenv('INPUT_DIR')
output_dir = os.getenv('OUTPUT_DIR')
extracter.main(input_dir, output_dir)

## Prepare data for the LLM extraction
# This part is not implemented yet, but you can add your logic here to prepare the data

