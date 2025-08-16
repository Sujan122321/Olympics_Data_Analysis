# Olympics_Data_Analysis
  
## Project Overview
Olympics Data Analysis is a Python project for exploring, analyzing, and visualizing historical Olympic Games data. It provides scripts and notebooks to help users gain insights into athlete performance, country participation, and trends over time.

## Folder Structure
```
App/
	app.py           # Main application script
	helpers.py       # Helper functions
	__pycache__/     # Python cache files
Data/
	athlete_events.csv  # Athlete event data
	noc_regions.csv     # NOC region data
Notebook/
	notebook.ipynb      # Jupyter notebook for analysis
	Data/
		athlete_events.csv
		noc_regions.csv
```

## Installation
1. Clone the repository:
	```powershell
	git clone https://github.com/Sujan122321/Olympics_Data_Analysis.git
	```
2. (Recommended) Create and activate a virtual environment:
	```powershell
	python -m venv venv
	.\venv\Scripts\activate
	```
3. Install required packages:
	```powershell
	pip install -r requirments.txt
	```

## Usage
- Run the main application:
	```powershell
	python App/app.py
	```
- Open and explore the Jupyter notebook:
	- Navigate to `Notebook/notebook.ipynb` and run the cells for interactive analysis.

## Data Sources
- `athlete_events.csv`: Contains athlete event data from the Olympic Games.
- `noc_regions.csv`: Contains National Olympic Committee region data.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements or new features.

## License
This project is licensed under the MIT License.