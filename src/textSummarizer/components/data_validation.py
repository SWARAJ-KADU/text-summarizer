import os
from textSummarizer.logging import logger
from textSummarizer.config.configuration import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_file_exist(self)-> bool:
        try:
            validation_status = True

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion","samsum_dataset"))
            required_files = self.config.ALL_REQUIRED_FILES

            for file in required_files:
                if file not in all_files:
                    validation_status = False
                    break
            
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
                
            return validation_status
                
        except Exception as e:
            raise e                 

