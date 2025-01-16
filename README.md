# README - Data Cleanup and Consolidation Projects

## Overview
This repository contains Python scripts designed for data cleanup and consolidation processes. The main focus of these projects is handling and enriching datasets through operations like splitting large datasets, validating and appending data using external APIs, and consolidating results into final outputs. Below is a detailed description of the projects and their functionalities.

---

## Project 1: **Handling Duplicate Partner IDs and Consolidating Contracts**

### Objective:
Identify duplicate `PartnerID` entries in a dataset, find the most recent contracts for those duplicates, and separate unique `PartnerID` entries into distinct files.

### Key Features:
1. Load data from an Excel file containing contract details.
2. Identify duplicate `PartnerID` entries.
3. Extract the most recent contract for each duplicate `PartnerID` based on the `Acceptance Date`.
4. Separate unique `PartnerID` entries.
5. Save results into two Excel files:
   - `recent_contracts.xlsx`: Contains the most recent contracts for duplicate `PartnerID`s.
   - `unique_partner_ids.xlsx`: Contains unique `PartnerID` entries.

### Input:
- An Excel file (`PMD-CMS.xlsx`) with columns including:
  - `PartnerID`
  - `Acceptance Date`
  - `Contract`

### Output:
- Two Excel files:
  - `recent_contracts.xlsx`
  - `unique_partner_ids.xlsx`

---

## Project 2: **CEP Validation and Data Enrichment**

### Objective:
Validate and enrich Brazilian postal codes (CEP) using an external API, handle large datasets by splitting and processing them incrementally, and consolidate the results into a final file.

### Key Features:
1. **Data Splitting**:
   - Split a large dataset into smaller chunks for efficient processing.
2. **CEP Validation**:
   - Validate each CEP using the OpenCEP API.
   - Enrich data by appending address details (e.g., `logradouro`, `bairro`, `cidade`).
3. **Consolidation**:
   - Merge validated and enriched data into the original dataset.
   - Save the final enriched dataset to an Excel file.

### Input:
- An Excel file (`PMD-CMS.xlsx`) with a column for CEPs (`CEP_NEW`).
- External API for CEP validation: [OpenCEP](https://opencep.com/).

### Output:
- Intermediate files:
  - Split datasets saved to the `Divididos` directory.
  - Processed files saved to the `revisados` directory.
- Final consolidated file:
  - `base_cep_consolidada.xlsx` in the `finalizados` directory.

### Steps:
1. **Load Dataset**:
   - Read the main dataset from the `PMD-CMS.xlsx` file.
2. **Clean CEP Data**:
   - Remove duplicates and standardize CEP formatting.
3. **Split Dataset**:
   - Divide the dataset into smaller files for batch processing.
4. **Process Files**:
   - Validate and enrich CEPs using the OpenCEP API.
5. **Consolidate Results**:
   - Merge processed files into a single consolidated dataset.
   - Update original dataset with enriched address details.

---

## Requirements

### Python Libraries:
- `pandas`: Data manipulation and analysis.
- `requests`: HTTP requests for API calls.
- `openpyxl`: Read and write Excel files.
- `os`: File and directory handling.
- `glob`: File pattern matching.

### External API:
- OpenCEP API for postal code validation and address enrichment.

---

## Directory Structure
```plaintext
.
├── DataSources
│   ├── PMD-CMS.xlsx           # Input data file
│   ├── Divididos             # Directory for split datasets
│   ├── revisados             # Directory for processed files
│   ├── finalizados           # Directory for final output files
│   └── GetInvoice.xlsx        # Additional dataset for merging (if required)
├── recent_contracts.xlsx      # Output file for recent contracts (Project 1)
├── unique_partner_ids.xlsx    # Output file for unique Partner IDs (Project 1)
├── base_cep_consolidada.xlsx  # Final consolidated dataset (Project 2)
└── README.md                  # Project documentation
```

---

## How to Run

1. **Setup**:
   - Ensure all required libraries are installed using:
     ```bash
     pip install pandas requests openpyxl
     ```

2. **Project 1**:
   - Run the script for handling duplicate Partner IDs.
   - Outputs will be saved in the `DataSources/finalizados` directory.

3. **Project 2**:
   - Update the paths in the script to match your directory structure.
   - Run the script to process CEPs and generate the consolidated file.

4. **Validate Outputs**:
   - Verify the final Excel files in the `finalizados` directory.

---

## Notes

- Ensure that the OpenCEP API is accessible for proper functionality.
- Adjust batch sizes and delays in API calls to avoid rate-limiting issues.
- Maintain the directory structure to avoid errors during file I/O operations.

---

## Contact
For questions or assistance, please contact:
- **Name**: [Your Name]
- **Email**: [Your Email]
- **GitHub**: [Your GitHub Profile]

