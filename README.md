# Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos
This repository contains Python code for calculation of the time to fixate (TTF) parameters from the eye-tracker videos recorded during driving simulation in [Nervtech](https://www.nervtech.com/) simulator. Also, the repository contains a sample eye tracker data video.

The current repository presents a supplementary code for the preprint titled "Effectiveness of a Time to Fixate for Fitness to Drive Evaluation in Neurological Patients" and shared on [arXiv](https://arxiv.org/ftp/arxiv/papers/2205/2205.08942.pdf) authored by Nadica Miljković and Jaka Sodnik.

If you find these parameters and R code useful for your own research and teaching class, please cite the following references:

1) Miljković, N., & Sodnik, J. (2023). NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos (v1.0.0). [Software code], Zenodo. https://doi.org/10.5281/zenodo.6560419
2) Miljković, N., & Sodnik, J. (2023, May). Sensing Time Effectiveness for Fitness to Drive Evaluation in Neurological Patients. Preprint in arXiv (pp. 1-23). https://doi.org/10.48550/arXiv.2205.08942
3) Motnikar, L., Stojmenova, K., Štaba, U. Č., Klun, T., Robida, K. R., & Sodnik, J. (2020). Exploring driving characteristics of fit-and unfit-to-drive neurological patients: A driving simulator study. Traffic Injury Prevention, 21(6), 359-364. https://doi.org/10.1080/15389588.2020.1764547

## GitHub repo contents
1) [data/user_1](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/tree/main/data/user_1) folder - contains user_1_raw.csv file with relevant data from the Tobii Pro Glasses 2 (Tobii Llc., Stockholm, Sweden) Eye Tracker
2) [video/user_1](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/tree/main/video/user_1) folder - contains all frames for user_1 (ID = 1) for collision scene extracted by extract_frames.py code
3) [license](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/blob/main/LICENSE) (GNU GPL v3.0)
4) [readme](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/blob/main/README.md) file
5) [extract_frames.py](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/blob/main/extract_frames.py) - Python code for video preprocessing
7) [parameter_table.py](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/blob/main/parameter_table.py) - Python code for creating data table parameters (please, note that parameters were added manually as we could not share the whole dataset)
8) [requirements.txt](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/blob/main/requirements.txt) - versions of used Python packages for appropriate reproducibility of results and for YOLO (You Only Look Once) application
9) [ttf.py](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/blob/main/ttf.py) - Python code for calculating TTF parameter
10) [user_1.mp4](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/blob/main/user_1.mp4) -  a silent video (sound is not provided due to the data anonimization) of a selected collision in driving simulation in user with ID = 1 (fit-to-drive)
11) [yolo5s.pt](https://github.com/NadicaSm/Time-To-Fixate-Calculation-from-the-Eye-Tracker-Videos/blob/main/yolov5s.pt) - PyTorch file for YOLO (You Only Look Once) application

## Disclaimer
The Python code is provided without any guarantee and it is not intended for medical purposes.

## Note
Table with TTF parameters and other relevant features for 56 neurological patients and R code for statistical analysis are available on Zenodo repository: Miljković, N., & Sodnik, J. (2023). Parameters for Statistical Evaluation of Time to Fixate Effectiveness for Assessment of Fitness to Drive [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6560246

## Acknowledgements
J.S. kindly acknowledges University Rehabilitation Institute Soča employees and the Nervtech team. Authors gratefully appreciate the support from Nenad B. Popović, PhD from University of Belgrade – School of Electrical Engineering for his valuable assistance in design of illustrations and for provided feedback for the initial manuscript structure. Also, both Authors thank Nebojša Jovanović, MSc from University of Belgrade - School of Electrical Engineering for his kind contribution to earlier stages of the project, especially for his work on developing Python code to capture time to fixate parameter. Last but not least, we are very thankful to Damjan Krstajić, founder and director of the Research Centre for Cheminformatics for his precious advices on statistical analysis in a retrospective study and to student Gregor Kovač from Faculty of Electrical Engineering, University of Ljubljana for his diligent work on YOLO application in driving simulation.

## Funding
N.M. acknowledges amiable support from the Grant No. 451-03-47/2023-01/200103 funded by the Ministry of Science, Technological Development and Innovation of the Republic of Serbia. This research was financially supported by Slovenian Research Agency within the research program ICT4QoL - Information and Communications Technologies for Quality of Life, grant number P2-0246, and the research project Neurophysiological and Cognitive Profiling of Driving Skills, grant number L2-8178.
